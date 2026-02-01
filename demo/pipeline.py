from parser.parser import parse_story
from ir.ir_builder import build_ir
from emotion_engine.emotion_engine import assign_emotion
from audio_engine.audio_engine import render_audio
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
STORY_PATH = os.path.join(BASE_DIR, "parser", "sample_story.txt")


def run_pipeline():
    with open(STORY_PATH, "r") as f:
        story_text = f.read()
    # 1. Parse story
    parsed_segments = parse_story(story_text)

    # 2. Build IR
    narrative_ir = build_ir(parsed_segments)

    # 3. Assign emotions  
    emotion_ir = assign_emotion(narrative_ir)

    print("\n--- EMOTION-ANNOTATED IR ---\n")
    for node in emotion_ir:
        print(node)

    # 4. Render audio
    print("\n--- PLAYING AUDIO ---\n")
    render_audio(emotion_ir)


if __name__ == "__main__":
    run_pipeline()
