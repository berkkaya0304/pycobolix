import { NextRequest, NextResponse } from 'next/server';
import { spawn } from 'child_process';
import path from 'path';

export async function POST(req: NextRequest) {
  try {
    const data = await req.json();
    
    return new Promise((resolve) => {
      const scriptPath = path.join(process.cwd(), 'scripts', 'export_generic_chart.py');
      
      // Use python or python3 depending on what's available
      // On Windows it's usually python
      const pythonCommand = process.platform === 'win32' ? 'python' : 'python3';
      const pythonProcess = spawn(pythonCommand, [scriptPath]);
      
      let imageBuffer = Buffer.alloc(0);
      let errorStr = '';

      pythonProcess.stdout.on('data', (chunk) => {
        imageBuffer = Buffer.concat([imageBuffer, chunk]);
      });

      pythonProcess.stderr.on('data', (chunk) => {
        errorStr += chunk.toString();
      });

      pythonProcess.on('close', (code) => {
        if (code !== 0 || imageBuffer.length === 0) {
          console.error(`Python script failed. Code: ${code}, Error: ${errorStr}`);
          resolve(NextResponse.json({ error: 'Failed to generate chart' }, { status: 500 }));
        } else {
          let contentType = 'image/png';
          if (data.format === 'pdf') contentType = 'application/pdf';
          else if (data.format === 'jpg' || data.format === 'jpeg') contentType = 'image/jpeg';

          resolve(new NextResponse(imageBuffer, {
            status: 200,
            headers: {
              'Content-Type': contentType,
              'Content-Disposition': `attachment; filename="${data.title || 'chart'}.${data.format || 'png'}"`,
            },
          }));
        }
      });

      pythonProcess.on('error', (err) => {
        console.error('Failed to start python process:', err);
        resolve(NextResponse.json({ error: 'Failed to start python process. Make sure python is in PATH.' }, { status: 500 }));
      });

      // Send JSON data to the python script
      pythonProcess.stdin.write(JSON.stringify(data));
      pythonProcess.stdin.end();
    });
    
  } catch (err) {
    console.error('Export API error:', err);
    return NextResponse.json({ error: 'Invalid request' }, { status: 400 });
  }
}
