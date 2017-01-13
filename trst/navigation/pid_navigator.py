from trst.navigation.navigator import Navigator
from trst.navigation.pid import PID


class PIDNavigator(Navigator):
    def __init__(self):
        self.pid_nav = PID()
        super(PIDNavigator, self).__init__()

    def navigate(self, boat_data, waypoint):
        curr_pos = self.get_latlon_from_dict(boat_data)
        next_pos = self.get_latlon_from_dict(waypoint)
        #TODO unhardcode deviation
        deviation = -14.8
        true_heading = float(boat_data['Heading']) + deviation
        if true_heading > 180: #correct to range [-180,180]
            true_heading = true_heading - 360
        #PID update
        self.pid_nav.target = float(curr_pos.heading_initial(next_pos)) #true angle to target
        rudder_target = self.pid_nav.update(true_heading)
        self.update_boat(rudder_target)
