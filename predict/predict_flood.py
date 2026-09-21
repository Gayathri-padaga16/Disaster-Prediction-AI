def _level(score):
    if score >= 7:
        return "High"
    if score >= 4:
        return "Moderate"
    return "Low"

def predict_flood_risk(slope, twi, flow_accumulation, drainage, rainfall):
    """
    Lightweight baseline risk model for the deployable demo.
    It scores the supplied environmental features using transparent thresholds.
    Replace with the original trained model when its dataset/model artifact is available.
    """
    score = 0
    if rainfall >= 150: score += 3
    elif rainfall >= 80: score += 2
    elif rainfall >= 40: score += 1

    if twi >= 2: score += 2
    elif twi >= 0: score += 1

    if flow_accumulation >= 500: score += 2
    elif flow_accumulation >= 150: score += 1

    if drainage < 100: score += 2
    elif drainage < 250: score += 1

    if slope < 5: score += 1
    return _level(score)
