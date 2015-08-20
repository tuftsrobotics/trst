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

#ser = serial.Serial('/dev/ttyACM0', 115200)

startTime = datetime.now()

class Analyzer():
    def __init__(self):
        self.attitude = {"SID" : 0, "yaw" : 0}
        self.cog_sog_rapid_update = {}
        self.GNSS_position_data = {}
        self.position_rapid_update = {}
        self.system_time = {}
        self.vessel_heading = {}
        self.wind_data = {}
        # id numbers for specific set of data mapped to function calls
        self.ids = { "1F119" : SET_attitude, 
                     "1F802" : SET_cog_sog_rapid_update,
                     "1F805" : SET_GNSS_position_data, 
                     "1F801" : SET_position_rapid_update,
                     "1F010" : SET_system_time, 
                     "1F112" : SET_vessel_heading, 
                     "1FD02" : SET_wind_data }
    '''
     def SET_attitude():
         SID = 
         yaw = 
         pitch = 
         roll = 

    def SET_cog_sog_rapid_update():
         SID = 
         cog_reference = 
         cog = 
         sog = 

     def SET_GNSS_position_data():
         SID = 
         position_date = 
         position_time = 
         latitude = 
         longitude = 
         type_of_system = 
         GNSS_method = 
         integrity = 
         num_SVs = 
         HDOP = 
         PDOP = 
         geoidal_separation = 
         num_reference_stations = 
         reference_station_type = 
         reference_station_id = 
         age_of_DGNSS_connection = 

     def SET_position_rapid_update():
         latitude = 
         longitude = 

     def SET_system_time():
         SID = 
         source = 
         date = 
         time = 

     def SET_vessel_heading():
         SID = 
         heading_sensor_reading = 
         deviation = 
         variation = 
         heading_sensor_reference = 

     def SET_wind_data():
         SID = 
         wind_speed = 
         wind_direction = 
         wind_reference = 
    '''

## analyze():
# decodes data into acceptable format
'''
def run_serial():
    analyzer = Analyzer()
    while 1:
        # line is a string read from the serial port, rstrip() removes
        # trailing white spaces on the line.
        # line=ser.readline()
        line = ser.readline().rstrip()


        # parses line into the data_id and the data itself
    	data_id, data = line.partition(' ')[::2]
        data = int(data)

        analyzer.ids[data_id](data)
'''

"""
gets the bytes of a 64 bit integer in big endian format
"""
def get_bytes(data_str, width):
    data_int = int(data_str)
    return [(data_int >> (8*i)) & 0xff for i in range(width-1, -1, -1)]

def run():
    analyzer = Analyzer()
    while 1:
        # parses line into the data_id and the data itself
    	pgn, data_str = line.partition(' ')[:2]
        data = get_bytes(data_str, 8)
        analyzer.ids[data_id](data)


if __name__ == "__main__":
    run()
