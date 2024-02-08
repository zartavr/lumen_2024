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

#define HIGH_SPEED

void setup()
{
  Serial.begin(115200);

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

#if defined HIGH_SPEED
  // reduce timing budget to 20 ms (default is about 33 ms)
  sensor.setMeasurementTimingBudget(20000);
#elif defined HIGH_ACCURACY
  // increase timing budget to 200 ms
  sensor.setMeasurementTimingBudget(200000);
#endif
}

void loop()
{
  int distance = sensor.readRangeSingleMillimeters();

  if (distance < 100){
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
  if (!sensor.timeoutOccurred()) {
    Serial.println(distance);
  }
  delay(200);
}
