#Navigator.py
#Created by Alex Tong 5 Jul 2015
#
#
#

initial_waypoint = {'Latitude': 42.432136, 'Longitude': -71.147794}
# about 100 meters off the dock

from LatLon import LatLon
import data
import pid
from boatstate import BoatState
pid_nav = pid.PID()
boat_state = BoatState()

def get_vect_to_wp(p):
    c = data.request('gps')
    print c.json()

def get_vect(p1, p2):
    """returns heading and magnitude between two latlon objects """
    assert type(p1) == type(LatLon)
    assert type(p2) == type(LatLon)
    return p2 - p1


def navigate(boat_data, waypoint):
    current_pos = LatLon(Latitude(boat_data['Latitude']), Longitude['Longitude'])
    next_pos = LatLon(Latitude(waypoing['Latitude']), Longitude['Longitude'])
    pid_nav.target = current_pos.heading_initial(next_pos)
    boat_state.set_rudder_scaled_pos(pid_nav.update(boat_data.Heading))


def main():
    post_request('waypoint', initial_waypoint)

    while 1:
        waypoint = get_request('waypoint')
        boat_data = get_request('')
        navigate(boat_data, waypoint)
    pass

if __name__ == '__main__':
    main()
