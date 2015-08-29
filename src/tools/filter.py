#The purpose of this script is to filter NMEA2000 data by pgn to examine particular
#pgn types

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('string-to-grep', help='regex to grep')
parser.add_argument('file', help='datafile to grep')
parser.parse_args()



