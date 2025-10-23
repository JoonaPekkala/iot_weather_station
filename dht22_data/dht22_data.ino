#include "DHT.h"              // Include library

#define DHTPIN 14             // Define pin
#define DHTTYPE DHT22         // Define sensor

DHT dht(DHTPIN, DHTTYPE);     // Create sensor object

void setup() {
  Serial.begin(9600);         // Open serial
  dht.begin();                // Start the sensor
}

void loop() {
  float temp = dht.readTemperature(); // Read temperature
  float hum = dht.readHumidity();     // Read humidity

  if (isnan(temp) || isnan(hum)) {
    Serial.println("Error reading DHT22!");
    return;
  }

  Serial.print(temp);
  Serial.print(","); 
  Serial.println(hum);

  delay(1000);                        // Wait 1 seconds
}
