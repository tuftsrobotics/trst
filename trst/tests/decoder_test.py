"""
feeder.py
feeds NMEA 2000 data slowly to analyzer
"""

import sys
import os
import pytest

from trst.decoders.decoder import Decoder, MalformedLineError, parse_line
from trst.utils.test_utils import raises, get_sample_fp

def test_open_file():
    d = Decoder(get_sample_fp('feed1'))
    assert d.sleep_time == 0

def test_stdin():
    d = Decoder()

def test_run_file():
    d = Decoder(get_sample_fp('feed1'))
    d.run()

def test_malformed_file():
    d = Decoder(get_sample_fp('bad_feed'), skip_malformed = False)
    raises(MalformedLineError, d.run)

def test_parse_line():
    l1 = "1F119 00FF7FFF7FFF7FFF\n\n\n"
    pgn, body = parse_line(l1)
    assert pgn == 0x1F119
    assert body == "00FF7FFF7FFF7FFF"

def test_malformed_line1():
    l1 = "1F119 00FF7FFF7FFF7FFF\n\na"
    raises(MalformedLineError, parse_line, l1)

def test_malformed_line2():
    l2 = "1FG119 00FF7FFF7FFF7FFF\n\n"
    raises(MalformedLineError, parse_line, l2)

def test_malformed_line3():
    l3 = "1F119 00FF7FFF7FFF7FFFA\n\n"
    raises(MalformedLineError, parse_line, l3)

#TODO write tester for serial connection
