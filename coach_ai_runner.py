from summarizer import build_summary
from coach_ai import get_coaching_feedback
import json

summary = build_summary()
feedback = get_coaching_feedback(summary)

# Save feedback for Streamlit
with open("data/feedback.json", "w") as f:
    json.dump({"summary": summary, "feedback": feedback}, f, indent=2)

print("Feedback saved to data/feedback.json")
