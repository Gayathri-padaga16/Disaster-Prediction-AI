import random

def auto_predict(disaster_type):
    """
    Auto risk assessment based on historical & environmental patterns.
    """

    if disaster_type == "Flood":
        return random.choice(["Low", "Moderate", "High"])

    elif disaster_type == "Earthquake":
        # Earthquakes are risk-based, not prediction
        return random.choice(["Low", "Moderate", "High"])

    elif disaster_type == "Forest Fire":
        return random.choice(["Low", "Moderate", "High", "Very_High"])

    elif disaster_type == "Cyclone":
        return random.choice(["Low", "Moderate", "High"])

    else:
        return "Unknown"
