import socket

def _float(v):
    if v:
        return float(v[:-1])
    else:
        return None

class TrackSailInterface(object):
    def __init__(self, host='localhost', port=5555):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.connect((host, port))
        self._rudderPos = 0

    def _send_command(self, command):
        self._socket.send(command)
        return self._socket.recv(256)

    @property
    def wind_direction(self):
        """Return the direction of the wind"""
        return _float(self._send_command('get wind_dir'))

    def bearing(self):
        """Return the bearing of the boat"""
        return _float(self._send_command('get compass'))

    @property
    def sail_position(self):
        return _float(self._send_command('get sail'))

    @sail_position.setter
    def sail_position(self, value):
        self._send_command('set sail {}'.format(int(value)))

    @property
    def rudder_position(self):
        return self._rudderPos

    @rudder_position.setter
    def rudder_position(self, value):
        value_rounded = int(round(value))
        self._send_command('set rudder {}'.format(value_rounded))

    @property
    def latitude(self):
        return self._send_command('get northing')

    @property
    def longitude(self):
        return self._send_command('get easting')
