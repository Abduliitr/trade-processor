import gzip
import datetime
from datetime import timedelta
from decimal import Decimal

from constants import sectionSizeDictionary

class TradeProcessor:
    def __init__(self, filepath):
        self.filepath = filepath
        self.currHour = 0
        self.hourlyData = []
        self.timeinhrs = set()
        self.processed = 0
        self.records = 0
        self.result = []

    def appendFileHeader(self):
        self.result.append('| {:1} | {:^8} | {:>10} |'.format(*['hour', 'stock', 'VWAP']))
        self.result.append('\n' + ('-' * 32) + '\n')

    def convertTime(self, timeNanos):
        secs = timeNanos / 1e9
        td = timedelta(seconds=secs)
        return str(td)

    def getBinaryToRegular(self, binaryMessage, type):
        if(type == 'alpha'):
            res = ""
            for i in binaryMessage:
                res += chr(i)
        elif(type == 'num'):
            res = 0
            factor = 0
            for i in range(len(binaryMessage)-1, -1, -1):
                res += int(binaryMessage[i]) * (2 ** factor)
                factor += 8

        return res

    def calculateAndSaveOutput(self, outputFile, hour, data):
        self.appendFileHeader()
        volWeightedPrice = data[0][3] * data[0][5]
        totalVolume = data[0][3]
        for i in range(1, len(data)):
            if data[i][4] != data[i-1][4]:
                # calculate
                res = [hour, data[i-1][4], round(Decimal(volWeightedPrice / totalVolume), 4)]
                self.records += 1
                self.result.append('| {:4} | {:^8} | {:>10} |'.format(*res) + '\n')
                volWeightedPrice, totalVolume = 0, 0

            volWeightedPrice += data[i][3] * data[i][5]
            totalVolume += data[i][3]
        
        # calculate for the last stock
        res = [hour, data[len(data)-1][4], round(Decimal(volWeightedPrice / totalVolume), 4)]
        self.records += 1
        self.result.append('| {:4} | {:^8} | {:>10} |'.format(*res) + '\n')
        outputFile.writelines(self.result)
        print("Writing output completed for :", outputFile.name)
        self.result = []

    def processHourlyData(self, hour, data):
        # print(hour, data)
        """
        sample:
        4 
        [['4:00:00.199973', 0, 'B', 1, 'UGAZ', 39.16], 
        ['4:00:04.669287', 0, 'B', 200, 'SPY', 264.4], 
        ['4:00:47.194467', 0, 'B', 16, 'AMZN', 1613.71], 
        ['4:00:47.304877', 0, 'B', 55, 'SPY', 264.15], 
        ['4:00:55.381650', 0, 'B', 40, 'AAPL', 162.72]]

        [timestamp, orderRefNum, buySellInd, shares, stock, price]
        """
        data.sort(key = lambda x: x[4])     # sort based on stock symbol

        if(len(data) == 0):
            print("No Hourly Data to process.", hour, data)
            return

        with open('results/output-' + str(hour) + '.txt', 'w') as outputFile:
            self.calculateAndSaveOutput(outputFile, hour, data)
        outputFile.close()


    def processPTypeMessage(self, message):
        stockLocate     = self.getBinaryToRegular(message[:2],  'num')
        trackingNum     = self.getBinaryToRegular(message[2:4], 'num')
        timestamp       = self.getBinaryToRegular(message[4:10], 'num')
        orderRefNum     = self.getBinaryToRegular(message[10:18], 'num')
        buySellInd      = self.getBinaryToRegular(message[18:19], 'alpha')
        shares          = self.getBinaryToRegular(message[19:23], 'num')
        stock           = self.getBinaryToRegular(message[23:31], 'alpha').rstrip()
        price           = self.getBinaryToRegular(message[31:35], 'num')/10000
        matchNumber     = self.getBinaryToRegular(message[35:43], 'num')

        convertedTimestamp = self.convertTime(timestamp)

        # group based on hour.
        hour = int(convertedTimestamp.split(":")[0])
        self.timeinhrs.add(hour)

        if(hour == self.currHour):
            self.hourlyData.append([convertedTimestamp, orderRefNum, buySellInd,
                shares, stock, price])
        else:
            # process previous hour data here to calculate vwap
            self.processHourlyData(self.currHour, self.hourlyData)
            self.currHour = hour
            self.hourlyData = []        # reset for new hour data.
            self.hourlyData.append([convertedTimestamp, orderRefNum, buySellInd,
                shares, stock, price])


    def processMessage(self, category, message):
        # print(category, message)
        if(category == b'P'):
            self.processPTypeMessage(message)

    def processFile(self):
        test_iterator, end = 0, 100
        with gzip.open(self.filepath, 'rb') as datafile:
            category = datafile.read(1)
            while test_iterator < end:
                if not category:
                    self.processHourlyData(self.currHour, self.hourlyData)  # for the last hour.
                    print("Reached EOF!")
                    break;

                if(category in sectionSizeDictionary):
                    message = datafile.read(sectionSizeDictionary[category] - 1)
                    self.processMessage(category, message)
                    self.processed += 1
                    if(self.processed % (10000000) == 0):
                        print("Processed", self.processed / (1000000), "M message records")

                if(test_iterator == end-1):
                    self.processHourlyData(self.currHour, self.hourlyData)  # for the last hour.
                    break;

                category = datafile.read(1)
                # test_iterator += 1

        datafile.close()
        print("Total Records saved in results folder:", self.records)

    def test(self):
        samplesMessage = [
                b'\x1f\x07\x00\x02\r\x18\xce\xcd\xd8\xa3\x00\x00\x00\x00\x00\x00\x00\x00B\x00\x00\x00\x01UGAZ    \x00\x05\xf9\xb0\x00\x00\x00\x00\x00\x00D\x11', 
                b'\x1c{\x00\x02\r\x19\xd92)8\x00\x00\x00\x00\x00\x00\x00\x00B\x00\x00\x00\xc8SPY     \x00(X \x00\x00\x00\x00\x00\x00D\x18', 
                b'\x01}\x00\x04\r#\xbf\xe4\xecc\x00\x00\x00\x00\x00\x00\x00\x00B\x00\x00\x00\x10AMZN    \x00\xf6;\x8c\x00\x00\x00\x00\x00\x00D%', 
                b'\x1c{\x00\x02\r#\xc6y\xa4\x1d\x00\x00\x00\x00\x00\x00\x00\x00B\x00\x00\x007SPY     \x00(N\\\x00\x00\x00\x00\x00\x00D&', 
                b'\x00\x0e\x00\x02\r%\xa7\xe3ip\x00\x00\x00\x00\x00\x00\x00\x00B\x00\x00\x00(AAPL    \x00\x18\xd4@\x00\x00\x00\x00\x00\x00D)'
            ]
        for msg in samplesMessage:
            self.processMessage(b'P', msg)

        print(len(self.hourlyData))
        self.processHourlyData(self.currHour, self.hourlyData)
        # [print(x) for x in self.hourlyData]

