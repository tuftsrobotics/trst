Tufts Robotic Sail Team Code Base
===

This code base describes the development of a code stack to run a
semi-autonomous sailboat with the intent of eventual trans-oceanic
autonomous operation. 

The Team
---
Alex Tong    
http://linkedin.com/in/atong01

Kabir Singh


Morgan Gellert


Modules
---

### Sensor parsing

Responsible for parsing data from the Airmar WX200 maring weather station from
the NMEA 2000 standard to a CSV (comma separated value) datafile.  

Input:       
NMEA 2000 PGN data over arduino serial input (usb port)

Output:     
CSV formatted raw airmar data 

### Navigator

Responsible for high level navigation plotting recommended course direction 
using current and forcast wind strength/direction and relevent polars.

Input:   
Current and Past GPS data
Optimal Course Direction History
Wind Strength and Direction History

Output:   
Optimal Course Direction (given in degrees from true north)

### Sailor

Responsible for sail and rudder control given optimal course direction,
using PID controller principles

Input:    
Optimal Course Direction (relative to true north)

Output:     
Sail angle (0-90 from centerline)
Rudder angle (-90 to 90 positive direction attempts right turn)

### Controller

Arduino C code responsible for arduino control of sail and rudder servos

Input:
Sail angle (format above)
Rudder angle (format above)

Output:    
PWM signals to servos (pulse width modulation)

###############################################################################
END OF FILE
###############################################################################