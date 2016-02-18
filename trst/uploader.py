from argparse import ArgumentParser

import sys
import json
import requests
from pgns import Pgns
#from signal import signal, SIGPIPE, SIG_DFL
#signal(SIGPIPE,SIG_DFL) 

def open_log_file(run_number = 0):
    f = open('log/uploader/' + str(logfilenum) + '.log', 'a+')
    return f

class Boat(object):
    def __init__(self):
        self.url = "http://127.0.0.1:8888/"

    def post(self, data):
        """THIS WAS CHANGED FOR FLASK SERVER TRANSITION """
#        print "posting", data
        requests.post(self.url, json = data)
#        requests.post(self.url, data = data)

    def get(self):
        return requests.get(self.url)

def main(log = None):
    boat = Boat()
    for line in sys.stdin:
        print "uploading", line
        try:
            data = json.loads(line)
            try:
                fields = data["fields"]
                if data["description"] == "Wind Data":
                    ref = fields["Reference"]
                    if ref == "Apparent":
                        fields["App Wind Angle"] = fields.pop("Wind Angle")
                        fields["App Wind Speed"] = fields.pop("Wind Speed")
                    if ref == "True (ground referenced to North)":
                        fields["True Wind Angle"] = fields.pop("Wind Angle")
                        fields["True Wind Speed"] = fields.pop("Wind Speed")
                boat.post(fields)
                return fields
            except KeyError:
                print "Key ERROR:", data
        except ValueError:
            print "Value ERROR:", line

if __name__ == '__main__':
#PARSE
    argparser = ArgumentParser()
    argparser.add_argument('-t', action = 'store', dest = 'run_number', help='run number used in logging')
    #filter for specific pgns to speed up analyzer if necessary
    #argparser.add_argument('-pgnfile', action = 'store', dest = 'pgn_fp', default = 'valid_pgns', help='port for uploader arduino')
    r = argparser.parse_args()
    log = (r.run_number is not None)
    #pgn_filter = Pgns(pgn_fp).get_filter_func()
    main(log = log)

