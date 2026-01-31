# parser/parser.py
import os
import re

def parse_story(text):
    segments = []
    lines = text.strip().split("\n")
    seg_id = 1

    for line in lines:
        line = line.strip()
        if not line:
            continue

        if '"' in line:
            speaker = extract_speaker(line)
            dialogue = re.findall(r'"(.*?)"', line)
            dialogue_text = dialogue[0] if dialogue else line

            if speaker.lower() in ["he", "she", "they"] and last_speaker:
                speaker = last_speaker
            else:
                last_speaker = speaker

            segments.append({
                "id": seg_id,
                "type": "dialogue",
                "speaker": speaker,
                "text": dialogue_text
        })

        else:
            # narration
            segments.append({
                "id": seg_id,
                "type": "narration",
                "speaker": "narrator",
                "text": line
            })

        seg_id += 1

    return segments
BASE_DIR = os.path.dirname(__file__)
STORY_PATH = os.path.join(BASE_DIR, "sample_story.txt")

def extract_speaker(line):
    match = re.search(r'(\w+)\s+(said|replied|whispered)', line.lower())
    if match:
        return match.group(1).capitalize()
    return "unknown"
if __name__ == "__main__":
    with open(STORY_PATH, "r") as f:
        text = f.read()
    result = parse_story(text)
    for r in result:
        print(r)
