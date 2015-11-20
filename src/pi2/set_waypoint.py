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
                d[i] = {'Latitude' : point.latitude, 'Longitude' : point.longitude}
    return d

def csv_main(infile, logfilenum):
    data = csv.reader(open(infile))
    d = {}
    for i, (lat, lon) in enumerate(data):
        d[i] = {'Latitude' : lat, 'Longitude' : lon} #key type integer
    return d

if __name__ == '__main__':
    a = ArgumentParser()
    a.add_argument('infile', help='waypoint csv file')
    a.add_argument('-t', action = 'store', dest = 'run_number', help='run number used in logging')
#TODO auto filetype detection
    a.add_argument('-g', '--gpx', action = 'store_true', help='flag for gpx filetype')
    r = a.parse_args()
    d = {}
    if r.gpx:
        d = gpx_main(r.infile, r.run_number)
    else:
        d = csv_main(r.infile, r.run_number)
    data.post_request(string = 'waypoint', data = d)
