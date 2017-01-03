import os
def _excstr(exc):
    if type(exc) is tuple:
        return str(tuple(map(_excstr, exc)))
    return exc.__name__

def raises(exc, func, *args, **kwds):
    """Raise AssertionError if ``func(*args, **kwds)`` does not raise *exc*.
    FROM SPHINX PROJECT"""
    try:
        func(*args, **kwds)
    except exc:
        pass
    else:
        raise AssertionError('%s did not raise %s' %
                             (func.__name__, _excstr(exc)))


def raises_msg(exc, msg, func, *args, **kwds):
    """Raise AssertionError if ``func(*args, **kwds)`` does not raise *exc*,
    and check if the message contains *msg*.

    FROM SPHINX PROJECT"""

    try:
        func(*args, **kwds)
    except exc as err:
        assert msg in str(err), "\"%s\" not in \"%s\"" % (msg, err)
    else:
        raise AssertionError('%s did not raise %s' %
                             (func.__name__, _excstr(exc)))

def get_sample_fp(fp):
    """helper to get sample files"""
    return os.path.abspath('./tests/samplefiles/' + fp)
