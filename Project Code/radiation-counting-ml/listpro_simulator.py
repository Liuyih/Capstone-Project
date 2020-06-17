"""
usage: python listpro_simulator.py data/cs.dat
Reads in file from argument, writes it out like ListPRO
"""

import sys
from lib.ortec_file_utils import get_file_contents, simulate_listPRO_output

if len(sys.argv) != 2:
    exit("Error: single filename argument mandatory")

infile = sys.argv[1]

print("Reading file...")
file_bytes = get_file_contents(infile)

print("Writing file...")
simulate_listPRO_output(file_bytes, "data/testfile.dat")
