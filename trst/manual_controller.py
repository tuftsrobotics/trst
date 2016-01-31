"""
manual.py

Intended for manual testing of the control system. Simple connection to an arduino
connected via tty port, and simple controls for setting the servos at specified
locations
"""
from argparse import ArgumentParser

from pyserial_driver import *
from boatstate import BoatState

def transmit_serial(state, connection):
    """ transmits boat state over a connection object

    calls connection.write(state) to write the state over some connection

    """
    connection.write(state)


def main(port, log, logfilenum):
    intro = """
            This program allows you to control a sailboat over serial.
            Default values for servos are around 1400 and range from around
            1100 to 1800 although this varies by model. Be careful with values
            outside this range (although they are allowed for testing purposes
            """
    print intro
    state = BoatState()
    connection = SerialConnection(port = port)
    try:
        while 1:
            rudder = int(input("Enter rudder position: "))
            sails  = int(input("Enter sails position: "))
            state.set_pos((rudder, sails))
            transmit_serial(state, connection)
            print state
    except KeyboardInterrupt:
        print "\nINTERUPT PROGRAM HALT"

if __name__ == "__main__":
    argparser = ArgumentParser(description = "Manual Servo Control")
    argparser.add_argument('-t', action = 'store', dest = 'run_number', help='run number used in logging')
    argparser.add_argument('-port', action = 'store', dest = 'port', default = '/dev/ttyACM0', help='port for uploader arduino')
    r = argparser.parse_args()
    log = (r.run_number is not None)
    main(port = r.port, log = log, logfilenum = r.run_number)
