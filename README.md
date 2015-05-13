ATSC
====

Small short scripts written for the University of New Hampshire's "Academic Technology Support Center"

<h5> rbbx_combiner <h5>

     Combines multiple rbbx files into a large file, to ensure human entry into a webisite is quicker

<h5> Verify Academic Apps USB <h5>

     Compares a USB of Academic Apps to a read only folder, checking the integrity of the USB

<h2> rbbx_combiner installation Instructions - Manual <h2>

1. Install Python
   * Note: Only tested with Python version 2.7.9, which can be downloaded here https://www.python.org/downloads/release/python-279/

2. Download all ATSC files in a .zip format from "https://github.com/GregHilston/ATSC/archive/master.zip"

3. Unzip the files

4. Move rbbx_combiner.py to "C:\"

5. Move Combine_rbbx.cmd to "%APPDATA%\Microsoft\Windows\SendTo"
   * Note: To get to the SendTo folder, you’ll need to open up an Explorer window, and then paste that weird looking address into the address bar
   * %APPDATA% is an environment variable that actually maps to something like C:\users\<username>\AppData\Roaming.
 
