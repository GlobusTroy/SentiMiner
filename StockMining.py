from GoogleQuote import*
import time, os

if __name__ == '__main__':
    stockTicker = 'AAPL'
    intervalInSeconds = 3600 # (3600 seconds = 1 hour)
    periodInDays = 1

    q = GoogleQuote(stockTicker, intervalInSeconds, periodInDays)
    print(q) # Print the extracted data to terminal

    ''' To write the extracted data to a CSV file, uncomment the next two lines'''
    #fileName = os.getcwd() + '/output/' + time.strftime('%Y-%m-%d %H:%M:%S') + ".csv"
    #q.writeCSV(fileName)
