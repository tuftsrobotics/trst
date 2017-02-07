from argparse import ArgumentParser

import sys
import json
import requests
from  trst.pgns.pgns import Pgns
#from signal import signal, SIGPIPE, SIG_DFL
#signal(SIGPIPE,SIG_DFL)

def open_log_file(run_number = 0):
    f = open('log/uploader/' + str(logfilenum) + '.log', 'a+')
    return f

class Boat(object):
    def __init__(self):
        self.url = "http://127.0.0.1:8888/"

    def post(self, data):
        requests.post(self.url, json = data)

    def get(self):
        return requests.get(self.url)

def main(log = None):
    boat = Boat()
    key_errors = 0
    for line in sys.stdin:
    #    print "uploading", line
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
            except KeyError:
                key_errors += 1
                if key_errors % 100 == 0:
                    print key_errors, "Key Errors"
        except ValueError:
            print "Value ERROR:", line

if __name__ == '__main__':
#PARSE
    argparser = ArgumentParser()
    argparser.add_argument('-t', action = 'store', dest = 'run_number', help='run number used in logging')
    #argparser.add_argument('-pgnfile', action = 'store', dest = 'pgn_fp', default = 'valid_pgns', help='port for uploader arduino')
    r = argparser.parse_args()
    log = (r.run_number is not None)
    #pgn_filter = Pgns(pgn_fp).get_filter_func()
    main(log = log)
