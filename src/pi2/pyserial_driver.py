"""
pyserial_driver.py

Written by Alex Tong September 2015

This program writes to a serial port in a specified format to control two servos
it also defines that format
"""

import serial
from boatstate import BoatState
import time

def format_to_arduino(state):
    rudder, sails = state.get_pos()
    return str(rudder) + ',' + str(sails) + '\n'

class SerialConnection(object):
    def __init__(self, port = '/dev/ttyACM0', baudrate = 115200):
        t = time.time()
        self.log_file = open('log/driver/' + str(t) + '.log', 'a')
        self.default_state = BoatState()
        self.ser = serial.Serial(port, baudrate)
        self.last_state_written = self.default_state

    def write(self, state = None):
        print state
        if state == None:
            state = self.default_state
        assert type(state) == BoatState
        string = format_to_arduino(state).encode()
        print string
        self.ser.write(string)
        print >> self.log_file, string

