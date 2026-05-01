import { NextRequest } from 'next/server';
import { runFullAnalysis } from '@/lib/server/analysis';

// Prevents caching of this API route
export const dynamic = 'force-dynamic';

export async function GET(req: NextRequest) {
  const encoder = new TextEncoder();
  
  const customReadable = new ReadableStream({
    async start(controller) {
      let isClosed = false;
      // Helper to enqueue a message in SSE format
      const sendEvent = (data: string) => {
        if (isClosed) return;
        try {
          // SSE format: "data: ...\n\n"
          controller.enqueue(encoder.encode(`data: ${JSON.stringify({ type: 'progress', message: data })}\n\n`));
        } catch (e) {
          console.error('Failed to send SSE event', e);
        }
      };

      try {
        sendEvent('Starting background analysis...');
        
        // Run full analysis with progress tracking
        const results = await runFullAnalysis((msg) => {
          sendEvent(msg);
        });

        if (!isClosed) {
          controller.enqueue(encoder.encode(`data: ${JSON.stringify({ type: 'complete', message: 'Analysis Finished', success: true })}\n\n`));
        }
      } catch (error: any) {
        console.error('Analysis API route failed:', error);
        if (!isClosed) {
          try {
            controller.enqueue(encoder.encode(`data: ${JSON.stringify({ type: 'error', message: error.message || 'Unknown error occurred' })}\n\n`));
          } catch (e) {}
        }
      } finally {
        if (!isClosed) {
          isClosed = true;
          try { controller.close(); } catch (e) {}
        }
      }
    }
  });

  return new Response(customReadable, {
    headers: {
      'Content-Type': 'text/event-stream',
      'Cache-Control': 'no-cache, no-transform',
      'Connection': 'keep-alive',
    },
  });
}
