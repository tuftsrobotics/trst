//Servo Testing Suite for Sailboat

#include <Servo.h>

// Servo sails;
Servo rudder;

int angle;

void setup() {
  // sails.attach(9);
  rudder.attach(10);
  Serial.begin(9600);
}

void loop() {
  for (int i = 0; i < 255; i = i + 30) {
    angle = i;
    rudder.write(angle);
    Serial.print(angle);
    Serial.print("\n");
    delay(2000);
    // rudder.write(angle);
    // delay(50);

  }

}
