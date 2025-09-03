import pandas as pd

# Load dataset
df = pd.read_csv("Amazon Sale Report.csv")

# # Interpolate numeric columns
# df['Qty'] = df['Qty'].interpolate(method='linear')
# df['Amount'] = df['Amount'].interpolate(method='linear')

# # Fill missing values in non-numeric columns
# df['currency'] = df['currency'].fillna('INR')
# df['ship-city'] = df['ship-city'].fillna('Unknown')
# df['ship-state'] = df['ship-state'].fillna('Unknown')
# df['ship-country'] = df['ship-country'].fillna('Unknown')

# # Convert Date column
# df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# # Save cleaned data
# df.to_csv("Amazon_Sale_Report_Cleaned_Interpolated.csv", index=False)
# print("✅ Interpolated and saved successfully.")

print(df.shape)


