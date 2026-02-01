# audio_engine/audio_engine.py

import asyncio
import edge_tts
import os

VOICE_NARRATOR = "en-US-AriaNeural"
VOICE_CHARACTER = "en-US-GuyNeural"

OUTPUT_DIR = "demo/audio_output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

async def _speak(text, voice, filename):
    communicate = edge_tts.Communicate(text=text, voice=voice)
    await communicate.save(filename)

def render_audio(ir_nodes):
    async def generate():
        for idx, node in enumerate(ir_nodes):
            voice = VOICE_NARRATOR if node["speaker"] == "narrator" else VOICE_CHARACTER
            filename = os.path.join(OUTPUT_DIR, f"line_{idx+1}.wav")
            await _speak(node["text"], voice, filename)

    asyncio.run(generate())

