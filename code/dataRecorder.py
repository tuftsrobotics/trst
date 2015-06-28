#!/usr/bin/python

'''
Written by Alex Tong May 2015
This program reads data from the serial port and stores each line in a python list

Input data will be copied line by line from the serial port.
Arduino must be connected on the port specified as the serial port.
'''

import serial
ser = serial.Serial('/dev/ttyACM0', 115200)

    line=ser.readline().rstrip()
    print(line)
