#!/usr/bin/env python
# Reference: http://stackoverflow.com/questions/9004135/merge-multiple-xml-files-from-command-line
'''
Script used to combine multiple .rbbx files into one, allowing human interaction with many .rbbx files to be quicker
'''

import sys
import fileinput
import time
from xml.etree import ElementTree

__author__ = 'Tyler_And_Greg' # Best ever
combined_files_limit = 3  # Number of students should be this number * 75
DEBUG_MODE = 1

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
    combined_counter = 1 # Number of combined files being created or about to be created
    file_counter = 0 # What .rbbx file we are currently on
    first = None # Our ElementTree
    combined_filenames = set() # To keep only unique filenames
    
    for filename in files:
        data = ElementTree.parse(filename).getroot()

        if first is None:
            first = data
        else:
            first.extend(data)

        #  Writing to file
        modified_filename = filename.rsplit('\\', 1)[1] # Remove the file path
        modified_filename = modified_filename.split(" (")[0] + ".rbbx" # Remove the student numbering
        modified_filename = str(combined_counter) + "_" + modified_filename # To differentiate multiple files 
        
        if DEBUG_MODE:
            print "modified_filename: " + modified_filename
        
        file = open((modified_filename), 'w+')
        
        file.write(ElementTree.tostring(first))
        file.close()
        file_counter += 1

        if file_counter % combined_files_limit == 0:
            combined_filenames.add(modified_filename) # Done with this file, so add it to our list
            combined_counter += 1
            first = None # Empties the element tree, as we would push over 400 students
            
    combined_filenames.add(modified_filename) # Adds the last file, set ensures uniqueness

    
    print "combined_counter: " + str(combined_counter)
    for file in combined_filenames:
        if DEBUG_MODE:
            print "\tPassing to remove_ns0: " + file
            
        remove_ns0(file)


if  __name__ =='__main__':
    if DEBUG_MODE:
        # Printing all arguements passed in
        print "len(sys.argv): " + str(len(sys.argv))
        for arg in sys.argv:
            print "\t" + arg
        
    combine(sys.argv[1:]) # -2: 1 for the filename of this script, 2 for the weird .rbbx0 passed by windows
