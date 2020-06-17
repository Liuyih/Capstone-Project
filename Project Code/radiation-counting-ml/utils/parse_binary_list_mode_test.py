'''
Read in ListPRO output file from file given as argument.
Sum the counts for each channel and plot.

usage: python parse_binary_list_mode_test.py <ListPRO output file>
'''

import struct
import sys
from typing import Dict

import matplotlib.pylab as plt

# ListPRO binary file format:
HEADER_SIZE_BYTES = 256

# Ortec DSPEC-PRO List Mode data word format
WORD_SIZE_BYTES = 4

#   bits 31..30 prefix (2)
PREFIX_BIT_SHIFT = 30
PREFIX_ADC = 3

#   bits 29..16 channel (14)
CHANNEL_BIT_SHIFT = 16
CHANNEL_SIZE_BITS = 14
CHANNEL_MASK = (1 << CHANNEL_SIZE_BITS) - 1

dic_counts: Dict[int, int] = {}

if len(sys.argv) != 2:
    exit("Error: single filename argument mandatory")

binary_data_filename = sys.argv[1]

with open(binary_data_filename, "rb") as data:
    # skip header
    data.seek(HEADER_SIZE_BYTES)

    while True:
        raw_word = data.read(WORD_SIZE_BYTES)
        if not raw_word:
            break
        # read word in as 32 bit unsigned int
        # struct assumes little endian
        word = struct.unpack("I", raw_word)[0]

        # don't need mask because it's the 2 MSB
        prefix = word >> PREFIX_BIT_SHIFT

        # ignoring words with time and other data for now
        if prefix == PREFIX_ADC:
            # need mask to remove prefix bits after shift
            channel = (word >> CHANNEL_BIT_SHIFT) & CHANNEL_MASK
            if channel in dic_counts:
                dic_counts[channel] += 1
            else:
                dic_counts[channel] = 1

        if data.tell() % 100000 == 0:
            print("at byte offset:", data.tell())

print("Done.")

tuples = sorted(dic_counts.items())
x, y = zip(*tuples)
plt.plot(x, y)
plt.show()
