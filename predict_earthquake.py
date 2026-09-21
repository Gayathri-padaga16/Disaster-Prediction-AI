def predict_earthquake(magnitude, depth, latitude, longitude, tsunami):
    """
    Lightweight baseline risk assessment.
    This is not a seismic forecasting model; it classifies the supplied event
    characteristics into a risk level.
    """
    score = 0
    if magnitude >= 7.0: score += 4
    elif magnitude >= 6.0: score += 3
    elif magnitude >= 5.0: score += 2
    elif magnitude >= 4.0: score += 1

    if depth <= 20: score += 2
    elif depth <= 70: score += 1

    if tsunami == 1: score += 2

    if score >= 6:
        return "High"
    if score >= 3:
        return "Moderate"
    return "Low"
