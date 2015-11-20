#Navigator.py
#Created by Alex Tong 5 Jul 2015
#
#
#
"""
This module is a navigator given a series of waypoints on a server

"""


WAIT_TIME = 0.5

#initial_waypoint = {'Latitude': 42.432136, 'Longitude': -71.147794}
# about 100 meters off the dock

from LatLon import LatLon, Latitude, Longitude
import data
import pid
import time
from boatstate import BoatState
from pyserial_driver import SerialConnection
from argparse import ArgumentParser

def get_vect_to_wp(p):
    c = data.request()

def get_vect(p1, p2):
    """returns heading and magnitude between two latlon objects """
    assert type(p1) == type(LatLon)
    assert type(p2) == type(LatLon)
    return p2 - p1

def get_latlon_from_dict(d):
    assert 'Latitude' in d and 'Longitude' in d
    return LatLon(d['Latitude'], d['Longitude'])

def navigate(boat_data, waypoint):
    curr_pos = get_latlon_from_dict(boat_data)
    next_pos = get_latlon_from_dict(waypoint)
#TODO unhardcode deviation
    deviation = -14.8
    true_heading = float(boat_data['Heading']) + deviation
    if true_heading > 180: #correct to range [-180,180]
        true_heading = true_heading - 360
    #PID update
    pid_nav.target = float(curr_pos.heading_initial(next_pos)) #true angle to target
    rudder_target = pid_nav.update(true_heading)
    boat_state.set_rudder_scaled_pos(rudder_target)

#    serial.write(state = boat_state)

def pull_data():
    boat_data = data.get_request('').json()
    if boat_data == {}:
        print "NO BOAT DATA EXITING"
    return boat_data

def main():
    #data.post_request('waypoint', initial_waypoint)
    try:
        waypoints = data.get_request('waypoint').json()
        while 1:
            boat_data = pull_data()
            navigate(boat_data, waypoints["0"]) #note that dictionary keys are string
            time.sleep(WAIT_TIME)
    except KeyboardInterrupt:
        print "\nINTERUPT NAVIGATOR PROGRAM HALT"

if __name__ == '__main__':
#PARSE
    argparser = ArgumentParser()
    argparser.add_argument('-t', action = 'store', dest = 'run_number', help='run number used in logging')
    argparser.add_argument('-port', action = 'store', dest = 'port', default = '/dev/ttyACM1', help='port for navigator arduino')
    r = argparser.parse_args()
    log = (r.run_number is not None)

    pid_nav = pid.PID()
    boat_state = BoatState()
#serial     = SerialConnection(port = '/dev/ttyACM1')
#    serial     = SerialConnection(port = r.port, log=log, logfilenum = r.run_number)
    main()

