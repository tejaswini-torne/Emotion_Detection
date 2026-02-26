from collections import Counter
import matplotlib.pyplot as plt


# ----------------------------
# DOMINANT EMOTION
# ----------------------------

def get_dominant_emotion(emotions):
    if not emotions:
        return "None"

    counts = Counter(emotions)
    max_count = max(counts.values())

    dominant = [e for e, c in counts.items() if c == max_count]

    if len(dominant) == 1:
        return dominant[0]
    else:
        return "Mixed"


# ----------------------------
# STABILITY
# ----------------------------

def calculate_stability(emotions):
    if len(emotions) < 2:
        return "Not enough data"

    changes = 0
    for i in range(1, len(emotions)):
        if emotions[i] != emotions[i - 1]:
            changes += 1

    total_transitions = len(emotions) - 1
    stability = 100 - (changes / total_transitions) * 100

    return round(stability, 2)


# ----------------------------
# MOOD SWINGS
# ----------------------------

def detect_mood_swings(emotions):
    if len(emotions) < 2:
        return 0

    swings = 0
    for i in range(1, len(emotions)):
        if emotions[i] != emotions[i - 1]:
            swings += 1

    return swings


# ----------------------------
# TREND DETECTION
# ----------------------------

def detect_trend(emotions):
    if len(emotions) < 3:
        return "Not enough data"

    positive = ["joy", "love"]
    negative = ["fear", "sadness", "anger"]

    score = 0
    for emotion in emotions:
        if emotion in positive:
            score += 1
        elif emotion in negative:
            score -= 1

    if score > 1:
        return "Positive Trend"
    elif score < -1:
        return "Negative Trend"
    else:
        return "Stable Trend"


# ----------------------------
# SUMMARY
# ----------------------------

def generate_summary(emotions, stability, swings, trend):

    dominant = get_dominant_emotion(emotions)

    summary = f"""
Behavioral Insight Summary:

• Dominant Emotion: {dominant}
• Emotional Stability Score: {stability}
• Mood Swings Detected: {swings}
• Emotional Trend: {trend}

Interpretation:
"""

    if dominant == "Mixed":
        summary += "Your emotional responses are varied, indicating dynamic shifts.\n"
    else:
        summary += f"Your responses show recurring patterns centered around '{dominant}'.\n"

    if stability == "Not enough data":
        summary += "More data is required to evaluate stability.\n"
    elif stability > 75:
        summary += "You demonstrate strong emotional consistency.\n"
    elif stability > 40:
        summary += "Moderate emotional variability observed.\n"
    else:
        summary += "Frequent emotional fluctuations detected.\n"

    if trend == "Positive Trend":
        summary += "Overall emotional direction appears to be improving.\n"
    elif trend == "Negative Trend":
        summary += "Overall emotional direction appears to be declining.\n"
    elif trend == "Stable Trend":
        summary += "No strong directional trend detected.\n"

    return summary.strip()


# ----------------------------
# BAR CHART
# ----------------------------

def generate_chart(history):
    if not history:
        return None

    emotions = [h["emotion"] for h in history]
    counts = Counter(emotions)

    fig = plt.figure()
    plt.bar(counts.keys(), counts.values())
    plt.xlabel("Emotions")
    plt.ylabel("Frequency")
    plt.title("Emotion Distribution")

    return fig


# ----------------------------
# TIMELINE CHART
# ----------------------------

def generate_timeline_chart(history):
    if not history:
        return None

    emotion_scale = {
        "anger": 0,
        "sadness": 1,
        "fear": 1,
        "surprise": 2,
        "joy": 3,
        "love": 3
    }

    emotions = [h["emotion"] for h in history]
    values = [emotion_scale.get(e, 2) for e in emotions]

    fig = plt.figure()
    plt.plot(range(1, len(values) + 1), values, marker='o')
    plt.xlabel("Session Step")
    plt.ylabel("Emotion Intensity Level")
    plt.title("Emotion Timeline Over Time")

    return fig