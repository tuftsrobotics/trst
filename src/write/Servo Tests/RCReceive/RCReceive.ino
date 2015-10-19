#include <Servo.h>

const int chA = 6;
const int chB = 5;
const int chC = 3;

int ch1;
Servo servo;

void setup() {
  servo.attach(9);
  Serial.begin(115200);
  pinMode(chA, INPUT);
  pinMode(chB, INPUT);
  pinMode(chC, INPUT);
}

void loop() {
  ch1 = pulseIn(chC, HIGH);
  Serial.print("Ch1:");
  Serial.print(ch1);
  servo.writeMicroseconds(ch1);
  Serial.print("\n");
  
}
