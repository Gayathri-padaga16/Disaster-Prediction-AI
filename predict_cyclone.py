def predict_cyclone(inputs):
    """
    Lightweight baseline cyclone-risk assessment.
    Replace with a trained cyclone model when the original dataset/model
    artifact is available.
    """
    score = 0
    sst = inputs["Sea_Surface_Temperature"]
    pressure = inputs["Atmospheric_Pressure"]
    humidity = inputs["Humidity"]
    wind_shear = inputs["Wind_Shear"]
    vorticity = inputs["Vorticity"]
    ocean_depth = inputs["Ocean_Depth"]
    disturbance = inputs["Pre_existing_Disturbance"]
    proximity = inputs["Proximity_to_Coastline"]

    if sst >= 29: score += 2
    elif sst >= 27: score += 1

    if pressure <= 990: score += 3
    elif pressure <= 1005: score += 1

    if humidity >= 85: score += 2
    elif humidity >= 70: score += 1

    if wind_shear <= 10: score += 2
    elif wind_shear <= 20: score += 1

    if vorticity >= 0.00003: score += 2
    elif vorticity >= 0.00001: score += 1

    if disturbance == 1: score += 2
    if proximity <= 10: score += 1

    if score >= 9:
        return "High"
    if score >= 5:
        return "Moderate"
    return "Low"
