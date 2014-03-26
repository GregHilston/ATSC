#!/bin/bash
# Academic Apps USB - Integrity Checker
# Usage: This is used to generate a "goodCheckSums.md5"


find . -type f -not -name "goodCheckSums.md5" -not -name "calculateVerifyCheckSums.sh" -not -name "calculateGoodCheckSums.sh" -not -name "verifyCheckSums.md5" -not -name "\.*" -exec md5sum '{}' \; > goodCheckSums.md5 # Mac's "md5sum" program is called md5, so change that to execute on a Mac

echo Successfully generated goodCheckSums.md5
