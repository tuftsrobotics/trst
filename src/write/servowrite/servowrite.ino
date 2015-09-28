#include <Servo.h>

//Data is sent to the arduino in 2 bytes, the  first 8 bits should be
//for the rudder (this number should be between 30 and 150 as to not hurt the servo)
//the second 8 bits are for the sails

int SAIL_MASK = 0;
int RUDD_MASK = 1;

int incomingByte = 0;
int incomingData = 0;

Servo sails;
Servo rudder;

void get_data(int data) {
  
}

void setup() {
  Serial.begin(115200);
  sails.attach(9);
  rudder.attach(10);
}

void loop() {
  if (Serial.available() > 0) {
    incomingByte = Serial.read();
    incomingData = incomingByte >> 1;
    if (incomingByte & 0x1) {
      rudder.write(incomingData);
    } else {
      sails.write(incomingData);
    }
    Serial.print("I recieved: ");
    Serial.println(incomingByte, DEC);
  }
}
