# ir/ir_builder.py

from .schema import narrative_ir_template

def build_ir(parsed_segments):
    ir = []
    scene_id = 1

    for idx, segment in enumerate(parsed_segments):
        node = narrative_ir_template()

        node["scene_id"] = scene_id
        node["sequence_id"] = idx + 1
        node["speaker"] = segment["speaker"]
        node["role"] = "narrator" if segment["speaker"] == "narrator" else "character"
        node["content_type"] = segment["type"]
        node["text"] = segment["text"]

        ir.append(node)

    return ir
if __name__ == "__main__":
    sample_input = [
        {
            "id": 1,
            "type": "narration",
            "speaker": "narrator",
            "text": "The wind howled through the empty street."
        },
        {
            "id": 2,
            "type": "dialogue",
            "speaker": "Rahul",
            "text": "I won't give up."
        }
    ]

    ir = build_ir(sample_input)
    for node in ir:
        print(node)


