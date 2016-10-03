from GoogleQuote import*
import time, os

if __name__ == '__main__':
    stockTicker = 'AAPL'
    intervalInSeconds = 3600 # (3600 seconds = 1 hour)
    periodInDays = 1

    q = GoogleQuote(stockTicker, intervalInSeconds, periodInDays)
    print(q) # Print the extracted data to terminal

    # Get the opening and closing price at 1475244000 (1475244000 = 09/30/2016 10:00:00 AM EST)
    # To convert from UNIX timestamps to "normal" time, use http://www.convert-unix-time.com/
    # Please make sure that the timezone is Eastern Standard (EST) since the NYSE operates on EST
    print(q.getPriceAtTime(1475244000))

    ''' To write the extracted data to a CSV file, uncomment the next two lines'''
    #fileName = os.getcwd() + '/output/' + time.strftime('%Y-%m-%d %H:%M:%S') + ".csv"
    #q.writeCSV(fileName)
