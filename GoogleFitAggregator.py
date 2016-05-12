'''
Rudimentary csv aggregator used for putting all of the csv's you get when you
download your Google Fit data from takeout.google.com into one csv file.
Pulls the information from the csv file names and adds a column to the beginning
with that date.

Author: Benjamin Matase
'''
from os import listdir
from os.path import isfile, join

mydir = '/home/ben/Downloads/Takeout/Fit/Daily Aggregations/'

onlyfiles = [f for f in listdir(mydir) if isfile(join(mydir, f))]

#doesn't matter which file to extract header from, all are same
f = open(onlyfiles[0])
header = f.readline()
f.close()

#add on Date variable in front
header = 'Date,' + header

strArray = []

new_f = open('aggregated.csv', 'a')
new_f.write(header)

for i in range(0, len(onlyfiles)):
    f = open(onlyfiles[i])
    #burn header
    f.readline()

    name = f.name

    content = f.readlines()

    for x in content:
        output = name[0:len(name) - 4] + ',' + x
        new_f.write(output)

    f.close()

new_f.close()
