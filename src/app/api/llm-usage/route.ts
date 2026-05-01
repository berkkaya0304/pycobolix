import { NextResponse } from 'next/server';
import fs from 'fs';
import path from 'path';

export const dynamic = 'force-dynamic';

export async function GET() {
  try {
    const LLM_USAGE_FILE = path.join(process.cwd(), 'public', 'output', 'llm_usage.json');
    
    if (!fs.existsSync(LLM_USAGE_FILE)) {
      return NextResponse.json([]);
    }
    
    const data = fs.readFileSync(LLM_USAGE_FILE, 'utf-8');
    return NextResponse.json(JSON.parse(data));
  } catch (error: any) {
    console.error('Failed to read LLM usage data:', error);
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}
