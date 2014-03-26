#!/bin/bash
# Academic Apps USB - Integrity Checker
# Usage: Have the goodCheckSums.md5 and this script [calculateVerifyCheckSums.sh] in the root folder of the USB
#			To execute, from terminal type ./calculateVerifyCheckSums.sh


find . -type f -not -name "goodCheckSums.md5" -not -name "calculateVerifyCheckSums.sh" -not -name "calculateGoodCheckSums.sh" -not -name "verifyCheckSums.md5" -not -name "\.*" -exec md5sum '{}' \; > verifyCheckSums.md5 # Mac's "md5sum" program is called md5, so change that to execute on a Mac

if diff goodCheckSums.md5 verifyCheckSums.md5 >/dev/null ; then
	echo No changes detected.
else 
	echo Changes detected. Re-image USB
fi
