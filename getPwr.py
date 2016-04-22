__author__ = 'ines'


import glob, csv, re, os, sys, numpy, csvFunctions


# csv header lines count
header_lines = 13
header_label = 11

csv_files = glob.glob('input/*.csv')
out_format = 'format/d101'
file_format = open(out_format)
aList = file_format.readlines()
print aList

csv_dict = {}

outputFile='out.csv'
powerFile='pwr.csv'
writerOut = csv.writer(open(outputFile, 'wb', buffering=0))
writerPwr = csv.writer(open(powerFile, 'wb', buffering=0))

for i, csv_file in enumerate(csv_files):
    print 'Processing ' + csv_file

    # open file, read each line & compute average current and voltage
    csv_reader = csv.reader(open(csv_file, 'rb'))

    columnMap, avgData = csvFunctions.generatePowerColumns(csv_reader, header_label)

    print columnMap
    print columnMap.__len__()
    csv_dict.update(columnMap)
    for row in sorted(avgData):
         cols = [v for tuple in row for v in tuple]
         writerOut.writerow(cols)

print csv_dict
print csv_dict.__len__()

for power_rail in aList:
    power_rail = power_rail.rstrip()
    if csv_dict.get(power_rail) is not None:
        print power_rail + " " + "{0:.2f}".format(csv_dict.get(power_rail))
        writerPwr.writerow([power_rail,"{0:.2f}".format(csv_dict.get(power_rail))])
    else:
        print power_rail + " "
        writerPwr.writerow([power_rail," "])

