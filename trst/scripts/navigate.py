import time
from trst.navigation.navigator import PIDNavigator
from trst.navigation.boatstate import BoatState
from trst.serial.pyserial_driver import SerialConnection
from trst.server.data import *


WAIT_TIME = 0.5

def pull_data():
    boat_data = data.get_request('').json()
    if boat_data == {}:
        print "NO BOAT DATA EXITING"
    return boat_data

def main(log=False, logfilenum=None):
    #Make this so we can easily invoke different navigators
    nav = PIDNavigator()

    if logfilenum is None:
        timesinceepoch = int(time.time())
        f = open('log/navigator/' + str(timesinceepoch) + '.log','a+')
    else:
        f = open('log/navigator/' + str(logfilenum) + '.log', 'a+')
    try:
        while 1:
            #TODO how often do we pull waypoints?
            waypoints = data.get_request('waypoint').json()
            boat_data = pull_data()
            next_waypoint = waypoints["0"]
            nav.navigate(boat_data, next_waypoint) #note that dictionary keys are string
            time.sleep(WAIT_TIME)
    except KeyboardInterrupt:
        print "\nINTERUPT NAVIGATOR PROGRAM HALT"

if __name__ == '__main__':
#PARSE
    argparser = ArgumentParser()
    argparser.add_argument('-t', action='store', dest='run_number', help='run number used in logging')
    argparser.add_argument('-port', action='store', dest='port', default='/dev/ttyACM1', help='port for navigator arduino')
    r=argparser.parse_args()
    log=(r.run_number is not None)
#serial      = SerialConnection(port = '/dev/ttyACM1')
#    serial     = SerialConnection(port = r.port, log=log, logfilenum = r.run_number)
    main(log=log, logfilenum=run_number)
