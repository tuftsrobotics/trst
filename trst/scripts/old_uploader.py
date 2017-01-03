import time
from trst.pgns.pgns import Pgns
import serial
import subprocess
import requests
import json
from argparse import ArgumentParser

#def analyze(lines, boat = None):
#    """ takes a line and pushes the data to boatd"""
#    if boat is None:
#        print "HALP no boat"
#    s = ''
#    for l in lines:
#        s += line_to_csv(l)
##TODO this opens a new analyzer process for every line, very slow... please fix me
#    proc = subprocess.Popen(['analyzer', '-json'],
#                            stdin = subprocess.PIPE,
#                            stdout = subprocess.PIPE,
#                            stderr = subprocess.PIPE)
#    stdout_val, stderr_val = proc.communicate(s)
#    json_val = stdout_val
#    try:
#        data = json.loads(json_val)
#        try:
#            fields = data["fields"]
#            if data["description"] == "Wind Data":
#                ref = fields["Reference"]
#                if ref == "Apparent":
#                    fields["App Wind Angle"] = fields.pop("Wind Angle")
#                    fields["App Wind Speed"] = fields.pop("Wind Speed")
#                if ref == "True (ground referenced to North)":
#                    fields["True Wind Angle"] = fields.pop("Wind Angle")
#                    fields["True Wind Speed"] = fields.pop("Wind Speed")
#            boat.post(fields)
#            return fields
#        except KeyError:
#            print "Key ERROR:", data
#    except ValueError:
#        print "Value ERROR:", json_val

def analyze(analyzer_proc, lines, boat = None):
    p = analyzer_proc
    """ takes a line and pushes the data to boatd"""
    if boat is None:
        print "HALP no boat"
    s = ''
    for l in lines:
        s += line_to_csv(l)
#TODO this opens a new analyzer process for every line, very slow... please fix me

    stdout_val, stderr_val = proc.communicate(s)
    json_val = stdout_val
    try:
        data = json.loads(json_val)
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
        print "Value ERROR:", json_val
class Boat(object):
    def __init__(self):
        self.url = "http://127.0.0.1:8888/"

    def post(self, data):
        """THIS WAS CHANGED FOR FLASK SERVER TRANSITION """
        requests.post(self.url, json = data)
#        requests.post(self.url, data = data)

    def get(self):
        return requests.get(self.url)

def get_filt():
    """ uses the files pgn.py and valid_pgns to get the set of pgns we track"""
    p = Pgns()
    good_pgns = p.valid_set
#    good_pgns = set([129029])
    filt = lambda x: pgn_is_good(x, good_pgns)
    return filt

def hex_to_int(h):
    """ converts hex string (no leading characters) to integer """
    return int(h, base = 16)

def line_to_csv(line):
    """ converts python list to csv string"""
    s = str(line[0])
    for l in line[1:]:
        s += ',' + str(l)
    return s + '\n'

def to_can_dump(line):
    """ formats data into analyzer input data

    Format is as follows: [0,0,pgn(base 10),0,0,8,FF,FF,FF,FF,FF,FF,FF,FF] note
    that the F chars indicate hex data with comma separated bytes
    """
    assert type(line) is list
    try:
        pgn, body = line
    except(ValueError):
        print "Malformed line"
        return None
    pgn = hex_to_int(pgn)
    assert(len(body) == 16)
    body = [body[i:i+2] for i in range(0, len(body), 2)]
    line = [time.clock(),0, pgn, 0,0, 8]
    line.extend(body)
    return line

def to_can_dump_with_time(line):
    """ formats data into analyzer input data

    Format is as follows: [time,0,pgn(base 10),0,0,8,FF,FF,FF,FF,FF,FF,FF,FF] note
    that the F chars indicate hex data with comma separated bytes
    """
    time_read, pgn, body = line
    pgn = hex_to_int(pgn)
    assert(len(body) == 16)
    body = [body[i:i+2] for i in range(0, len(body), 2)]
    line = [time_read, 0, pgn, 0,0, 8]
    line.extend(body)
    return line

def main_past():
    data = execute('../../data/2/feed.2', to_can_dump, filt, has_time = False) #GNSS Position Data
    boat = Boat()
    accum = [data[1]]
    for d in data:          # This is very strange... but the first line
        if d[2] == accum[-1][2]: #if same pgn
            accum.append(d)
        else:
            analyze(accum, boat) # analyze pgn return json
            accum = [d]

def main(track_time = False, ser = '/dev/ttyACM0', log = True, logfilenum = None):
    proc = subprocess.Popen(['analyzer', '-json'],
                            stdin = subprocess.PIPE,
                            stdout = subprocess.PIPE,
                            stderr = subprocess.PIPE)
    ser = serial.Serial(ser, 115200)
    if logfilenum is None:
        timesinceepoch = int(time.time())
        f = open('log/uploader/' + str(timesinceepoch) + '.log','a+')
    else:
        f = open('log/uploader/' + str(logfilenum) + '.log', 'a+')

    try:
        boat = Boat()
        #look for a good line
        can_line = None
        while can_line is None:
            line=ser.readline().rstrip()
            can_line = to_can_dump(line.split())
        accum = [can_line]
        while 1:
            #line is a string read from the serial port
            #look for a good line
            d = None
            while d is None:
                line=ser.readline().rstrip()
                if track_time:
                    line = time.clock() + " " + line
                d = to_can_dump(line.split())
            if log:
                print >> f, line
            if d[2] == accum[-1][2]: #if same pgn
                accum.append(d)
            else:
                analyzed = analyze(proc, accum, boat) # analyze pgn return json
                if log:
                    print >> f, analyzed
                accum = [d]
    except KeyboardInterrupt:
        print "\nINTERUPT PROGRAM HALT"
    f.close()

if __name__ == '__main__':

#PARSE
    argparser = ArgumentParser()
    argparser.add_argument('-t', action = 'store', dest = 'run_number', help='run number used in logging')
    argparser.add_argument('-port', action = 'store', dest = 'port', default = '/dev/ttyACM0', help='port for uploader arduino')
    r = argparser.parse_args()
    log = (r.run_number is not None)
    filt = get_filt()
    main(ser = r.port, log = log, logfilenum = r.run_number)
