import streamlit as st
import json

st.set_page_config(page_title="Cycle-Aware Fitness", layout="centered")
st.title("🌸 Cycle-Aware Fitness Dashboard")

# Load summary + AI feedback
with open("data/feedback.json") as f:
    data = json.load(f)

summary = data["summary"]
feedback = data["feedback"]

st.subheader("📊 Today")
st.json(summary)

st.subheader("🏋️ AI Feedback & Suggestions")
st.write(feedback)
