import gzip
import os
import time

from collections import defaultdict

from constants import sectionSizeDictionary

if __name__ == '__main__':
    startTime = time.time()
    filepath = os.path.join(os.getcwd(), 'data', "01302019.NASDAQ_ITCH50.gz")
    print("Processing file at: ", filepath)

    testIterator, end = 0, 20
    processed = 0
    # categoryCount = defaultdict(int)    # b'\n\n`\xaa\xdb\x93'
    categorySamples = defaultdict(list)

    with gzip.open(filepath, 'rb') as datafile:
        category = datafile.read(1)
        while True and testIterator < end:
            if not category:
                print("Reached File End!!")
                break;

            if(category in sectionSizeDictionary):
                # processed += 1
                message = datafile.read(sectionSizeDictionary[category] - 1)
                # categoryCount[category] += 1
                if(len(categorySamples[category]) < 5):
                    categorySamples[category].append(message)
                # print(category, message)
            category = datafile.read(1)
            # testIterator += 1
            # if(processed % (10000000) == 0):
            #     print("Processed", processed / (1000000), "M message records in", (time.time() - startTime), "s")
            
    datafile.close()
    endTime = time.time()
    print("Processing completed in", (endTime - startTime), "s")
    # print("Category count processed is", categoryCount)
    print("Category samples are as follows:")
    print(categorySamples)