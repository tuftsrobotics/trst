#Navigator.py
#Created by Alex Tong 5 Jul 2015
#
#
#
"""
This module is a navigator given a series of waypoints on a server

"""

#initial_waypoint = {'Latitude': 42.432136, 'Longitude': -71.147794}
# about 100 meters off the dock

import abc
from LatLon import LatLon, Latitude, Longitude
from argparse import ArgumentParser
from trst.navigation.boatstate import BoatState


class Navigator(object):
    """
    Base class for navigators. Implements some navigation method and then
    update the boat state with the update_boat function
    """
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self.boat_state = BoatState()

    @staticmethod
    def get_vect_to_wp(p):
        c = data.request()

    @staticmethod
    def get_vect(p1, p2):
        """returns heading and magnitude between two latlon objects """
        assert type(p1) == type(LatLon)
        assert type(p2) == type(LatLon)
        return p2 - p1

    @staticmethod
    def get_latlon_from_dict(d):
        assert 'Latitude' in d and 'Longitude' in d
        return LatLon(d['Latitude'], d['Longitude'])

    @abc.abstractmethod
    def navigate(self, boat_data, waypoint):
        pass

    def update_boat(self, rudder_target):
        self.boat_state.set_rudder_scaled_pos(rudder_target)
