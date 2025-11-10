import pandas as pd
import os

# Paths
raw_file = '../data/raw/NYC_Air_Quality.csv'
processed_file = '../data/processed/nyc_pm_data.csv'
summary_file = '../data/processed/nyc_pm_summary.csv'

# Ensure processed folder exists
os.makedirs(os.path.dirname(processed_file), exist_ok=True)

# Load raw data
df_nyc = pd.read_csv(raw_file, low_memory=False)
print("Columns found:", df_nyc.columns)

# Filter PM2.5 rows
df_pm25 = df_nyc[df_nyc['Name'] == 'Fine particles (PM 2.5)'].copy()

# Convert Start_Date to datetime and extract year
df_pm25['Start_Date'] = pd.to_datetime(df_pm25['Start_Date'], errors='coerce')
df_pm25['Year'] = df_pm25['Start_Date'].dt.year

# Extract season from Time Period column (first word, e.g., 'Winter', 'Summer')
df_pm25['Season'] = df_pm25['Time Period'].str.split().str[0]

# Filter for years 2015–2018
df_pm25 = df_pm25[(df_pm25['Year'] >= 2015) & (df_pm25['Year'] <= 2018)]

# Save filtered & cleaned CSV
df_pm25.to_csv(processed_file, index=False)
print(f"✅ Filtered & cleaned NYC PM2.5 data saved: {processed_file}")
print(f"Number of rows: {len(df_pm25)}")

# -----------------------------
# Create summary CSV
# -----------------------------
# Compute annual mean
annual_mean = df_pm25.groupby('Year')['Data Value'].mean().rename('Annual_mean')

# Compute summer mean
summer_mean = df_pm25[df_pm25['Season'].str.lower() == 'summer'].groupby('Year')['Data Value'].mean().rename('Summer_mean')

# Compute winter mean
winter_mean = df_pm25[df_pm25['Season'].str.lower() == 'winter'].groupby('Year')['Data Value'].mean().rename('Winter_mean')

# Combine into summary DataFrame
summary_df = pd.DataFrame({
    'Year': annual_mean.index,
    'Annual_mean': annual_mean.values,
    'Summer_mean': summer_mean.reindex(annual_mean.index).values,
    'Winter_mean': winter_mean.reindex(annual_mean.index).values
})

# Save summary CSV
summary_df.to_csv(summary_file, index=False)
print(f"✅ NYC PM summary saved: {summary_file}")
print(summary_df)
