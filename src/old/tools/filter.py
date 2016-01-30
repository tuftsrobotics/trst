#The purpose of this script is to filter NMEA2000 data by pgn to examine particular
#pgn types

"""
The purpose of this script is to filter NMEA2000 data by pgn to examine particular
pgn types
Example:
    python filter.py "FFFFF" data.dat
    will find and print to stdout all the lines that contain the string FFFFF
"""

import argparse
import subprocess
if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('regex', help='regex to grep')
    parser.add_argument('file', help='datafile to grep')
    args = parser.parse_args()

    proc = subprocess.Popen(['egrep', args.regex, args.file],
                            stdin = subprocess.PIPE,
                            stdout = subprocess.PIPE,
                            stderr = subprocess.PIPE)
    stdout_val, stderr_val = proc.communicate('')
    print stdout_val



