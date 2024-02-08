/* This example shows how to use continuous mode to take
range measurements with the VL53L0X. It is based on
vl53l0x_ContinuousRanging_Example.c from the VL53L0X API.

The range readings are in units of mm. */

#include <Wire.h>
#include <VL53L0X.h>

VL53L0X sensor;

#define LED_GPIO 2
#define BUZ_GPIO 4
#define BUZ_CH 0


void setup()
{
  Serial.begin(9600);

  pinMode(LED_GPIO, OUTPUT);
  pinMode(BUZ_GPIO, OUTPUT);
  ledcAttachPin(BUZ_GPIO, BUZ_CH);


  Wire.begin();

  sensor.setTimeout(500);
  if (!sensor.init())
  {
    Serial.println("Failed to detect and initialize sensor!");
    while (1) {}
  }

  // Start continuous back-to-back mode (take readings as
  // fast as possible).  To use continuous timed mode
  // instead, provide a desired inter-measurement period in
  // ms (e.g. sensor.startContinuous(100)).
  sensor.startContinuous();
}

void loop()
{
  int distance = sensor.readRangeContinuousMillimeters();

  if (distance < 80){
      digitalWrite(LED_GPIO, 1);
      digitalWrite(BUZ_GPIO, 1);
    ledcAttachPin(BUZ_GPIO, BUZ_CH);

  }
  else {
      digitalWrite(LED_GPIO, 0);
      digitalWrite(BUZ_GPIO, 0);
      ledcDetachPin(BUZ_GPIO);
  }

  ledcWriteTone(BUZ_CH, 1000);
  Serial.print(distance);
  if (sensor.timeoutOccurred()) { Serial.print(" TIMEOUT"); }

  Serial.println();
}
