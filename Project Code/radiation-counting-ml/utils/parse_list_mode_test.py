import sys
from typing import Dict

import matplotlib.pylab as plt

data_filename = sys.argv[1]
data_filename_no_extension = data_filename.split('.')[0]

print('Program starting, filename is first arg:', data_filename)
print("raw file name:" + data_filename_no_extension)

outfileDataPath = "output/" + data_filename_no_extension + "Data_1.csv"
outfileHeaderPath = "output/" + data_filename_no_extension + "Header.csv"
outfileData = open(outfileDataPath, 'w')
outfileHeader = open(outfileHeaderPath, 'w')

in_header = True
initial_stage = True
detector_on = False

linecounter = 0
writeLine = ""

cycleID = 0
mS1counter = 0

dic_counts: Dict[int, int] = {}

with open(data_filename, 'r') as fp:
    for line in fp:
        linecounter += 1

        if in_header:
            outfileHeader.write(line.replace('\r', ''))
            if 'Acq Start Reference' in line:
                in_header = False
                outfileHeader.close()

        elif initial_stage and ('EX1' in line) and ('mS: 0' in line):
            initial_stage = False

        elif detector_on:
            # normal line write
            if 'ADC:' in line and 'Real:' in line and 'UTC Time:' in line:
                parse_string = line.split('Real:')[1]
                parse_string, time = parse_string.split('UTC Time:')
                parse_string, channel_str = parse_string.split('ADC:')
                milliSec = parse_string.split('mS')[0]

                log_items = [str(cycleID), milliSec, channel_str, time.strip()]
                writeLine = ', '.join(log_items) + '\n'
                channel = int(channel_str.strip())
                if channel in dic_counts:
                    dic_counts[channel] += 1
                else:
                    dic_counts[channel] = 1

                outfileData.write(writeLine)

            if ('EX1' in line) and ('mS: 0' in line):
                detector_on = False

        # create new file
        elif ('EX1' in line) and ('mS: 1' in line):
            detector_on = True

            mS1counter += 1
            cycleID += 1
            outfileData.close()
            outfileDataPath = (
                f'output/{data_filename_no_extension}Data_{cycleID}.csv'
            )
            outfileData = open(outfileDataPath, 'w')
            outfileData.write("runID, millisec, Bin, timestamp \n")
            print(
                f'lines read so far: {linecounter}, last line of '
                f'previous cycle: {writeLine}'
            )
            print('new cycle: {cycleID} line: {line}')

print(
    f'cycleCounter: {cycleID}, linecounter: {linecounter}, '
    f'mS1counter: {mS1counter}'
)

lists = sorted(dic_counts.items())
x, y = zip(*lists)
plt.plot(x, y)
plt.show()
# to see all millisec decimal places in R options(digits=10) and to load into R
# dataframe: filename<-read.csv("parsedFileName")
