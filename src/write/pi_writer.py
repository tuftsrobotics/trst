"""
pi_writer.py

Written by Alex Tong September 2015

This program writes to an arduino over a serial port intending to control two
servo motors

Note:
    Currently REALLY annoying as you have to hit enter after every key input

"""

#import serial
#
#
#ser = serial.Serial('/dev/ttyACM0', 115200)

class BoatState(object):
    SERVO_LOW = 0
    SERVO_HIGH = 255
    SERVO_START = (SERVO_HIGH - SERVO_LOW) / 2
    INCREMENT = 5
    def __init__(self):
        self.rudder_pos = self.SERVO_START
        self.sails_pos = self.SERVO_START

    def turn_right(self, n = 5):
        self.set_rudder_pos(self.rudder_pos + n)

    def turn_left(self, n = 5):
        self.set_rudder_pos(self.rudder_pos - n)

    def adjust_sails(self, n):
        self.set_sails_pos(self.sails_pos + n)

    def set_rudder_pos(self, new_pos):
        if new_pos >= self.SERVO_LOW and new_pos < self.SERVO_HIGH:
            self.rudder_pos = new_pos

    def set_sails_pos(self, new_pos):
        if new_pos >= self.SERVO_LOW and new_pos < self.SERVO_HIGH:
            self.sails_pos = new_pos

    def set_pos(self, new_pos):
        assert type(new_pos) == tuple
        assert len(new_pos) == 2
        self.set_rudder_pos(new_pos[0])
        self.set_sails_pos(new_pos[1])

    def get_pos(self):
        return self.rudder_pos, self.sails_pos

    def __repr__(self):
        return "<BoatState Obj: " + str(id(self)) + " rudder: " + str(self.rudder_pos) + " sails: " + str(self.sails_pos) + ">"

def control(key, state):
    """ controls the servo positions given a keyboard input
    Takes wasd input from the keyboard and uses it to control two servos. 
    The rudder servo is controlled by ad, sails by ws

    Args:
        key (str): key entered on stdin
        state: boatstate of t-1 timestep
    
    Returns:
        A new boatstate object
    """
    INCREMENT = 5
    
    if key == 'a':
        state.turn_left()
    elif key == 'd':
        state.turn_right()
    elif key == 's':
        state.adjust_sails(-5)
    elif key == 'w':
        state.adjust_sails(+5)
    else:
        print "invalid key"
    return state

def main():
    state = BoatState()
    try:
        while 1:
            key = raw_input()
            state = control(key, state)
            print state
    except KeyboardInterrupt:
        print "\nINTERUPT PROGRAM HALT"

if __name__ == '__main__':
    main()
