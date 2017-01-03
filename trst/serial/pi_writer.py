"""
pi_writer.py

Written by Alex Tong September 2015

This program writes to an arduino over a serial port intending to control two
servo motors

Note:
    Currently REALLY annoying as you have to hit enter after every key input

"""

from trst.serial.pyserial_driver import *
from trst.navigation.boatstate import BoatState

def control(key, state):
    """ controls the servo positions given a keyboard input
    Takes wasd input from the keyboard and uses it to control two servos.
    The rudder servo is controlled by ad, sails by ws

    Args:
        key (str): key entered on stdin
        state: boatstate of t-1 timestep

    Returns:
        updated boatstate
    """
    INCREMENT = 100

    if key == 'a':
        state.turn_left()
    elif key == 'd':
        state.turn_right()
    elif key == 's':
        state.adjust_sails(-INCREMENT)
    elif key == 'w':
        state.adjust_sails(+INCREMENT)
    else:
        print "invalid key"
    return state

def transmit_serial(state, connection):
    """ transmits boat state over a connection object

    calls connection.write(state) to write the state over some connection

    """
    connection.write(state)

def main():
    state = BoatState()
    connection = SerialConnection()
    try:
        while 1:
            key = raw_input()
            state = control(key, state)
            print state
            transmit_serial(state, connection)
    except KeyboardInterrupt:
        print "\nINTERUPT PROGRAM HALT"

if __name__ == '__main__':
    main()
