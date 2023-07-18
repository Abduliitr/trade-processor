"""
Compress        : gzip filename
Decompress      : gzip -d filename.gz
Read Compressed : gzcat filename.gz | head -5
Read Depressed  : cat filename | head -5
"""

import gzip     # gzip for .gz, zipfile for .zip

filename = "sample.txt.gz"
n = int(input())

# Approach 1:
print("The content in the file is (approach 1): ")
with gzip.open(filename, 'rb') as filedata:
    linesList = filedata.readlines()
    for line in linesList[:n]:
        print(line)
        
filedata.close()

#Approach 2:
print("The content in the file is (approach 2): ")
with gzip.open(filename, 'rb') as filedata:
    linesList = filedata.read()
    print(len(linesList))
    print(chr(linesList[0]), chr(linesList[1]), linesList[19])
        
filedata.close()
