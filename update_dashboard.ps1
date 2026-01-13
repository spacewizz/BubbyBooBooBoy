# Activate Python venv
& "C:\Users\Ken\health-dashboard\venv\Scripts\activate.ps1"

# Pull latest health JSON from iCloud
$HealthDir = "$env:USERPROFILE\iCloudDrive\HealthExports"
$LatestFile = Get-ChildItem $HealthDir -Filter "*.json" | Sort-Object LastWriteTime -Descending | Select-Object -First 1

Copy-Item $LatestFile.FullName "C:\Users\Ken\health-dashboard\data\health.json" -Force

# Run Python AI script
python "C:\Users\Ken\health-dashboard\coach_ai_runner.py"

# Optionally start Streamlit
Start-Process python -ArgumentList "C:\Users\Ken\health-dashboard\app.py"
