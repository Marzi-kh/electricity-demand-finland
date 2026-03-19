Finland Electricity Consumption Analysis
Overview:
This project analyzes electricity consumption in Finland using open data from Fingrid. 
The goal is to understand demand patterns over time and build a baseline forecasting model to support energy planning.
Data:
The dataset contains ~1 year of electricity consumption data at 15-minute intervals.
Approach:
Data cleaning and validation
Time-series structuring and feature engineering (hour, weekday, month)
Exploratory analysis of temporal patterns
Baseline forecasting using Random Forest
Time-series cross-validation for evaluation
Key Insights:
Strong seasonality: winter demand ~35% higher than summer
Clear daily pattern: higher during daytime, lower overnight
Weekend effect: demand decreases on weekends
Peak demand reaches ~1.4× average load
Demand is highly predictable based on time features
Model:
A Random Forest model was used as a baseline with time-based features only.
Average MAE ≈ 935 MWh (~10% of average demand) using time-series validation.
Why This Matters:
Supports energy production planning
Helps manage peak demand
Improves supply–demand balancing
Supports renewable energy integration
Next Steps:
Incorporate weather data (e.g., temperature)
Add lag features to capture temporal dependencies
Use advanced models (e.g., Gradient Boosting)
Develop real-time forecasting pipeline



## How to run the project

1. Install dependencies:
   pip install -r requirements.txt

2. Run the scripts in the following order:

   python SCR/data_preprocessing.py
   python SCR/consumption_eda.py
   python SCR/visualization.py
   python SCR/model.py
   python SCR/summary_table.py