#Navigator.py
#Created by Alex Tong 5 Jul 2015
#
#
#


from LatLon import LatLon
import data

def get_vect_to_wp(p):
    c = data.request('gps')
    print c.json()

def get_vect(p1, p2):
    """returns heading and magnitude between two latlon objects """
    assert type(p1) == type(LatLon)
    assert type(p2) == type(LatLon)
    return p2 - p1


def main():
    get_vect_to_wp(LatLon(1,1))
    pass

if __name__ == '__main__':
    main()
