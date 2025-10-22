import matplotlib

def read_from_csv(filename = "data.csv"):
    with open(filename) as file:
        for line in file:
            timestamp, temp, hum = line.rstrip().split(",")
            print(f"{timestamp} Temperature: {temp}°C, Humidity: {hum}%")

read_from_csv()
