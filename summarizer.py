import json
from datetime import date

def load_health_data():
    with open("data/health.json") as f:
        return json.load(f)

def build_summary():
    data = load_health_data()

    return {
        "date": str(date.today()),
        "cycle_phase": data.get("cycle_phase", "unknown"),
        "planned_workout": "Full body strength",
        "calories": data.get("calories", 0),
        "protein_g": data.get("protein_g", 0),
        "notes": data.get("symptoms", [])
    }
