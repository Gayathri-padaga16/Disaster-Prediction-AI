import os

def _local_explanation(disaster, risk):
    messages = {
        "Low": "The supplied conditions indicate a lower relative risk under this baseline assessment. Continue normal monitoring and follow official local alerts.",
        "Moderate": "The supplied conditions indicate a moderate relative risk. Keep monitoring environmental conditions and official warnings.",
        "High": "The supplied conditions indicate a higher relative risk. Follow official emergency guidance and monitor updated information closely.",
    }
    return f"{disaster} assessment: {messages.get(risk, 'Review the input values and official alerts for guidance.')}"

def explain_disaster_risk(disaster, risk):
    """
    Uses Gemini when GEMINI_API_KEY is configured; otherwise returns a
    safe local explanation so the app remains deployable without an LLM key.
    """
    key = None
    try:
        import streamlit as st
        key = st.secrets.get("GEMINI_API_KEY")
    except Exception:
        key = None
    key = key or os.getenv("GEMINI_API_KEY")

    if not key:
        return _local_explanation(disaster, risk)

    try:
        from google import genai
        client = genai.Client(api_key=key)
        prompt = (
            f"Explain this disaster risk assessment in 3 concise sentences. "
            f"Disaster: {disaster}. Risk level: {risk}. "
            f"Do not claim to predict a disaster or give emergency instructions "
            f"beyond advising the user to follow official local alerts."
        )
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt,
        )
        return response.text.strip() if response.text else _local_explanation(disaster, risk)
    except Exception:
        return _local_explanation(disaster, risk)

def explain_flood_risk(risk):
    return explain_disaster_risk("Flood", risk)
