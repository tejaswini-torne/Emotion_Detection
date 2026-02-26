# 🌸 AI-Powered Emotion Analytics & Behavioral Insight System

## Overview
This project is an **AI-driven mental health and emotion analysis system** designed to help users track and understand their emotional state over time. By analyzing user text inputs, the system detects emotions, calculates behavioral insights, and visualizes trends with intuitive charts.  

The application combines **state-of-the-art NLP models** with **interactive visualizations** to provide users with meaningful insights about their emotional well-being.

## Features
- **Emotion Detection**: Detects emotions such as joy, sadness, anger, fear, surprise, love, and neutral from user text.  
- **Confidence Scoring**: Provides a confidence percentage for detected emotions.  
- **Behavioral Analysis**:  
  - Dominant emotion identification  
  - Emotional stability assessment  
  - Mood swing detection  
  - Trend analysis (positive, negative, or stable)  
- **Visual Analytics**:  
  - Emotion distribution (bar/pie charts)  
  - Timeline of emotion changes over conversation steps  
- **Interactive Web Interface**: Built with **Gradio**, allowing users to input text, view results, and reset sessions seamlessly.  

## Tech Stack
- **Python**  
- **PyTorch**  
- **Transformers** (Hugging Face pre-trained models)  
- **Gradio** (interactive web interface)  
- **Matplotlib & Pandas** (for data visualization)  

## Model
Uses the pre-trained Hugging Face model:  
**`j-hartmann/emotion-english-distilroberta-base`**  
- Classifies English text into 6-7 basic emotions  
- Provides probability scores for predictions  

## How to Use

1. Enter your thoughts or feelings in the text box.

2. Click Analyze to detect your emotions.

3. View:
Detected emotion & confidence
Behavioral insights summary
Emotion distribution chart
Emotion timeline chart

4. Use Clear to empty the input box.

5. Use Reset to start a new session with fresh analysis.

