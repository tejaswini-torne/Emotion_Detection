import matplotlib.pyplot as plt
import pandas as pd

EMOJI_MAP = {
    "joy": "😊",
    "sadness": "😢",
    "anger": "😡",
    "fear": "😨",
    "surprise": "😲",
    "love": "❤️",
    "neutral": "😐"
}

def generate_analysis(history):
    if len(history) == 0:
        return None, None, None

    df = pd.DataFrame(history)

    # Pie Chart
    emotion_counts = df["emotion"].value_counts()
    fig1 = plt.figure(figsize=(5,5))
    plt.pie(emotion_counts, labels=emotion_counts.index, autopct='%1.1f%%')
    plt.title("Emotion Distribution")

    # Bar Chart
    fig2 = plt.figure(figsize=(6,4))
    emotion_counts.plot(kind="bar")
    plt.title("Emotion Frequency")
    plt.ylabel("Count")

    # Intensity Trend
    fig3 = plt.figure(figsize=(6,4))
    plt.plot(df["intensity"], marker="o")
    plt.title("Emotion Intensity Trend")
    plt.xlabel("Conversation Step")
    plt.ylabel("Confidence %")
    plt.ylim(0,100)

    return fig1, fig2, fig3