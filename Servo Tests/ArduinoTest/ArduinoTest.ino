//Servo Testing Suite for Sailboat

#include <Servo.h>

Servo myServo;

int angle;

void setup() {
  myServo.attach(9);
  Serial.begin(9600);
}

void loop() {
  for (int i = 0; i < 180; i = i + 10) {
    angle = i;
    myServo.write(angle);
    Serial.print(angle);
    Serial.print("\n");
    delay(100);
  }

}
