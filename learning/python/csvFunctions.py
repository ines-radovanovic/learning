__author__ = 'ines'

import numpy

# function: averageCurrent
#
# computes the average value given a count of header lines to skip,
# an index to current column & csv reader
def findColumnAverage(headerCount, columnLabels, column_indeces, csv_reader):
    # skip header lines
    all_averages = []
    for line in range(headerCount):
        all_averages = next(csv_reader)

    count = 0
    for row in csv_reader:
        for i_column in column_indeces:
            all_averages[i_column]=float(all_averages[i_column])+float(row[i_column])
        count=count+1

    columnAverages = []
    for index,colAverage in enumerate(all_averages):
        if column_indeces.__contains__(index):
            colAverage = colAverage/count
            columnAverages.append(colAverage)

    averages_dict = dict(zip(columnLabels, columnAverages))

    return averages_dict

# function: stepThroughColumns
#
# gets the label for each column along with the index
def stepThroughColumns(csv_reader, headerRow):
    header_row = []
    for line in range(headerRow):
        header_row = next(csv_reader)

    columnLabels = []
    column_indeces = []
    for column in range(2, len(header_row)):
        label = header_row[column].strip()
        if label.__ne__('unused'):
            columnLabels.append(label)
            column_indeces.append(column)

    return findColumnAverage(headerRow+2, columnLabels, column_indeces, csv_reader)


def generatePowerColumns(csv_reader, headerRow):
    header_row = []
    for line in range(headerRow):
        header_row = next(csv_reader)

    power_labels = header_row[2:]
    power_labels = [i.strip() for i in power_labels]
    for column in range (2, 17):
        label = header_row[column].strip()
        if label.__ne__('unused'):
            label = label.replace('i', 'p',1)
        power_labels.append(label)

    for line in range(2):
        next(csv_reader)

    r = 0
    column_averages = [0] * (len(header_row) + 15)
    for row in csv_reader:
        temp_row = [float(i) for i in row]
        for column in range(2, 17):
            power = float(row[column]) * float(row[column + 16])
            temp_row.append(power)

        column_averages = numpy.add(column_averages, temp_row)
        r=r+1
    column_averages = column_averages/r
    column_averages = list(column_averages[2:])

    column_map = dict(zip(power_labels, column_averages))
    #del(column_map['unused'])

    ilist = []
    vlist = []
    plist = []

    for i,label in enumerate(power_labels):
        if label.startswith('i'):
            ilist.append((label,column_averages.__getitem__(i)))
        elif label.startswith('v'):
            vlist.append((label,column_averages.__getitem__(i)))
        elif label.startswith('p'):
            plist.append((label,column_averages.__getitem__(i)))

    lists = zip(ilist, vlist, plist)
    return column_map, lists


def getCapacitance(icpu1, icpu2, freq1, freq2, vcpu):
    cap1 = 1000*(icpu2 - icpu1)/((freq2 - freq1)*vcpu)

    return cap1
