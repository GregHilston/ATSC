# Greg Hilston 

import tarfile
import hashlib

# Directory of Academic Apps USB goes here
target_dir = '/Volumes/ACADEMIC2/' # Replace "2" with the correct USB number [Eg. 1,2,3]

# Name of the tar file we are making goes here
tar_file_name = 'Academic_Apps.tar'

# Correct original md5 goes here
original_md5 = '9581cf2554b354724eb0db2163e6acf5' 


# Tar up all the contents of the USB
tar = tarfile.open(tar_file_name, "w") # "w" flag represents, 'do not compress' (saves time)
tar.add(target_dir)
tar.close()


# Open,close, read file and calculate MD5 on its contents 
with open(tar_file_name) as file_to_check:
    # read contents of the file
    data = file_to_check.read()    
    # pipe contents of the file through
    md5_returned = hashlib.md5(data).hexdigest()


# Finally compare original MD5 with freshly calculated
if original_md5 == md5_returned:
    print "USB device clean"
else:
    print "Possible infection detected. Reimage."
    print md5_returned # Uncomment if the "Correct original md5" is needed
