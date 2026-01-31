from parser.parser import parse_story
from ir.ir_builder import build_ir
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
STORY_PATH = os.path.join(BASE_DIR, "parser", "sample_story.txt")
# demo/pipeline.py

from parser.parser import parse_story
from ir.ir_builder import build_ir
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
STORY_PATH = os.path.join(BASE_DIR, "parser", "sample_story.txt")


def run_pipeline():
    with open(STORY_PATH, "r") as f:
        story_text = f.read()

    parsed_segments = parse_story(story_text)
    narrative_ir = build_ir(parsed_segments)

    print("\n--- NARRATIVE IR OUTPUT ---\n")
    for node in narrative_ir:
        print(node)


if __name__ == "__main__":
    run_pipeline()
