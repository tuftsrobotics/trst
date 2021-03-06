import os

class Pgns(object):
    def __init__(self, fp = None):
        """reads a valid pgn file and returns a set of valid pgn ints

        a valid fp will be a space separated file with a single line containing
        all valid pgns all other pgns will be ignored

        Args:
            fp (file): string pointing to valid_pgn file
        """
        self.valid_set = set()
        if fp is None:
            fp = os.path.join(os.path.dirname(__file__), 'valid_pgns')
        with open(fp) as f:
            for line in f:
                valid = line.rstrip().split()
                self.valid_set |= set([int(i, base = 16) for i in valid])

    def is_valid_pgn(self, pgn):
        if type(pgn) == int:
            return pgn in self.valid_set
        return int(pgn, base = 16) in self.valid_set

    def get_filter_func(self):
        return lambda pgn: self.is_valid_pgn(pgn)

    def __repr__(self):
        return self.valid_set.__repr__()

if __name__ == "__main__":
    p = Pgns()
