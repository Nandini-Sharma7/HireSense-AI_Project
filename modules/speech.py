import random

def analyze_speech():

    filler_words = random.randint(1, 8)

    speech_duration = random.randint(40, 120)

    confidence_score = max(
        50,
        100 - (filler_words * 5)
    )

    result = {
        "confidence": confidence_score,
        "filler_words": filler_words,
        "duration": speech_duration
    }

    return result