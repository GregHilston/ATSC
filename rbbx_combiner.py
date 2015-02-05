#!/usr/bin/env python
# Reference: http://stackoverflow.com/questions/9004135/merge-multiple-xml-files-from-command-line

import sys
import fileinput
from xml.etree import ElementTree

__author__ = 'Tyler_And_Greg'
combined_files_limit = 3  # Number of students should be this number * 75


'''
As it stands, blackboard has a limitation of a student size xml file (Which is referred to as .rbbx files) of 400.
The program used to generate the .rbbx files does so in chunks of 75 students.
The program accepts any number of .rbbx files and combines them into files of 375 students, essentially combining up to
5 files into one.
'''


# Remove all "nso:" namespace from the file
def remove_ns0(file):
    for line in fileinput.FileInput(file, inplace=1):
        line = line.replace("ns0:", "")
        print line,  # Printed on same line


# Given any number of .rbbx files, combines up to five .rbbx files into one, resulting in files of 375 students or less
def combine(files):
    combined_counter = 0
    file_counter = 0  # What .rbbx file we are currently on
    first = None  # Our ElementTree

    for filename in files:
        data = ElementTree.parse(filename).getroot()

        if first is None:
            first = data
        else:
            first.extend(data)

        #  Decide what file to write to
        file = open(('combined' + str(file_counter / combined_files_limit) + '.rbbx'), 'w+')

        file.write(ElementTree.tostring(first))
        file.close()
        file_counter += 1

        if file_counter % combined_files_limit == 0:
            combined_counter += 1
            first = None # Empties the element tree, as we would push over 400 students

    for i in range(combined_counter):  # + 1 for 0 based
        remove_ns0("combined" + str(i) + ".rbbx")


if  __name__ =='__main__':
    combine(sys.argv[1:])
