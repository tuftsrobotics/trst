#include <Servo.h>

//Data is sent to the arduino as a string rudder_pos,sail_pos
// rudder_pos should be 0-255 and sail_pos should be 1100-1800


Servo sails;
Servo rudder;


int readRudder() {
  String input;
  int angle
  while (Serial.available() > 0) {
    int inChar = Serial.read();
    if (isDigit(inChar)) {
      // convert the incoming byte to a char
      // and add it to the string:
      input += (char)inChar;
    }
    // if you get a comma, return the value
    if (inChar == ',') {
      angle = input.toInt();      
      return angle;
    }
  }
}

int readSail() {
  String input;
  int angle
  while (Serial.available() > 0) {
    int inChar = Serial.read();
    if (isDigit(inChar)) {
      // convert the incoming byte to a char
      // and add it to the string:
      input += (char)inChar;
    }
    // if you get a comma, return the value
    if (inChar == '\n') {
      angle = input.toInt();      
      return angle;
    }
  }
}


void setRudder(int pos) {
  if (pos >= 30 && pos <= 150) {
      rudder.write(pos);
  }
}

void setSails(int speed) {
  if (speed >= 1100 && speed <= 1800) {
    sails.writeMicroseconds(speed);    
  }
}

void setup() {
  Serial.begin(115200);
  sails.attach(9);
  rudder.attach(10);

  // rudder and sail defaults
  rudder.write(180);
  sails.writeMicroseconds(1800);
}

void loop() {
  int rudder_pos;
  int sail_pos;
  if (Serial.available() > 0) {
    rudder_pos = readRudder();
    sail_pos = readSail();
    setRudder(rudder_pos);
    setSails(sail_pos);
  }
}
