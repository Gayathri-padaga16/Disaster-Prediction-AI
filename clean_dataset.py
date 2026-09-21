import pandas as pd

# Read Excel file
df = pd.read_excel("C:/Users/ahary/OneDrive/Desktop/disaster_GPT/flood_data/Pluvial_Flood_Dataset.xlsx")

# FIX: remove extra spaces from column names
df.columns = df.columns.str.strip()

# Remove unwanted columns
df_cleaned = df.drop(columns=["X", "Y", "Curvature", "Aspect"])

# Rename target column
df_cleaned = df_cleaned.rename(columns={"SUSCEP": "risk"})

# Save as CSV
df_cleaned.to_csv("C:/Users/ahary/OneDrive/Desktop/disaster_GPT/flood_data/Pluvial_Flood_Dataset.xlsx", index=False)

print("✅ Dataset cleaned successfully!")
print(df_cleaned.head())
