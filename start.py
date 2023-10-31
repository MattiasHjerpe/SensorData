import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Load CSV file into data variable
data = pd.read_csv('data.csv')

# Plot the data
plt.figure(figsize=(10, 6))

# Z-score stored in variables
data_baro = stats.zscore(data['Baro'])
data_lidar = stats.zscore(data['Lidar'])
threshold = 1.5

# Remove outliers
dataNoOutliers = data[(abs(data_baro) < threshold) & (abs(data_lidar) < threshold)]

# Filter 'Baro' data after 3.5 seconds
dataNoOutliers_baro = dataNoOutliers[dataNoOutliers['Time'] <= 3.5]

# Plot 'Baro' and 'Lidar' data
plt.plot(dataNoOutliers_baro['Time'], dataNoOutliers_baro['Baro'], label='Baro')
plt.plot(dataNoOutliers['Time'], dataNoOutliers['Lidar'], label='Lidar')

plt.xlabel('Time(sec)')
plt.ylabel('Altitude(m)')
plt.title('Sensor Data')
plt.legend()
plt.grid(True)
plt.show()


