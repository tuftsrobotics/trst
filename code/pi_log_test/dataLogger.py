#!/usr/bin/python

'''
Written by Alex Tong Jan 2015
Adapted from Ben Kenney's blog www.benk.ca
This program reads data from the serial port to a data file.

Input data will be copied line by line from the serial port.
Arduino must be connected on the port specified as the serial port.
'''

import serial
from time import strftime
from datetime import datetime, time

ser = serial.Serial('/dev/ttyACM0', 9600)

startTime = datetime.now()
try:
    while 1:
        #line is a string read from the serial port, rstrip() removes
        #trailing white spaces on the line.
        line=ser.readline().rstrip()
        print(line)
        f=open('tempLog.dat','a')
        print >> f,line
        f.close()
except KeyboardInterrupt:
    print "\nINTERUPT PROGRAM HALT"
