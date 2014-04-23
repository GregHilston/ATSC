#!/bin/bash

usbDir='/Volumes/ATSC'
masterDir='/Users/Receptionist/Documents/ATSC/'

diff -qr --exclude=".*" --exclude="System Volume Information" /Volumes/ATSC /Users/Receptionist/Documents/ATSC/
