import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Load CSV file into data variable
data = pd.read_csv('data.csv')

# Plot the data
plt.figure(figsize=(10, 6))

data_baro = stats.zscore(data['Baro'])
data_lidar = stats.zscore(data['Lidar'])
threshold = 3

dataNoOutliers = data[(abs(data_baro) < threshold) & (abs(data_lidar) < threshold)]

# Attempt to plot data (assuming column names are correct)
plt.plot(dataNoOutliers['Time'], dataNoOutliers['Baro'], label='Baro')
plt.plot(dataNoOutliers['Time'], dataNoOutliers['Lidar'], label='Lidar')

plt.xlabel('Time(sec)')
plt.ylabel('Altitude(m)')
plt.title('Sensor Data')
plt.legend()
plt.grid(True)
plt.show()


