import streamlit as st

from utils.weather import get_current_weather
from predict.predict_flood import predict_flood_risk
from predict.predict_earthquake import predict_earthquake
from predict.predict_cyclone import predict_cyclone
from llm.explain_risk import explain_disaster_risk

st.set_page_config(
    page_title="AI Disaster Prediction System",
    page_icon="🌍",
    layout="centered"
)

def load_css():
    try:
        with open("animations.css", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        pass

load_css()

st.title("🌍 AI-Based Disaster Prediction & Management System")
st.caption(
    "Machine-learning-based disaster risk assessment using environmental "
    "features, live weather context, and explainable results."
)

st.divider()
st.markdown('<div class="weather-card">🌦️ Live Weather</div>', unsafe_allow_html=True)

city = st.text_input("Enter City Name", value="Chennai")
weather = get_current_weather(city)

if weather:
    col1, col2, col3 = st.columns(3)
    col1.metric("🌡️ Temperature (°C)", weather["temperature"])
    col2.metric("💧 Humidity (%)", weather["humidity"])
    col3.metric("🌬️ Wind Speed (m/s)", weather["wind_speed"])
    st.caption(
        f"📍 {weather['city']} | {weather['weather']} | "
        f"Pressure: {weather['pressure']} hPa"
    )
else:
    st.info(
        "Live weather is unavailable. Add OPENWEATHER_API_KEY to Streamlit "
        "Secrets to enable it. Disaster risk assessment can still be used."
    )

st.divider()

disaster = st.selectbox(
    "Select Disaster Type",
    ["Flood", "Earthquake", "Cyclone"]
)

st.divider()

if disaster == "Flood":
    st.subheader("🌊 Flood Input Parameters")
    slope = st.number_input("Slope", value=60.0)
    twi = st.number_input("Topographic Wetness Index (TWI)", value=-4.1)
    fa = st.number_input("Flow Accumulation (FA)", value=150.0)
    drainage = st.number_input("Drainage", value=235.0)
    rainfall = st.number_input("Rainfall (mm)", value=120.0)

    if st.button("Predict Flood Risk", type="primary"):
        risk = predict_flood_risk(slope, twi, fa, drainage, rainfall)
        st.subheader(f"🚨 Flood Risk Level: {risk}")
        st.write(explain_disaster_risk("Flood", risk))

elif disaster == "Earthquake":
    st.subheader("🌋 Earthquake Input Parameters")
    magnitude = st.number_input("Magnitude", value=6.5)
    depth = st.number_input("Depth (km)", value=50.0)
    latitude = st.number_input("Latitude", value=10.0)
    longitude = st.number_input("Longitude", value=76.0)
    tsunami = st.selectbox("Tsunami Warning", [0, 1])

    if st.button("Predict Earthquake Risk", type="primary"):
        risk = predict_earthquake(
            magnitude, depth, latitude, longitude, tsunami
        )
        st.subheader(f"🚨 Earthquake Risk Level: {risk}")
        st.write(explain_disaster_risk("Earthquake", risk))

else:
    st.subheader("🌪️ Cyclone Input Parameters")
    sea_temp = st.number_input("Sea Surface Temperature (°C)", value=28.0)
    pressure = st.number_input("Atmospheric Pressure (hPa)", value=1005.0)
    humidity = st.number_input("Humidity (%)", value=80.0)
    wind_shear = st.number_input("Wind Shear", value=15.0)
    vorticity = st.number_input("Vorticity", value=0.00002, format="%.7f")
    ocean_depth = st.number_input("Ocean Depth", value=80.0)
    latitude = st.number_input("Latitude", value=15.0)
    pre_disturbance = st.selectbox("Pre-existing Disturbance", [0, 1])
    proximity = st.number_input("Proximity to Coastline (km)", value=1.5)

    if st.button("Predict Cyclone Risk", type="primary"):
        inputs = {
            "Sea_Surface_Temperature": sea_temp,
            "Atmospheric_Pressure": pressure,
            "Humidity": humidity,
            "Wind_Shear": wind_shear,
            "Vorticity": vorticity,
            "Ocean_Depth": ocean_depth,
            "Latitude": latitude,
            "Pre_existing_Disturbance": pre_disturbance,
            "Proximity_to_Coastline": proximity,
        }
        risk = predict_cyclone(inputs)
        st.subheader(f"🚨 Cyclone Risk Level: {risk}")
        st.write(explain_disaster_risk("Cyclone", risk))
