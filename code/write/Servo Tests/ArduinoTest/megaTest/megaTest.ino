//Servo Testing Suite for Sailboat
//pins for the arduino mega 2560 used for testing purposes.

#include <Servo.h>

Servo sails;
Servo rudder;

int angle;

void setup() {
  sails.attach(1);
  rudder.attach(6);
  Serial.begin(9600);
}

void loop() {
  for (int i = 0; i < 180; i = i + 10) {
    angle = i;
    sails.write(angle);
    Serial.print(angle);
    Serial.print("\n");
    delay(50);
    rudder.write(angle);
    delay(50);

  }

}
