class Pgns:
    def __init__(self, fp = None):
        """reads a valid pgn file and returns a set of valid pgn ints

        a valid fp will be a space separated file with a single line containing
        all valid pgns all other pgns will be ignored 

        Args:
            fp (file): string pointing to valid_pgn file 
        """
        if fp is None:
            fp = "valid_pgns"
        with open(fp) as f:
            valid = next(f)
        valid = valid.rstrip().split()
        valid = set([int(i, base = 16) for i in valid])
        self.valid_set = valid

    def __repr__(self):
        return self.valid_set.__repr__()

if __name__ == "__main__":
    p = Pgns()
    print p
