"""
This script parses a waypoint csv file with each line of the form:
    [latitude],[longitude]
where each line represents a waypoint
"""
from argparse import ArgumentParser
import csv
import data

def main(infile, logfilenum):
    data = csv.reader(open(infile))
    d = {}
    for i, (lat, lon) in enumerate(data):
        key = ("waypoint%d" % i)
        d[key] = {'latitude' : lat, 'longitude' : lon}
    print d




     

if __name__ == '__main__':
    a = ArgumentParser()
    a.add_argument('infile', help='waypoint csv file')
    a.add_argument('-t', action = 'store', dest = 'run_number', help='run number used in logging')
    r = a.parse_args()
    main(r.infile, r.run_number)
