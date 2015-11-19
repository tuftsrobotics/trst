"""
This script parses a waypoint csv file with each line of the form:
    [latitude],[longitude]
where each line represents a waypoint
"""
from argparse import ArgumentParser
import csv
import data
import gpxpy

def gpx_main(infile, logfilenum):
    gpx_file = open(infile)
    d = {}
    gpx = gpxpy.parse(gpx_file)
    for track in gpx.tracks:
        for segment in track.segments:
            for i, point in enumerate(segment.points):
                d[str(i)] = {'latitude' : point.latitude, 'longitude' : point.longitude}
    print d

def csv_main(infile, logfilenum):
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
#TODO auto filetype detection
    a.add_argument('-g', '--gpx', action = 'store_true', help='flag for gpx filetype')
    r = a.parse_args()
    print r
    if r.gpx:
        gpx_main(r.infile, r.run_number)
    else:
        csv_main(r.infile, r.run_number)
