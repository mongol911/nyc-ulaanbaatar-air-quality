# NYC vs Mongolia Air Pollution Analysis

## Overview
This project compares fine particulate matter (PM) levels between **New York City (NYC)** and **Mongolian Capital City (UB)** using publicly available environmental monitoring data.  
The analysis includes annual trends, seasonal comparisons, and a heatmap of PM levels over multiple years.

## Research Question
How do PM2.5 concentrations in Ulaanbaatar and New York City compare, and what temporal patterns or drivers can be identified in each city?

## Folder Structure
- `data/` - contains raw, processed, and combined datasets
- `src/` - Python scripts for data retrieval, cleaning, and visualization
- `visuals/` - exported charts and plots
- `README.md` - project overview and documentation
- `LICENSE` - MIT license
- `.gitignore` - files/folders excluded from version control

## Visualization

### Comparative PM2.5 Analysis: NYC & Ulaanbaatar
![NYC-Ulaanbaatar PM2.5](visuals/nyc_ub_pm_visualization.png)

### Description of Plots
1. **Annual PM Trend:**  
   Displays average annual PM levels for NYC and UB. NYC is relatively stable, while UB shows more variation.

2. **Seasonal Comparison:**  
   Illustrates average summer and winter PM levels. UB experiences high winter pollution due to coal-based heating, while NYC is moderate year-round.

3. **Heatmap:**  
   Shows seasonal PM by year for both cities. Warmer colors indicate higher PM levels, highlighting UB's harsh winter pollution.

### Data Note
Some values (such as Ulaanbaatar's summer 2015 PM measurement) are missing (NaN) due to gaps in monitoring data.  
This reflects real-world challenges in environmental data collection and demonstrates the importance of data completeness.

## Insights
- UB's winter PM levels are significantly higher than NYC's due to geographic and infrastructure factors.  
- Seasonal and annual trends can inform AI-based pollution modeling or policy evaluation.

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/mongol911/nyc-mongolia-air-pollution.git
