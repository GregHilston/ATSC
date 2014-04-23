#!/bin/bash

#Note: Change "/Volumes/ACADEMIC/" to match the path of the USE plugged in. Sometimes they are "ACADEMIC2" or "ACADEMIC3"

diff -qr --exclude=".*" --exclude="System Volume Information" /Volumes/ACADEMIC /Users/Receptionist/Documents/ACADEMIC/
