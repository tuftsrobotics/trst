#!/bin/bash

#This script is used to setup python serial connection with arduino for a 
#raspberry pi running raspbian

#Created by Alex Tong February 20, 2015
echo "This script must be run with sudo"
echo "Running command: sudo apt-get install pyserial"
apt-get install pyserial

echo "next find the arduino serial port with the command: ls /dev/tty*"
echo "checking for changes between inserting the arduino through usb"

