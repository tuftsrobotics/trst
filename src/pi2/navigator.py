#Navigator.py
#Created by Alex Tong 5 Jul 2015
#
#
#

initial_waypoint = {'Latitude': 42.432136, 'Longitude': -71.147794}
# about 100 meters off the dock

from LatLon import LatLon, Latitude, Longitude
import data
import pid
import time
from boatstate import BoatState
from pyserial_driver import SerialConnection
from argparse import ArgumentParser


def get_vect_to_wp(p):
    c = data.request('gps')
    print c.json()

def get_vect(p1, p2):
    """returns heading and magnitude between two latlon objects """
    assert type(p1) == type(LatLon)
    assert type(p2) == type(LatLon)
    return p2 - p1


def navigate(boat_data, waypoint):
    current_pos = LatLon(Latitude(boat_data['Latitude']), Longitude(boat_data['Longitude']))
#remove for waypoint goodness TODO
    waypoint = initial_waypoint
    next_pos = LatLon(Latitude(waypoint['Latitude']), Longitude(waypoint['Longitude']))
#PID update
    pid_nav.target = float(current_pos.heading_initial(next_pos))
    heading = float(boat_data['Heading'])
    if heading > 180:
        heading = heading - 360
    boat_state.set_rudder_scaled_pos(pid_nav.update(heading))
    serial.write(state = boat_state)

def main():
    data.post_request('waypoint', initial_waypoint)
    try:
        while 1:
            waypoint = data.get_request('waypoint').text
            boat_data = data.get_request('').json()
            navigate(boat_data, waypoint)
            time.sleep(0.5)
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
    serial     = SerialConnection(port = r.port, log=log, logfilenum = r.run_number)
    main()

