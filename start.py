import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Load CSV file into data variable
data = pd.read_csv('data.csv')

# Z-score stored in variables
data_baro = stats.zscore(data['Baro'])
data_lidar = stats.zscore(data['Lidar'])
threshold = 1.5

# Remove outliers
data_no_outliers = data[(abs(data_baro) < threshold) & (abs(data_lidar) < threshold)]

# Filter 'Baro' data after 3.5 seconds
data_no_outliers_baro = data_no_outliers[data_no_outliers['Time'] <= 3.5]

# Plot 'Baro' and 'Lidar' data
plt.figure(figsize=(10, 6))

# Combine 'Baro' and 'Lidar' data after removing outliers
plt.plot(data_no_outliers_baro['Time'], data_no_outliers_baro['Baro'], label='Baro')
plt.plot(data_no_outliers['Time'], data_no_outliers['Lidar'], label='Lidar')

# Plot the average data
combined_average = (data_no_outliers_baro['Baro'] + data_no_outliers['Lidar']) / 2
combined_average[data_no_outliers['Time'] > 3.5] = data_no_outliers['Lidar'][data_no_outliers['Time'] > 3.5]
plt.plot(data_no_outliers['Time'], combined_average, label='Average')

# Display the graph
plt.xlabel('Time(sec)')
plt.ylabel('Altitude(m)')
plt.title('Sensor Data')
plt.legend()
plt.grid(True)
plt.show()


