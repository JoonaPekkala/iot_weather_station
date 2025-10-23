# Needed libraries
import os
import serial
import time
import csv
from datetime import datetime

# Read the DHT22 sensor data from ESP32
def read_from_serial():
    try:
        ser = serial.Serial(port = "COM4", baudrate = 9600, timeout = 2)    # Open serial port
        line = ser.readline().decode("utf-8").strip()
        ser.close()
        if line:
            temp, hum = map(float, line.split(","))
            return temp, hum
        
    except Exception as e:
        print(f"Serial read error: {e}")

    return None, None

# Write the data to csv file and print to terminal
def write_to_csv(filename = "data.csv", duration = 28800, interval = 60):     # Duration for total logging in seconds and interval between measurement in seconds (8hours for every 1 minute)
    file_exists = os.path.exists(filename)                                    # Check if CSV already exists

    with open(filename, "a", newline = "") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["timestamp", "temp_C", "hum_%"])           # Create the first line in csv if the file has not been created yet
        print("Timestamp: Temp (C), Hum (%)")                           # Terminal print
        start_time = time.time()

        try:
            while time.time() - start_time < duration:                  # While loop to measure data for a wanted time
                timestamp = datetime.now().isoformat()                  # Timestamp for data
                temp, hum = read_from_serial()
                writer.writerow([timestamp, temp, hum])
                print(f"{timestamp}: Temperature: {temp} C, Humidity: {hum} %")     # Terminal print
                time.sleep(interval)
        except KeyboardInterrupt:                                                   # Handle user interruption
            print("\nData logging stopped by user.")

        print(f"\nData logging complete. Data can be found at {filename}.")

if __name__ == "__main__":
    write_to_csv()
