//Servo Testing Suite for Sailboat Sails

#include <Servo.h>

Servo sails;
//Servo rudder;

int angle;
String input;

void setup() {
  sails.attach(9);
//  rudder.attach(10);
  Serial.begin(9600);
}

void loop() {

  while (Serial.available() > 0) {
    int inChar = Serial.read();
    if (isDigit(inChar)) {
      // convert the incoming byte to a char
      // and add it to the string:
      input += (char)inChar;
    }
    // if you get a newline, print the string,
    // then the string's value:
    if (inChar == '\n') {
      Serial.print("Value: ");
      angle = input.toInt();
      Serial.println(angle);
      sails.writeMicroseconds(angle);
      
      input = "";
    }
  }

//  sails.write(0);
//  Serial.print("0");
//  Serial.print("\n");
//  delay(1000);
//  sails.write(180);
//  Serial.print("1800");
//  Serial.print("\n");
//  delay(1000);
//  sails.write(255);
//  Serial.print("255");
//  Serial.print("\n");
//  delay(1000);
//  sails.write(180);
//  Serial.print("180");
//  Serial.print("\n");
//  delay(1000);

}
