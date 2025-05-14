import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create a sample dataset
data = pd.DataFrame({
    'date': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-01', '2023-01-02', '2023-01-03', '2023-01-01', '2023-01-02', '2023-01-03']),
    'location': ['Kenya', 'USA', 'India', 'Kenya', 'USA', 'India', 'Kenya', 'USA', 'India'],
    'total_cases': [100, 500, 200, 110, 550, 220, 120, 600, 240],
    'total_deaths': [5, 25, 10, 6, 27, 11, 7, 29, 12],
    'total_vaccinations': [50, 250, 100, 55, 275, 110, 60, 300, 120]
})

# Exploratory Data Analysis (EDA)
# Plot total cases over time for selected countries
plt.figure(figsize=(10, 6))
sns.lineplot(x='date', y='total_cases', hue='location', data=data)
plt.title('Total Cases Over Time')
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('total_cases_over_time.png')

# Plot total deaths over time
plt.figure(figsize=(10, 6))
sns.lineplot(x='date', y='total_deaths', hue='location', data=data)
plt.title('Total Deaths Over Time')
plt.xlabel('Date')
plt.ylabel('Total Deaths')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('total_deaths_over_time.png')

# Visualizing Vaccination Progress
# Plot cumulative vaccinations over time for selected countries
plt.figure(figsize=(10, 6))
sns.lineplot(x='date', y='total_vaccinations', hue='location', data=data)
plt.title('Total Vaccinations Over Time')
plt.xlabel('Date')
plt.ylabel('Total Vaccinations')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('total_vaccinations_over_time.png')

print('Plots saved successfully!')
