# Import libraries
import matplotlib.pyplot as plt
import csv
from datetime import datetime

# Read the data in .csv file
def read_from_csv(filename = "data.csv"):
    timestamps, temps, hums = [], [], []    # Create empty lists for the data

    with open(filename) as file:
        reader = csv.reader(file)
        next(reader)                    # Skip header line
        for row in reader:
            if len(row) < 3:            # Skip empty or imcomplete rows
                continue
            timestamp, temp, hum = row
            try:
                timestamps.append(datetime.fromisoformat(timestamp))    # Append in lists
                temps.append(float(temp))
                hums.append(float(hum))
            except ValueError:                      # Skip malformed lines if any
                continue

    return timestamps, temps, hums


# Plot the data using matplotlib
def plot_data(filename = "data.csv"):
    timestamps, temps, hums = read_from_csv(filename)

    plt.figure(figsize=(10, 5))
    plt.plot(timestamps, temps, label="Temperature (°C)", linewidth=1.5)
    plt.plot(timestamps, hums, label="Humidity (%)", linewidth=1.5)
    plt.xlabel("Time")
    plt.ylabel("Value")
    plt.title("Temperature and Humidity over Time")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.gcf().autofmt_xdate()                   # Tilt timestamp labels for readability
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_data()
