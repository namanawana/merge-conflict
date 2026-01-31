# audio_engine/audio_engine.py

import pyttsx3
import time

def render_audio(ir_nodes, output_file=None):
    engine = pyttsx3.init()

    # Optional: list available voices
    voices = engine.getProperty('voices')

    for node in ir_nodes:
        text = node["text"]
        emotion = node["emotion"]
        delivery = node["delivery"]

        # Map emotion to speech properties
        base_rate = 170
        rate = int(base_rate * delivery["pace"] + emotion["arousal"] * 30)
        engine.setProperty('rate', rate)

        # Simple volume control using valence
        volume = 0.7 + (emotion["valence"] * 0.2)
        engine.setProperty('volume', max(0.3, min(volume, 1.0)))

        # Speaker-based voice selection (basic)
        if node["speaker"] != "narrator" and len(voices) > 1:
            engine.setProperty('voice', voices[1].id)
        else:
            engine.setProperty('voice', voices[0].id)

        # Pause before
        time.sleep(delivery["pause_before"] / 1000)

        engine.say(text)
        engine.runAndWait()

        # Pause after
        time.sleep(delivery["pause_after"] / 1000)
