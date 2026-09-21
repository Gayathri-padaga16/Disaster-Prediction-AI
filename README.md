# AI-Based Disaster Prediction & Management System

A Streamlit application for disaster-risk assessment covering Flood, Earthquake and Cyclone scenarios.

## Features
- Flood, earthquake and cyclone risk assessment
- Optional live weather using OpenWeather
- Optional Gemini-generated explanations
- Streamlit web interface

## Important model note
The original uploaded project did not contain the `utils`, `predict`, `llm`, datasets, or trained model artifacts referenced by `app.py`.
This deployable version therefore includes **transparent baseline risk-assessment functions**, not the missing original trained models. Replace the functions in `predict/` with the original trained models if those artifacts become available.

## Streamlit Cloud secrets
Add these only if you want the corresponding optional services:

```toml
OPENWEATHER_API_KEY = "your_openweather_key"
GEMINI_API_KEY = "your_gemini_key"
```

The app can still run without these keys; live weather and Gemini explanations will be unavailable.
