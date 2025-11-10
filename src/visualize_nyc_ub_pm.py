import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load dataset
df = pd.read_csv('../data/combined/nyc_ub_pm_summary.csv')

sns.set(style="whitegrid", font_scale=1.1)
fig, axes = plt.subplots(3, 1, figsize=(10, 16))

# --- 1️⃣ Annual PM Trend ---
axes[0].plot(df['Year'], df['Annual_mean'], marker='o', label='NYC Annual PM', color='blue')

# Add UB if available
if 'UB_Annual_mean' in df.columns:
    axes[0].plot(df['Year'], df['UB_Annual_mean'], marker='s', label='UB Annual PM', color='red')

axes[0].set_title('Annual PM Trend: NYC vs UB')
axes[0].set_xlabel('Year')
axes[0].set_ylabel('PM Level (µg/m³)')
axes[0].legend()
axes[0].grid(True)

# --- 2️⃣ Bar Plot: Seasonal Comparison ---
seasons, nyc_season, ub_season = [], [], []

if 'UB_Summer_mean' in df.columns and 'UB_Winter_mean' in df.columns:
    seasons = ['UB Summer', 'UB Winter']
    ub_season = [df['UB_Summer_mean'].mean(), df['UB_Winter_mean'].mean()]

# Only plot NYC if available
if 'NYC_Summer_mean' in df.columns and 'NYC_Winter_mean' in df.columns:
    seasons = ['NYC Summer', 'NYC Winter'] + seasons
    nyc_season = [df['NYC_Summer_mean'].mean(), df['NYC_Winter_mean'].mean()]

x = np.arange(len(seasons))
width = 0.35

# Combine bar values dynamically
bars = nyc_season + ub_season
axes[1].bar(x, bars, width, color='skyblue')
axes[1].set_title('Average Seasonal PM Levels')
axes[1].set_ylabel('PM Level (µg/m³)')
axes[1].set_xticks(x)
axes[1].set_xticklabels(seasons, rotation=20)

# --- 3️⃣ Heatmap: Seasonal PM by Year ---
heatmap_cols = [c for c in df.columns if 'mean' in c and c != 'Annual_mean']
if heatmap_cols:
    heatmap_data = df[['Year'] + heatmap_cols].set_index('Year')
    sns.heatmap(heatmap_data, annot=True, fmt=".1f", cmap="coolwarm", ax=axes[2])
    axes[2].set_title('Seasonal PM by Year')

# --- Layout ---
plt.tight_layout()
plt.savefig('../data/combined/nyc_ub_pm_visualization.png', dpi=300, bbox_inches='tight')
plt.show()

print("✅ Visualization saved as ../data/combined/nyc_ub_pm_visualization.png")
