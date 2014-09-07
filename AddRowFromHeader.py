# This script allows you to input a row to a file by asking you for each column value for 
# the row.
# The script first asks for the file you want to add a row to. Then, it reads the first row
# of the file and then asks you for the value of each column found in the header. It then 
# appends the row with these column values.

# Created by:     Praneet Puppala
# Created on:     August 20, 2014
# Last Modified:  August 20, 2014

import sys
import csv

# File to add to
fileName = raw_input("File to append to: ")
file = open(fileName, 'rU')
reader = csv.reader(file)

header = reader.next()
toAdd = []

for col in header:
    val = raw_input("{!s}: ".format(col))
    toAdd.append(val)

# close read-version of the file and open as write
file.close()
file = open(fileName, 'a')
writer = csv.writer(file)

writer.writerow("")
writer.writerow(toAdd)
print "Added: {!s}".format(toAdd)

file.close()
