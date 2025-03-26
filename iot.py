#include &lt;LiquidCrystal.h&gt;

// Initialize the LCD, connected to pins: RS=7, E=8, D4=9, D5=10, D6=11, D7=12
LiquidCrystal lcd(7, 8, 9, 10, 11, 12);

// Pin Definitions
const int tempPin = A0; // Temperature sensor connected to A0
const int heartRatePin = A1; // Potentiometer simulating heart rate on A1
const int ledPin = 13; // LED connected to pin 13 (to indicate sending data)

void setup() {
pinMode(ledPin, OUTPUT); // Set LED pin as output
lcd.begin(16, 2); // Initialize the LCD
lcd.print(&quot;Smart Healthcare&quot;); // Display startup message
delay(2000); // Wait for 2 seconds
lcd.clear(); // Clear the LCD
Serial.begin(9600); // Initialize serial communication
}

void loop() {
// Read temperature sensor data
int tempValue = analogRead(tempPin); // Read the TMP36 sensor value
float voltage = tempValue * (5.0 / 1023.0); // Convert to voltage
float temperature = (voltage - 0.5) * 100; // Convert voltage to Celsius

// Simulate heart rate using potentiometer
int heartRateValue = analogRead(heartRatePin); // Read potentiometer value
int heartRate = map(heartRateValue, 0, 1023, 60, 100); // Map to 60-100 BPM

// Display data on the LCD

lcd.setCursor(0, 0); // Set cursor to first row
lcd.print(&quot;Temp: &quot;);
lcd.print(temperature, 1); // Display temperature with 1 decimal
lcd.print(&quot; C&quot;);

lcd.setCursor(0, 1); // Set cursor to second row
lcd.print(&quot;Heart: &quot;);
lcd.print(heartRate); // Display heart rate
lcd.print(&quot; BPM&quot;);

// Simulate sending data to the cloud (LED blink)
digitalWrite(ledPin, HIGH); // Turn on the LED
delay(500); // Keep LED on for 500ms
digitalWrite(ledPin, LOW); // Turn off the LED
delay(500); // Pause for 500ms before next cycle

// Print to Serial Monitor for debugging
Serial.print(&quot;Temperature: &quot;);
Serial.print(temperature);
Serial.print(&quot; C, Heart Rate: &quot;);
Serial.print(heartRate);
Serial.println(&quot; BPM&quot;);

delay(1000); // Wait 1 second before the next loop iteration
}
