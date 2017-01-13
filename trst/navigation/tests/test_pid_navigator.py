import unittest
import LatLon
from trst.navigation.pid_navigator import PIDNavigator

class TestNavigator(unittest.TestCase):
    def setUp(self):
        self.pid_nav = PIDNavigator()
        self.palmyra = {'Latitude': 5.8833, 'Longitude': -162.0833}
        # self.honolulu = {}
        self.boat_data = {'Heading': 22.0, 'Latitude': 21.3, 'Longitude': -157.8167}

    #TODO Write Tests
    def test_navigate(self):
        self.pid_nav.navigate(self.boat_data, self.palmyra)
