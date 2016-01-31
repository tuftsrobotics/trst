"""
Context file to allow tests from an adjacent test directory
"""

import sys
import os

print os.path.abspath('..')
sys.path.insert(0, os.path.abspath('..'))

import trst

