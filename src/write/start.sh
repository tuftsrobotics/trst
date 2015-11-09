#!/bin/bash

./dataLogger.py &
./dataLogger2.py&

python pi_writer.py
