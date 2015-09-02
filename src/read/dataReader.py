"""
dataReader.py

Written by Alex Tong Sep 2 2015

This file reads a datafile into a python object

The datafile format is currently:
[pgn] [data]
where pgn is 5 hex dgits and data is 16 hex digits

"""

#import numpy as np
import csv

def to_list(l):
    
    l[1] = int(l[1], base = 16)
    return l

def to_can_dump(pgn, body):
    pgn = int(pgn, base = 16)
    assert(len(body) == 16)
    body = [body[i:i+2] for i in range(0, len(body), 2)]
    line = [0,0, pgn, 0,0, 8]
    line.extend(body)
    return line

def execute(fp, fun):
    data = []
    with open(fp) as f:
        for line in f:
            l = line.rstrip().split()
            if not len(l) == 2:
                assert(False)
            pgn, body = l
        
            data.append(fun(pgn, body))
    return data

def line_to_csv(line):
    s = str(line[0])
    for l in line[1:]:
        s += ',' + str(l)
    print s
    return s


if __name__ == '__main__':
    data = execute('../../data/1/feed', to_can_dump)
    for d in data[-20:]:
        print line_to_csv(d)
#    print data
    

