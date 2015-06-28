#!/usr/bin/python
#decoder.py
#Created by Alex Tong 25 May 2015
#This program reads data from the serial port, outputs it on stdout, and
#  uses the canboat project analyzer to decode it into meaningful data,
#  which is then stored and used in further modules

import serial
from time import strftime
from dattime import datetime, time

PORT = '/dev/ttyACM0'
BAUD = 115200

ser = serial.Serial(PORT, BAUD)
try:
    while 1:
        line = ser.readline().rstrip()
        print(line)
########## PROCESS LINE
except KeyboardInterrupt:
    print >> stderr, (
"-------------------------------------------------------------------------------\n"
"INTERUPT PROGRAM HALT\n"
"-------------------------------------------------------------------------------")
