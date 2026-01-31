# ir/schema.py

def narrative_ir_template():
    return {
        "scene_id": None,
        "sequence_id": None,
        "speaker": None,
        "role": None,          # narrator / character
        "content_type": None,  # narration / dialogue
        "text": None,

        # Emotion placeholders (Person 3 will fill later)
        "emotion": {
            "valence": 0.0,    # -1 (negative) to +1 (positive)
            "arousal": 0.0     # 0 (calm) to 1 (intense)
        },

        # Delivery / prosody placeholders
        "delivery": {
            "pace": 1.0,       # speaking rate multiplier
            "pause_before": 0,
            "pause_after": 0
        }
    }
