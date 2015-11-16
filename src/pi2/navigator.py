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



pid_nav = pid.PID()
boat_state = BoatState()
serial     = SerialConnection(port = '/dev/ttyACM1')

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
    boat_state.set_rudder_scaled_pos(pid_nav.update(float(boat_data['Heading'])))
    serial.write(state = boat_state)

def main():
    print type(initial_waypoint)
    data.post_request('waypoint', initial_waypoint)
    while 1:
        waypoint = data.get_request('waypoint').text
        boat_data = data.get_request('').json()
        navigate(boat_data, waypoint)
        time.sleep(0.5)

if __name__ == '__main__':
    main()
