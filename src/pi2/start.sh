#/bin/bash

i=0 #i = run number
while [[ -e log/run/$i.log ]] ; do
    let i++
done
f=log/run/$i.log
touch f
echo "Starting run $i" > $f


#up_port=/dev/tty.usbModem1411
#nav_port=/dev/tty.usbModem1421
up_port=/dev/ttyACM0
nav_port=/dev/ttyACM1

### START SERVER ###
python server.py

### STAT WAYPOINT SETTER ###


### START UPLOADER ###
python uploader.py -t $i -p $up_port


### START NAVIGATOR ###
python navigator.py -t $i -p $nav_port
