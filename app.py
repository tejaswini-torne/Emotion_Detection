import gradio as gr
from emotion_engine import detect_emotion
from behavior_analysis import (
    calculate_stability,
    detect_mood_swings,
    detect_trend,
    generate_summary,
    generate_chart,
    generate_timeline_chart
)

# ---------------------------
# ANALYSIS FUNCTION
# ---------------------------

def analyze_text(text, history):

    if history is None:
        history = []

    if not text.strip():
        return "Enter some text.", "", None, None, history

    emotion, confidence = detect_emotion(text)

    history.append({
        "text": text,
        "emotion": emotion,
        "confidence": confidence
    })

    emotions = [h["emotion"] for h in history]

    stability = calculate_stability(emotions)
    swings = detect_mood_swings(emotions)
    trend = detect_trend(emotions)

    summary = generate_summary(emotions, stability, swings, trend)

    distribution_chart = generate_chart(history)
    timeline_chart = generate_timeline_chart(history)

    result = f"Detected Emotion: {emotion}\nConfidence: {confidence}%"

    return result, summary, distribution_chart, timeline_chart, history


# ---------------------------
# CLEAR INPUT
# ---------------------------

def clear_input():
    return ""


# ---------------------------
# RESET SESSION
# ---------------------------

def reset_session():
    return "", "", None, None, []


# ---------------------------
# UI
# ---------------------------

with gr.Blocks(theme=gr.themes.Soft()) as demo:

    gr.Markdown("# 🌸 Emotion Detection 🌸")
    gr.Markdown("### AI-Powered Emotion Analytics and Behavioral Insight System")

    history_state = gr.State([])

    with gr.Row():

        # LEFT
        with gr.Column():
            gr.Markdown("#### 🧠 Enter Your Thoughts")
            user_input = gr.Textbox(lines=5, placeholder="Type your feelings...")

            with gr.Row():
                analyze_btn = gr.Button("Analyze", variant="primary")
                clear_btn = gr.Button("Clear", variant="secondary")
                reset_btn = gr.Button("Reset", variant="stop")

        # RIGHT
        with gr.Column():
            gr.Markdown("#### 📊 Emotion Result")
            result_output = gr.Textbox(lines=3)

            gr.Markdown("#### 🔎 Behavioral Insights")
            summary_output = gr.Textbox(lines=8)

    gr.Markdown("#### 📈 Emotion Analytics")

    with gr.Row():
        distribution_output = gr.Plot(label="Emotion Distribution")
        timeline_output = gr.Plot(label="Emotion Timeline")

    # Button Actions
    analyze_btn.click(
        analyze_text,
        inputs=[user_input, history_state],
        outputs=[result_output, summary_output, distribution_output, timeline_output, history_state]
    )

    clear_btn.click(
        clear_input,
        outputs=user_input
    )

    reset_btn.click(
        reset_session,
        outputs=[result_output, summary_output, distribution_output, timeline_output, history_state]
    )

if __name__ == "__main__":
    demo.queue().launch()