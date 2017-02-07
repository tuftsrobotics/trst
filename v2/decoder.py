import sys
import time
import subprocess
from pgns import Pgns
#from signal import signal, SIGPIPE, SIG_DFL
#signal(SIGPIPE,SIG_DFL)

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

def analyze(lines, boat = None):
    """ takes a line and pushes the data to boatd"""
    s = ''
    print lines
#TODO this opens a new analyzer process for every line, very slow... please fix me
    proc = subprocess.Popen(['analyzer', '-json'],
                            stdin = subprocess.PIPE,
                            stdout = subprocess.PIPE)
#    stdout_val, stderr_val = proc.communicate(s)
    proc.stdin.write(s)
    for line in proc.stdout:
        print line
    proc.stdin.close()

class MalformedLineError(Error):
    """Error thrown when line in is malformed"""
    def __init__(self, expr, msg = None):
        self.expr = expr
        self.msg = msg
    def __repr__(self):
        return self.expr

def is_well_formatted(line):
    try:
        parse_line(line)
        return True
    except MalformedLineError:
        return False

def list_to_csv(l):
    """Python list to csv string"""
    s = str(l[0])
    for l in l[1:]:
        s += ',' + str(l)
    return s + '\n'

def parse_line(line):
    """Parses string line into a tuple of pgn and body"""
    try:
        pgn, body = line.rstrip().split()
        pgn = int(pgn, base = 16)
        assert len(body) == 16
        return pgn, body
    except (ValueError, AssertionError):
        raise MalformedLineError(line)


class Accumulator(object):
    """Accumulates lines with the same PGN to group multi-line messages"""
    def __init__(self):
        self.pgn = None
        self.lines = []

    def update(self, line):
        """Inserts a line into the accumulator, and returns if a new PGN is found

        Args:
            line (str): format [pgn] [body]
        """
        pgn, body = parse_line(line)
        if pgn == self.pgn:
            self.lines.append(line)
            return None
        else:
            self.pgn = pgn
            to_return = self.lines
            self.lines = [line]
            return to_return

def to_can_analyzer_multi(lines):
    to_return = ""
    for line in lines:
        to_return += to_can_analyzer_format(line)
    return to_return

def to_can_analyzer_format(line):
    """ formats data into analyzer input data

    Format is as follows: [0,0,pgn(base 10),0,0,8,FF,FF,FF,FF,FF,FF,FF,FF] note
    that the F chars indicate hex data with comma separated bytes

    Args:
        line: tuple of (pgn, data)
    """
    pgn, body = line.rstrip().split()
    pgn = int(pgn, base = 16)
    assert(len(body) == 16)
    body = [body[i:i+2] for i in range(0, len(body), 2)]
    line = [time.clock(),0, pgn, 0,0, 8]
    line.extend(body)
    return list_to_csv(line)

class File_Decoder(object):
    def __init__(self, fp=None, sleep_time=0, skip_malformed=True, pgn_file=None):
        self.filter_func = Pgns(pgn_file).get_filter_func()
        if fp is None:
            self.inf = sys.stdin
        else:
            self.inf = open(fp)
        self.sleep_time = sleep_time
        self.skip_malformed = skip_malformed

    def run(self):
        accum = Accumulator()
        count = 0
        for line in self.inf:
            if count < 100:
                count += 1
                continue
            if self.skip_malformed and not is_well_formatted(line):
                continue
            if not self.filter_func(parse_line(line)[0]):
                continue
            out = accum.update(line)
            if out is not None and out != []:
                sys.stdout.write( to_can_analyzer_multi(out))
#                analyze(to_can_analyzer_multi(out))
            time.sleep(self.sleep_time)
#
class Serial_Decoder(object):
    """ Initializes a serial connection and waits for valid NMEA 2000 input
    """
    def __init__(self, port = '/dev/ttyACM0', baud = 115200):
        import serial
        self.serial = serial.Serial(port, baud)
        self.skip_malformed = True

    def run(self):
        accum = Accumulator()
        try:
            while True:
                line = self.serial.readline()
                print line
                if self.skip_malformed and not is_well_formatted(line):
                    continue
                out = accum.update(line)
                if out is not None and out is not []:
#                    sys.stdout.write( to_can_analyzer_multi(out))
                    analyze(out)
        except KeyboardInterrupt:
            print "\nINTERUPT PROGRAM HALT"


if __name__ =='__main__':
#    d = File_Decoder(fp = '../data/1/feed', sleep_time = 0.0, pgn_file = "valid_pgns")
    #d = Serial_Decoder()
    d = Serial_Decoder(port='/dev/cu.usbmodem1461')
    d.run()
