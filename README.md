# IoT Weather Station with ESP32 and DHT22

This project is a simple IoT weather station built using an **ESP32 microcontroller** and a **DHT22 temperature** and **humidity** sensor.  
The data is sent from the ESP32 to a connected computer over the serial port and logged using a **Python script**.

The Python application saves all measurements to a `.csv` file and visualizes the results using `matplotlib`.

---

## Features

- Reads **temperature** and **humidity** from DHT22  
- Sends data over **serial connection (UART)** to Python  
- Logs all data with **timestamps** to a CSV file  
- Visualizes temperature and humidity trends with a **plot**

---

## Hardware setup

| Component       | ESP32 Pin               | Description      |
|-----------------|-------------------------|------------------|
| DHT22 VCC       | 5V                      | Power            |
| DHT22 GND       | GND                     | Ground           |
| DHT22 DATA      | GPIO 14                 | Data line        |
| 10kohm resistor | between DATA and 5V     | Pull-up resistor |

---

## Software setup

### 1. Flash the ESP32
- Open the provided `.ino` file in **Arduino IDE**  
- Select your ESP32 board under **Tools -> Board -> ESP32 Dev Module**
- Select the correct COM port under **Tools -> Port**
- Upload the code

### 2. Install Python dependencies
In the `/python_app` folder, run:
```bash
pip install -r requirements.txt
```

### 3. Start logging data
Run:
```bash
python main.py
```
This will:
- Open serial port
- Read sensor data
- Save results to `data.csv`

### 4. Plot the results
After some data has been collected:
```bash
python plotter.py
```
This displays a temperatute and humidity graph over time.

---

## Learning goals
This project demonstrates
- Serial communication between ESP32 ja Python
- File handling and data logging
- Basic data visualization using matplotlib
- Hardware interfacing (sensor + microcontroller)

Small project for **embedded systems**, **IoT** and **Python data handling** practice.

---

## Requirements
- Python 3.10+
- Arduino IDE with ESP32 board support
- DHT22 sensor
- ESP32 development board

---

## Author
**Joona-Oskari Pekkala**

Oulu, Finland

---

## requirements.txt

```text
pyserial
matplotlib
```

---

## Example of the data

![Graph of Temperature and Humidity over Time](/graph.png)

---