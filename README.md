Tufts Robotic Sail Team Code Base
===

Created By Alex Tong January  27 2015    
Updated By Alex Tong February 15 2015

This code base describes the development of a code stack to run a
semi-autonomous sailboat with the intent of eventual trans-oceanic
autonomous operation. 

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

Responsible for sail and rudder control given optimal course direction. 

Input:    

Output:     
::