# emotion_engine/emotion_engine.py

def assign_emotion(ir_nodes):
    """
    Takes Narrative IR and enriches it with emotion values.
    """
    enriched_ir = []

    for node in ir_nodes:
        text = node["text"].lower()

        # Default values
        valence = 0.0
        arousal = 0.3

        # Dialogue vs narration
        if node["content_type"] == "dialogue":
            arousal = 0.5
        else:
            arousal = 0.2

        # Determination
        if any(word in text for word in ["won't", "never", "must", "fight", "give up"]):
            valence = 0.5
            arousal = 0.6

        # Fear / tension
        if any(word in text for word in ["whispered", "creaked", "dark", "shadow", "fear"]):
            valence = -0.6
            arousal = 0.7

        node["emotion"]["valence"] = valence
        node["emotion"]["arousal"] = arousal

        enriched_ir.append(node)

    return enriched_ir
