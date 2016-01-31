"""
pyserial_driver.py

Written by Alex Tong September 2015

This program writes to a serial port in a specified format to control two servos
it also defines that format
"""

import serial
from boatstate import BoatState
import time

DEBUG = False

def format_to_arduino(state):
    """ Defines the format passed to the arduino

    Each serial line has the format:
        [rudder_pos],[sails_pos]
    
    Each position being an integer number of miliseconds in PWM format.
    """
    rudder, sails = state.get_pos()
    return str(rudder) + ',' + str(sails) + '\n'

class SerialConnection(object):
    """ Serial Connection object used to connect to arduino over usb serial

    Serial connection has a number of option, logging will log all messages sent
    over serial to the arduino, very useful for debugging. Log files will either 
    be time stamped or numbered ordinally.

    """
    def __init__(self, port = '/dev/ttyACM0', baudrate = 115200, log = True,  logfilenum = None):
        if logfilenum is None:
            self.log_file = open('log/driver/' + str(int(time.time())) + '.log', 'a+')
        else:
            self.log_file = open('log/driver/' + str(logfilenum) + '.log', 'a+')
        self.default_state = BoatState()
        self.ser = serial.Serial(port, baudrate)
        self.last_state_written = self.default_state
        self.log = log
    def write(self, state = None):
        if state == None:
            state = self.default_state
        assert type(state) == BoatState
        string = format_to_arduino(state).encode()
        if DEBUG:
            print "STATE:", state
            print "SENT:", string
        self.ser.write(string)
        if self.log:
            print >> self.log_file, string

