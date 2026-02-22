Finland Electricity Consumption Analysis

Overview:
In this project, I explored electricity consumption in Finland using open data from Fingrid. The goal was to understand how electricity demand changes over time and what patterns can be observed across hours, days, and seasons.
This kind of analysis is important for energy system planning, especially when thinking about renewable energy and the transition to a more sustainable system.
Data:
The data comes from Fingrid’s open data platform and includes electricity consumption measured every 15 minutes. I worked with roughly one year of data to capture seasonal effects.

I followed a simple but structured workflow:
Cleaned the data and converted timestamps into a usable format
Organized the data as a time series
Created basic time-related features like hour, weekday, and month
Grouped the data to understand patterns
Built a few simple visualizations to highlight trends
Key findings
A few things stood out clearly:
Electricity consumption is much higher in winter than in summer. This is likely due to heating demand.
February had the highest average consumption, while summer months like July were the lowest.
There is a clear daily pattern, with higher consumption during daytime hours.
Demand tends to be lower on weekends compared to weekdays.
There are significant peaks and lows in the data, showing how variable electricity demand can be.
Simple forecasting model
I also built a very simple machine learning model (Random Forest) to predict electricity consumption using only time-based features (hour, weekday, month).
The model achieved a mean absolute error of about 1,356 MWh, which is roughly 13% of average consumption.
This shows that time alone explains a large part of electricity demand, although adding weather or temperature data would likely improve the model.
Why this matters
Understanding how electricity demand changes over time is important for:
planning energy systems
integrating renewable energy
managing peak demand
supporting decarbonization
This project is a small example of how data can be used to support decisions in the energy sector.



## How to run the project

1. Install dependencies:
   pip install -r requirements.txt

2. Run the scripts in the following order:

   python SCR/data_preprocessing.py
   python SCR/consumption_eda.py
   python SCR/visualization.py
   python SCR/model.py
   python SCR/summary_table.py