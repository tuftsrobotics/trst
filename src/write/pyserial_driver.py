"""
pyserial_driver.py

Written by Alex Tong September 2015

This program writes to a serial port in a specified format to control two servos
it also defines that format
"""

import serial
from boatstate import BoatState

def format_to_arduino(state):
    rudder, sails = state.get_pos
    return "R " + str(rudder) + "\n" + \
           "S " + str(sails)

class SerialConnection(object):
    def __init__(self, port = '/dev/ttyACM0', baudrate = 115200)
        self.default_state = BoatState()
        self.ser = serial.Serial(port, baudrate)
        self.last_state_written = self.default_state

    def write(self, state = None):
        if state == None:
            state = self.default_state
        assert type(state) == BoatState
        




