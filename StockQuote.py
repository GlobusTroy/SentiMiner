import urllib, time, datetime, csv
from time import strftime

class StockQuote(object):
    DATE_FMT = '%Y-%m-%d'
    TIME_FMT = '%H:%M:%S'
    TIMESTAMP_FMT = '%m-%d-%Y %H:%M:%S' #Change is actual format of Tweet Timstamp is different

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

    def getDataAtTimes(self, timestampArr):
        for timestamp in timestampArr:
            print(self.getDataAtTime(timestamp))

    def getDataAtTime(self, timestamp):
        dt = datetime.datetime.fromtimestamp(timestamp)
        try:
            index = self.timestamp.index(timestamp)
            return "At {0}, {1} opened at {2} and closed at {3}".format(dt,
                    self.symbol, self.open_[index], self.close[index])
        except ValueError:
            return "Stock information not found at time: " + str(dt)

    def readTweetCSV(self, fileName):
        timestampArr = []
        firstLine = True;
        for line in open(fileName, 'r'):
            if firstLine:
                firstLine = False
                continue
            tokens = line.rstrip().split(',')
            timeStr = tokens[0].strip() # Change hardcoded magic number
            timestampArr.append(self.convertToTimestamp(timeStr))
        return timestampArr

    def convertToTimestamp(self, timeStr):
        return int(time.mktime(datetime.datetime.strptime(timeStr, self.TIMESTAMP_FMT).timetuple()))
