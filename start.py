import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


# Display a menu
def print_average_sensor_data():
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

    # Set size of graph
    plt.figure(figsize=(10, 6))

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


def print_unedited_graph():
    # Load CSV file into data variable
    data = pd.read_csv('data.csv')

    # Plot the data and set the size of the graph
    plt.figure(figsize=(10, 6))
    plt.plot(data['Time'], data['Baro'], label='Baro')
    plt.plot(data['Time'], data['Lidar'], label='Lidar')

    # Display the graph
    plt.xlabel('Time(sec)')
    plt.ylabel('Altitude(m)')
    plt.title('Sensor Data')
    plt.legend()
    plt.grid(True)
    plt.show()


while True:
    print("Menu:")
    print("1. Print average sensor data")
    print("2. Show unedited graph with both sensors")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        print_average_sensor_data()
    elif choice == '2':
        print_unedited_graph()
    elif choice == '3':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