"""
b'P': [
    b'\x1f\x07\x00\x02\r\x18\xce\xcd\xd8\xa3\x00\x00\x00\x00\x00\x00\x00\x00B\x00\x00\x00\x01UGAZ    \x00\x05\xf9\xb0\x00\x00\x00\x00\x00\x00D\x11', 
    b'\x1c{\x00\x02\r\x19\xd92)8\x00\x00\x00\x00\x00\x00\x00\x00B\x00\x00\x00\xc8SPY     \x00(X \x00\x00\x00\x00\x00\x00D\x18', 
    b'\x01}\x00\x04\r#\xbf\xe4\xecc\x00\x00\x00\x00\x00\x00\x00\x00B\x00\x00\x00\x10AMZN    \x00\xf6;\x8c\x00\x00\x00\x00\x00\x00D%', 
    b'\x1c{\x00\x02\r#\xc6y\xa4\x1d\x00\x00\x00\x00\x00\x00\x00\x00B\x00\x00\x007SPY     \x00(N\\\x00\x00\x00\x00\x00\x00D&', 
    b'\x00\x0e\x00\x02\r%\xa7\xe3ip\x00\x00\x00\x00\x00\x00\x00\x00B\x00\x00\x00(AAPL    \x00\x18\xd4@\x00\x00\x00\x00\x00\x00D)'
] 
"""