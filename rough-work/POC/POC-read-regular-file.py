"""
Compress        : gzip filename
Decompress      : gzip -d filename.gz
Read Compressed : gzcat filename.gz | head -5
Read Depressed  : cat filename | head -5
"""

filename = "samplecopy.txt"
n = int(input())

print("The content in the file is: ")
with open(filename, 'r') as filedata:
    linesList = filedata.readlines()
    for line in linesList[:n]:
        print(line, end='')
        
filedata.close()