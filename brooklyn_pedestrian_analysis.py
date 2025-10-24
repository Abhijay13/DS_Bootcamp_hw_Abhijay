# Brooklyn Bridge Pedestrian Activity Analysis
# ---------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("brooklyn_pedestrian.csv")

# ---------------------------------------------------------------
# 1️⃣ Filter to weekdays (Monday–Friday) and plot pedestrian counts by day
# ---------------------------------------------------------------

# Convert date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Create weekday column
df['Weekday'] = df['Date'].dt.day_name()

# Filter only Monday–Friday
weekdays_df = df[df['Date'].dt.weekday < 5]

# Group by weekday and sum pedestrian counts
weekday_counts = weekdays_df.groupby('Weekday')['Pedestrians'].sum().reindex(
    ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
)

# Plot line graph
plt.figure(figsize=(8, 4))
plt.plot(weekday_counts.index, weekday_counts.values, marker='o', linewidth=2)
plt.title("Brooklyn Bridge Pedestrian Counts by Weekday")
plt.xlabel("Weekday")
plt.ylabel("Total Pedestrian Count")
plt.grid(True)
plt.show()

# ---------------------------------------------------------------
# 2️⃣ Analyze 2019 pedestrian counts by weather
# ---------------------------------------------------------------

# Filter only 2019 data
df_2019 = df[df['Date'].dt.year == 2019]

# Group by weather summary and calculate mean pedestrian count
weather_analysis = df_2019.groupby('Weather_Summary')['Pedestrians'].mean().sort_values(ascending=False)
print("\nAverage Pedestrian Count by Weather Condition (2019):")
print(weather_analysis)

# Correlation matrix for weather-related variables
weather_corr = df_2019[['Pedestrians', 'Temperature', 'Humidity', 'Precipitation']].corr()

plt.figure(figsize=(6, 4))
sns.heatmap(weather_corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Matrix: Weather vs Pedestrian Count (2019)")
plt.show()

# ---------------------------------------------------------------
# 3️⃣ Categorize time of day and analyze activity patterns
# ---------------------------------------------------------------

# Convert timestamp column to datetime (if exists)
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# Define a function for time-of-day categories
def categorize_time_of_day(hour):
    if 5 <= hour < 12:
        return 'Morning'
    elif 12 <= hour < 17:
        return 'Afternoon'
    elif 17 <= hour < 21:
        return 'Evening'
    else:
        return 'Night'

# Create new column
df['Time_of_Day'] = df['Timestamp'].dt.hour.apply(categorize_time_of_day)

# Group by time of day and calculate mean pedestrian count
tod_counts = df.groupby('Time_of_Day')['Pedestrians'].mean().reindex(
    ['Morning', 'Afternoon', 'Evening', 'Night']
)

# Plot activity by time of day
plt.figure(figsize=(7, 4))
tod_counts.plot(kind='bar', color='skyblue')
plt.title("Average Pedestrian Activity by Time of Day")
plt.xlabel("Time of Day")
plt.ylabel("Average Pedestrian Count")
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
