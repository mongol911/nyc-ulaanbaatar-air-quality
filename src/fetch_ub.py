import pandas as pd
import os
import re

# -----------------------------
# Paths
# -----------------------------
raw_file = '../data/raw/Ulaanbaatar Particulate Matter Sensor Data.csv'
processed_file = '../data/processed/ub_pm_data.csv'
summary_file = '../data/processed/ub_pm_summary.csv'

# Ensure processed folder exists
os.makedirs(os.path.dirname(processed_file), exist_ok=True)

# -----------------------------
# Load raw data
# -----------------------------
df_ub = pd.read_csv(raw_file, low_memory=False)

# Check column names
print("Columns found:", df_ub.columns)

# -----------------------------
# Extract UTC from date column
# -----------------------------
def extract_utc(s):
    if pd.isna(s):
        return pd.NaT
    match = re.search(r'utc=(.*?),', s)
    if match:
        return match.group(1)
    return pd.NaT

df_ub['date'] = df_ub['date'].apply(extract_utc)
df_ub['date'] = pd.to_datetime(df_ub['date'], errors='coerce')

# -----------------------------
# Filter for 2015–2018
# -----------------------------
df_ub_filtered = df_ub[(df_ub['date'] >= '2015-01-01') & (df_ub['date'] <= '2018-12-31')]

# Forward-fill missing values safely
df_ub_filtered.ffill(inplace=True)

# Save cleaned CSV
df_ub_filtered.to_csv(processed_file, index=False)
print("Cleaned Ulaanbaatar data saved:", processed_file)
print("Number of rows:", len(df_ub_filtered))

# -----------------------------
# Create summary CSV
# -----------------------------

# Copy cleaned DataFrame
df_summary = df_ub_filtered.copy()

# Extract year and month
df_summary['Year'] = df_summary['date'].dt.year
df_summary['Month'] = df_summary['date'].dt.month

# Define seasons
def get_season(month):
    if month in [12, 1, 2]:
        return 'Winter'
    elif month in [6, 7, 8]:
        return 'Summer'
    else:
        return 'Other'

df_summary['Season'] = df_summary['Month'].apply(get_season)

# Use correct PM column
pm_column = 'value'  # <--- this is the column with PM2.5 readings

# Calculate annual mean
annual_mean = df_summary.groupby('Year')[pm_column].mean().rename('Annual_mean')

# Calculate summer mean
summer_mean = df_summary[df_summary['Season'] == 'Summer'].groupby('Year')[pm_column].mean().rename('Summer_mean')

# Calculate winter mean
winter_mean = df_summary[df_summary['Season'] == 'Winter'].groupby('Year')[pm_column].mean().rename('Winter_mean')

# Combine all into one DataFrame
summary_df = pd.concat([annual_mean, summer_mean, winter_mean], axis=1).reset_index()

# Save summary CSV
summary_df.to_csv(summary_file, index=False)
print("UB PM summary saved:", summary_file)
print(summary_df)
