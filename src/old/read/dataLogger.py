#!/usr/bin/python

'''
Written by Alex Tong Jan 2015
Adapted from Ben Kenney's blog www.benk.ca
This program reads data from the serial port to a data file.

Input data will be copied line by line from the serial port.
Arduino must be connected on the port specified as the serial port.
'''

import serial
import time

ser = serial.Serial('/dev/ttyACM0', 115200)



def main(track_time = False):
    try:
        while 1:
            #line is a string read from the serial port, rstrip() removes
            #trailing white spaces on the line.
            #line=ser.readline()
            line=ser.readline().rstrip()
            if track_time:
                line = time.clock() + " " + line
            print(line)
            f=open('tempLog.dat','a')
            print >> f,line
            f.close()
    except KeyboardInterrupt:
        print "\nINTERUPT PROGRAM HALT"


if __name__ == '__main__':
    main()
