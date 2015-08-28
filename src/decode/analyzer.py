## analyzer.py
# creates a static class Analyzer which keeps the most recently updated 
# data from the wind sensor in an acceptable format
#
# Author: Michael Caughron
# Editor: Alex Tong
# Created: 2015-06-28
# Modified: 2015-8-17

#import serial
from time import strftime
from datetime import datetime, time
from decoders import *

#ser = serial.Serial('/dev/ttyACM0', 115200)

startTime = datetime.now()

def get_bytes(data_str, width):
    """ Gets the bytes of a 64 bit integer in big endian format
    """
    data_int = int(data_str)
    return [(data_int >> (8*i)) & 0xff for i in range(width-1, -1, -1)]

class Pgn(object):
    """ A data class for a single NMEA 2000 statement

    Holds data pertaining to a single NMEA 2000 datapoint. A new Pgn object is 
    initialized for every dataline in the log.

    Attributes:
        pgn (string) 
        body (int)
        data (dict)
    """
    VALID_PGNS = { "1F119" : attitude, 
                   "1F802" : cog_sog_rapid_update,
                   "1F805" : gnss_position, 
                   "1F801" : position_rapid_update,
                   "1F010" : sys_time, 
                   "1F112" : vessel_heading, 
                   "1FD02" : wind }

    def __init__(self, pgn, body):
        self.pgn  = pgn
        self.body = body
        self.data = self.handle_body(pgn, body)

    def handle_body(self, pgn, body):
        if self.validate(pgn, body):
            return VALID_PGNS[pgn](body)
        else:
            return None

    def validate(self, pgn, body):
#TODO
        return True

    def __getitem__(self, i):
        return self.data[i]

class Analyzer(object):
    """ A database for sensor information.

    This class holds sensor information pertaining to a robotic boat, decoding
    NMEA 2000 sentences into python readable dictionaries.
    """
    def __init__(self):
        self.recents  = []
        self.attitude = {"SID" : 0, "yaw" : 0}
        self.cog_sog_rapid_update = {}
        self.GNSS_position_data = {}
        self.position_rapid_update = {}
        self.system_time = {}
        self.vessel_heading = {}
        self.wind_data = {}
