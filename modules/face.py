import random

def analyze_face():

    emotions = [
        "Confident",
        "Neutral",
        "Nervous",
        "Calm"
    ]

    detected_emotion = random.choice(emotions)

    confidence_score = random.randint(65, 95)

    return {
        "emotion": detected_emotion,
        "confidence": confidence_score
    }