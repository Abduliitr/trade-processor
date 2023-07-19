import gzip

from constants import sectionSizeDictionary

class TradeProcessor:
    def __init__(self, filepath):
        self.filepath = filepath

    def processMessage(self, category, message):
        print(category, message)

    def processFile(self):
        test_iterator, end = 0, 20
        with gzip.open(self.filepath, 'rb') as datafile:
            category = datafile.read(1)
            while True and test_iterator < end:
                if not category:
                    print("Reached EOF!!")
                    break;

                if(category in sectionSizeDictionary):
                    message = datafile.read(sectionSizeDictionary[category] - 1)
                    print(category, message)
                    self.processMessage(category, message)
                else:
                    print(category)
                category = datafile.read(1)
                test_iterator += 1
                
        datafile.close()