#!/usr/bin/env python
# Reference: http://stackoverflow.com/questions/9004135/merge-multiple-xml-files-from-command-line
'''
Script used to combine multiple .rbbx files into one, allowing human interaction with many .rbbx files to be quicker
'''

import sys
import fileinput
import time
import re
from xml.etree import ElementTree

__author__ = 'Tyler_And_Greg' # Best ever
combined_files_limit = 3  # Max input files per one combined file (Note: Number of students should be this number * 75)
DEBUG_MODE = 0 # Displays more information
combined_counter = 1 # Number of combined files being created or about to be created

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

# Based on the input file name and counters, generate an appropriate output file name
def generate_output_filename(filename):
    p = re.compile("\d*_\d*_\d*") # Construct a regex for the date
    match = p.search(filename) # Search the filename for the string that is the date
    
    modified_filename = filename.rsplit('\\', 1)[1] # Remove the file path
    modified_filename = re.compile("\d*_\d*_\d*").split(modified_filename)[0] # Use regex to remove the date and everything after (Ideally would just remove what's after it...)
    modified_filename = modified_filename + match.group(0) # Reattach the date, as the split removed it as the delimiter
    modified_filename = str(combined_counter) + "_" + modified_filename + ".rbbx" # To differentiate multiple files
    
    if DEBUG_MODE:
            print "modified_filename: " + modified_filename
            
    return modified_filename

# Given any number of .rbbx files, combines up to five .rbbx files into one, resulting in files of 375 students or less
def combine(files):
    global combined_counter # Needed to modify global variable
    file_counter = 0 # What .rbbx file we are currently on
    first = None # Our ElementTree
    combined_filenames = set() # To keep only unique filenames
    
    for filename in files:
        data = ElementTree.parse(filename).getroot()

        if first is None:
            first = data # Writing to a new file
        else:
            first.extend(data) # Extending the current file
       
        modified_filename = generate_output_filename(filename) # Get the output file name
        
        # Actually write to the file
        file = open((modified_filename), 'w+')
        file.write(ElementTree.tostring(first))
        file.close()
        file_counter += 1

        # Handle having to write to a new file, if we push the student limit for the current file
        if file_counter % combined_files_limit == 0:
            combined_filenames.add(modified_filename) # Done with this file, so add it to our list
            combined_counter += 1
            first = None # Empties the element tree, as we would push over 400 students
            
    combined_filenames.add(modified_filename) # Adds the last file, set ensures uniqueness
    
    print "Output:"
    for file in combined_filenames:
        if DEBUG_MODE:
            print "\tPassing to remove_ns0: " + file
        
        remove_ns0(file)
        print("\t" + file)
        
    print "***********************************************"

if  __name__ =='__main__':
    if DEBUG_MODE:
        # Printing all arguments passed in
        print "len(sys.argv): " + str(len(sys.argv))
        for arg in sys.argv:
            print "\t" + arg
            
    # Printing some other useful information regarding student limits per each file
    print "***********************************************"
    print "Each combined file contains <= " + str(combined_files_limit * 75) + " students"
    print "\tMax " + str(combined_files_limit) + " input files per combined file\n"
        
    combine(sys.argv[1:]) # Pass all input except the name of this script
