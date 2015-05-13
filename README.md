ATSC
====

Small short scripts written for the University of New Hampshire's "Academic Technology Support Center"

rbbx_combiner
     Combines multiple rbbx files into a large file, to ensure human entry into a webisite is quicker

Verify Academic Apps USB
     Compares a USB of Academic Apps to a read only folder, checking the integrity of the USB

rbbx_combiner Installtion Instructions

1. Install Python
   * Note: Only tested with Python version 2.7.9, which can be downloaded here https://www.python.org/downloads/release/python-279/

2. Download rbbx_combiner.py

3. Download Combine_rbbx.cmd

4. Note: All ATSC files can be downloaded in a .zip format from "https://github.com/GregHilston/ATSC/archive/master.zip"

5. Move rbbx_combiner.py to "C:\"

6. Move Combine_rbbx.cmd to "%APPDATA%\Microsoft\Windows\SendTo"
   * Note: To get to the SendTo folder, you’ll need to open up an Explorer window, and then paste in the following to the address bar. 
   * %APPDATA% is an environment variable that actually maps to something like C:\users\<username>\AppData\Roaming.
