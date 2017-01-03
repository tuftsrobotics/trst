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

read -p "Start python server [Y/N]? " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]
then
    python server.py &
fi

### STAT WAYPOINT SETTER ###

read -p "Set Waypoints to default [Y/N]? " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]
then
    python set_waypoint.py $waypoints -g
fi


### START UPLOADER ###
read -p "Start uploader [Y/N]? " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]
then
    python old_uploader.py -t $i -p $sensor_port
    #this should be python decoder.py | analyzer -json | python uploader.py
fi

### START NAVIGATOR ###
read -p "Start navigator [Y/N]? " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]
then
    python navigator.py -t $i -p $nav_port
fi
