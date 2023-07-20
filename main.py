import os
import time

from processor import TradeProcessor

if __name__ == '__main__':
    startTime = time.time()
    filepath = os.path.join(os.getcwd(), 'data', "01302019.NASDAQ_ITCH50.gz")
    print("Processing file at: ", filepath)

    tradeProcessor = TradeProcessor(filepath)
    tradeProcessor.processFile()
    # tradeProcessor.test()

    endTime = time.time()
    print("Processing completed in", (endTime - startTime), "s")