import { NextRequest } from 'next/server';
import { runCobolToPythonTranslation } from '@/lib/server/analysis';

export const dynamic = 'force-dynamic';

export async function GET(req: NextRequest) {
  const targetModelName = req.nextUrl.searchParams.get('modelName');
  
  const encoder = new TextEncoder();
  
  const customReadable = new ReadableStream({
    async start(controller) {
      let isClosed = false;
      const sendEvent = (data: string) => {
        if (isClosed) return;
        try {
          controller.enqueue(encoder.encode(`data: ${JSON.stringify({ type: 'progress', message: data })}\n\n`));
        } catch (e) {
          console.error('Failed to send SSE event', e);
        }
      };

      try {
        if (!targetModelName) {
           throw new Error('No target model name provided');
        }

        sendEvent('Starting background AI Translation...');
        
        const result = await runCobolToPythonTranslation(targetModelName, (msg) => {
          sendEvent(msg);
        });

        if (!isClosed) {
          if (result.success) {
            controller.enqueue(encoder.encode(`data: ${JSON.stringify({ type: 'complete', message: 'Translation Finished', success: true })}\n\n`));
          } else {
            controller.enqueue(encoder.encode(`data: ${JSON.stringify({ type: 'error', message: result.error || 'Translation failed' })}\n\n`));
          }
        }
      } catch (error: any) {
        console.error('Translation API route failed:', error);
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
