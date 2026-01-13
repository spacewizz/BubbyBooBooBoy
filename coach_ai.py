from openai import OpenAI
import os
import json

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
You are a fitness coach specializing in menstrual-cycle–aware training.
Give practical, non-medical workout and nutrition advice.
Respond in short bullet points.
"""

def get_coaching_feedback(summary: dict):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": f"""
Here is today's health summary:
{json.dumps(summary, indent=2)}

Provide:
1. Workout suggestion
2. Nutrition suggestion
3. Recovery tip
"""
            }
        ],
        temperature=0.4
    )
    return response.choices[0].message.content
