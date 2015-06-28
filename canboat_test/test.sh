#!/bin/bash
testfile=$1
candump2analyzer $test_file | analyzer > out
