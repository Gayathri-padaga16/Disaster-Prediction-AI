import pandas as pd

# Read Excel file (explicit engine)
df = pd.read_excel(
    "data/Pluvial_Flood_Dataset.xlsx",
    engine="openpyxl"
)

# Clean column names
df.columns = df.columns.str.strip()

# Save as CSV
df.to_csv("data/Pluvial_Flood_Dataset.csv", index=False)

print("✅ Excel converted to CSV successfully!")
print(df.head())
