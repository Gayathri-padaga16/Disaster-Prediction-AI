import os
import requests

def _get_key():
    try:
        import streamlit as st
        return st.secrets.get("OPENWEATHER_API_KEY", os.getenv("OPENWEATHER_API_KEY"))
    except Exception:
        return os.getenv("OPENWEATHER_API_KEY")

def get_current_weather(city):
    api_key = _get_key()
    if not api_key:
        return None

    try:
        response = requests.get(
            "https://api.openweathermap.org/data/2.5/weather",
            params={"q": city, "appid": api_key, "units": "metric"},
            timeout=10,
        )
        if response.status_code != 200:
            return None

        data = response.json()
        return {
            "city": data.get("name", city),
            "temperature": round(data["main"]["temp"], 1),
            "humidity": data["main"]["humidity"],
            "wind_speed": round(data.get("wind", {}).get("speed", 0), 1),
            "pressure": data["main"]["pressure"],
            "weather": data["weather"][0]["description"].title(),
        }
    except Exception:
        return None
