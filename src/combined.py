import pandas as pd
import os

# Paths
nyc_file = '../data/processed/nyc_pm_summary.csv'
ub_file = '../data/processed/ub_pm_summary.csv'
combined_file = '../data/combined/nyc_ub_pm_summary.csv'

# Ensure combined folder exists
os.makedirs(os.path.dirname(combined_file), exist_ok=True)

# Load summary CSVs
df_nyc = pd.read_csv(nyc_file)
df_ub = pd.read_csv(ub_file)

# Rename UB columns to distinguish from NYC
df_ub = df_ub.rename(columns={
    'Annual_mean': 'UB_Annual_mean',
    'Summer_mean': 'UB_Summer_mean',
    'Winter_mean': 'UB_Winter_mean'
})

# Merge by Year
df_combined = pd.merge(df_nyc, df_ub, on='Year', how='outer')

# Save combined CSV
df_combined.to_csv(combined_file, index=False)

print(f"✅ Combined NYC & UB PM summary saved: {combined_file}")
print(df_combined)
