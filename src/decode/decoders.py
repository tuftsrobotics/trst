""" Holds a set of pgn specific NMEA 2000 decoders

Each function takes a line of data (int64) and returns a dictionary with useful 
data pertaining to that pgn. Since each pgn stores different data, the dictionary
keys are pgn specific.

"""


def attitude(data):
    """ PGN 1F119 """
    pass

def position_rapid_update(data):
    """ PGN 1F801 """
    pass

def cog_sog_rapid_update(data):
    """ PGN 1F802 """
    pass

def gnss_position(data):
    """ PGN 1F805 """
    pass

def sys_time(data):
    """ PGN 1F010 """
    pass

def vessel_heading(data):
    """ PGN 1F112 """
    pass

def wind(data):
    """ PGN 1FD02 """
    pass

