#include <Servo.h>

//Data is sent to the arduino as a string rudder_pos,sail_pos
// rudder_pos should be 1100-1800 and sail_pos should be 1100-1800


Servo sails;
Servo rudder;

int rudder_default = 1300;
int sail_default = 1800;

int RC_sail_port = 5;
int RC_rudder_port = 6;

int AR_sail_port = 9;
int AR_rudder_port = 10;

int RC_pulse_timeout = 100000;

int upper_bound = 1800;
int lower_bound = 1100;

bool RC_state = false;



void setRudder(int pos) {
  if (pos >= lower_bound && pos <= upper_bound) {
      rudder.writeMicroseconds(pos);
  } else {
    Serial.print("error: Rudder out of bounds!\n");
  }
}

void setSails(int pos) {
  if (pos >= lower_bound && pos <= upper_bound) {
    sails.writeMicroseconds(pos);    
  } else {
    Serial.print("error: Sails out of bounds!\n");
  }
}

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(10);
  sails.attach(AR_sail_port);
  rudder.attach(AR_rudder_port);

  // rudder and sail defaults
  rudder.writeMicroseconds(rudder_default);
  sails.writeMicroseconds(sail_default);
  Serial.print("ready\n");
}

void loop() {
  int rudder_pos;
  int sail_pos;
  while (Serial.available() > 0 && !RC_state) {
    rudder_pos = Serial.parseInt();
    sail_pos = Serial.parseInt();
    if (Serial.read() == '\n') {
      
      setRudder(rudder_pos);
      setSails(sail_pos);
      Serial.print('r');
      Serial.print(rudder_pos);
      Serial.print('s');
      Serial.print(sail_pos);
      Serial.print('\n');
    }
  }
  int RC_sails = pulseIn(RC_sail_port, HIGH, RC_pulse_timeout);
  int RC_rudder = pulseIn(RC_rudder_port, HIGH, RC_pulse_timeout);

  if (RC_sails != 0 || RC_rudder != 0) {
      // RC override
      RC_state = true;
      
      setSails(RC_sails);
      setRudder(RC_rudder);

      Serial.print("RC_rudder: ");
      Serial.print(RC_rudder);
      Serial.print("\nRC_sails: ");
      Serial.print(RC_sails);
      Serial.print('\n');
    } else {
      RC_state = false;
    }
    delay(10);
}
