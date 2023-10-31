import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file into data variable
data = pd.read_csv('data.csv')

# Plot the data
plt.figure(figsize=(10, 6))

# Attempt to plot data (assuming column names are correct)
plt.plot(data['Time'], data['Baro'], label='Baro')
plt.plot(data['Time'], data['Lidar'], label='Lidar')

plt.xlabel('Time(sec)')
plt.ylabel('Altitude(m)')
plt.title('Sensor Data')
plt.legend()
plt.grid(True)
plt.show()


