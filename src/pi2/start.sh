#/bin/bash

#Start.sh
#Start script for the trst project.
#   0. (optional) start server
#   1. set waypoints with a waypoint csv/gpx file
#   2. start sensor upload on first arduino
#   3. start navigator on second arduino

i=0 #i = run number
while [[ -e log/run/$i.log ]] ; do
    let i++
done
f=log/run/$i.log
touch $f
echo "Starting run $i" > $f

#sensor_port=/dev/tty.usbModem1411
#nav_port=/dev/tty.usbModem1421
sensor_port=/dev/ttyACM0
nav_port=/dev/ttyACM1
waypoints=waypoints/test

### START SERVER ###
#removed for ease of control
#python server.py &

### STAT WAYPOINT SETTER ###
python set_waypoint.py $waypoints -g


### START UPLOADER ###
python uploader.py -t $i -p $sensor_port


### START NAVIGATOR ###
python navigator.py -t $i -p $nav_port
