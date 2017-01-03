def get_filt():
    """ uses the files pgn.py and valid_pgns to get the set of pgns we track"""
    p = Pgns()
    good_pgn_set = p.valid_set
#    good_pgns = set([129029])
    pgn_filter = lambda x: pgn_is_good(x, good_pgns)
    return filt
