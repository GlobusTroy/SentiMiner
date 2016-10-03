from StockQuote import*

class GoogleQuote(StockQuote):
    def __init__(self, symbol, intervalSeconds=120, numDays=7):
        super(GoogleQuote,self).__init__()
        self.symbol = symbol.upper()
        urlString = "http://www.google.com/finance/getprices?q="
        urlString += "{0}&i={1}&p={2}d&f=d,o,h,l,c,v".format(self.symbol, intervalSeconds, numDays)
        csvData = urllib.urlopen(urlString).readlines()
        for element in xrange(7, len(csvData)):
            if (csvData[element].count(',') != 5):
                continue
            offset, close, high, low, open_, volume = csvData[element].split(',')
            if (offset[0] == 'a'):
                day = float(offset[1:])
                offset = 0
            else:
                offset = float(offset)
            open_, high, low, close = [float(i) for i in [open_,high,low,close]]
            timestamp = day + (intervalSeconds*offset)
            dateTime = datetime.datetime.fromtimestamp(timestamp)
            self.append(timestamp, dateTime, open_, high, low, close, volume)
