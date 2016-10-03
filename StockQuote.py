import urllib, time, datetime, csv
from time import strftime

class StockQuote(object):
    DATE_FMT = '%Y-%m-%d'
    TIME_FMT = '%H:%M:%S'

    def __init__(self):
        self.symbol = ''
        self.timestamp = []
        self.date = []
        self.time = []
        self.open_ = []
        self.high = []
        self.low = []
        self.close = []
        self.volume = []

    def append(self, timestamp, dateTime, open_, high, low, close, volume):
        self.timestamp.append(int(timestamp))
        self.date.append(dateTime.date())
        self.time.append(dateTime.time())
        self.open_.append(float(open_))
        self.high.append(float(high))
        self.low.append(float(low))
        self.close.append(float(close))
        self.volume.append(int(volume))

    def getPriceAtTime(self, timestamp):
        try:
            index = self.timestamp.index(timestamp)
            return "Open: " + str(self.open_[index]) + ", Close: " + str(self.close[index])
        except ValueError:
            return "Stock information not found for: " + str(datetime.datetime.fromtimestamp(timestamp))

    def getCsvHeader(self):
        return ['Stock Ticker', 'Date', 'Time', 'Open', 'High', 'Low', 'Close', 'Volume']

    def toCSV(self):
        return ''.join(["{0},{1},{2},{3:.2f},{4:.2f},{5:.2f},{6:.2f},{7}\n".format(
                self.symbol, self.date[element].strftime(self.DATE_FMT), self.time[element].strftime(self.TIME_FMT),
                self.open_[element], self.high[element], self.low[element], self.close[element], self.volume[element])
                for element in xrange(len(self.close))])

    def writeCSV(self, fileName):
        with open(fileName, 'w') as file:
            writer = csv.writer(file)
            writer.writerow(self.getCsvHeader())
            file.write(self.toCSV())

    # TODO: Implement Read CSV Function

    def __repr__(self):
        return self.toCSV()
