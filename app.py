```python
import streamlit as st

from utils.weather import get_current_weather
from llm.explain_risk import explain_disaster_risk

st.set_page_config(
    page_title="AI Disaster Prediction System",
    page_icon="🌍",
    layout="centered"
)


def load_css():
    try:
        with open("animations.css", encoding="utf-8") as f:
            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )
    except FileNotFoundError:
        pass


load_css()

st.title("🌍 AI-Based Disaster Prediction & Management System")

st.caption(
    "Enter a city to analyze its current environmental conditions "
    "and assess potential disaster risk."
)

st.divider()

# -----------------------------
# CITY INPUT
# -----------------------------

st.subheader("📍 Enter Location")

city = st.text_input(
    "City Name",
    value="Chennai",
    placeholder="Example: Chennai"
)

# -----------------------------
# CHECK DISASTER RISK
# -----------------------------

if st.button("🔍 Check Disaster Risk", type="primary"):

    if not city.strip():
        st.warning("Please enter a city name.")
        st.stop()

    with st.spinner("Fetching live environmental data..."):

        weather = get_current_weather(city)

    if not weather:
        st.error(
            "Unable to retrieve live weather data. "
            "Please check your OpenWeather API key and city name."
        )
        st.stop()

    # -----------------------------
    # LIVE WEATHER
    # -----------------------------

    st.divider()

    st.subheader("🌦️ Current Environmental Conditions")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Temperature",
        f"{weather['temperature']} °C"
    )

    col2.metric(
        "Humidity",
        f"{weather['humidity']} %"
    )

    col3.metric(
        "Wind Speed",
        f"{weather['wind_speed']} m/s"
    )

    st.caption(
        f"📍 {weather['city']} | "
        f"{weather['weather']} | "
        f"Pressure: {weather['pressure']} hPa"
    )

    # -----------------------------
    # BASIC ENVIRONMENTAL RISK
    # -----------------------------

    temperature = weather["temperature"]
    humidity = weather["humidity"]
    wind_speed = weather["wind_speed"]
    pressure = weather["pressure"]
    condition = weather["weather"].lower()

    risk_points = 0
    possible_risk = []

    # Heavy rain / storm conditions
    if any(word in condition for word in [
        "heavy rain",
        "thunderstorm",
        "torrential",
        "rain"
    ]):
        risk_points += 2
        possible_risk.append("Heavy rainfall / flooding")

    # Very high humidity
    if humidity >= 90:
        risk_points += 1

    # Strong wind
    if wind_speed >= 15:
        risk_points += 2
        possible_risk.append("Strong wind / storm conditions")
    elif wind_speed >= 10:
        risk_points += 1

    # Low atmospheric pressure
    if pressure < 1000:
        risk_points += 1

    # Extreme temperature
    if temperature >= 45 or temperature <= 5:
        risk_points += 1
        possible_risk.append("Extreme temperature")

    # -----------------------------
    # OVERALL RESULT
    # -----------------------------

    st.divider()
    st.subheader("🚨 Disaster Risk Assessment")

    if risk_points >= 4:

        risk_level = "HIGH"
        st.error("🚨 POTENTIAL DISASTER RISK DETECTED")

    elif risk_points >= 2:

        risk_level = "MODERATE"
        st.warning("⚠️ POTENTIAL ENVIRONMENTAL RISK DETECTED")

    else:

        risk_level = "LOW"
        st.success("✅ NO SIGNIFICANT DISASTER RISK DETECTED")

    st.write(f"**Overall Risk Level:** {risk_level}")

    if possible_risk:

        st.write("**Possible concern:**")

        for risk in possible_risk:
            st.write(f"- {risk}")

    else:

        st.write(
            "The current available environmental conditions do not "
            "indicate a significant immediate disaster-related risk."
        )

    # -----------------------------
    # AI EXPLANATION
    # -----------------------------

    st.divider()
    st.subheader("🤖 AI Risk Explanation")

    try:

        explanation = explain_disaster_risk(
            "Overall Environmental Risk",
            risk_level
        )

        st.write(explanation)

    except Exception:

        st.write(
            "The assessment is based on the currently available "
            "environmental data."
        )

    # -----------------------------
    # DISCLAIMER
    # -----------------------------

    st.divider()

    st.caption(
        "⚠️ This system provides an AI/ML-based risk assessment for "
        "educational purposes. It is not an official emergency warning "
        "system. Always follow local government and disaster-management "
        "authorities for real-world alerts."
    )
```
