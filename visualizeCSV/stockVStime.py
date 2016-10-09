import csv
from yahoo_finance import Share
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from matplotlib.finance import candlestick_ohlc
import pandas as pd
import plotly.plotly as py
from plotly.tools import FigureFactory as figf



#def getCompany(company):
#   targetCompany = Share(company)

def getCompanyHistoricalStock(company):
#   output = open(company,'r')
#   data = output.read()
#   output.close()
#   output = open('stock'+startDate+'-'+endDate+'.csv','a')
#   output.write(targetCompany.get_historical(startDate,endDate)
#   output.close()
#   print targetCompany.get_historical(startDate, endDate)

#   rows = []
#   with open(company,'r') as csvfile:
#       reader = csv.reader(csvfile)
#       rows = list(reader)
#   return rows[1:5]
    df = pd.read_csv(company,index_col=0)
    fig = figf.create_candlestick(df['OPEN'],df['HIGH'],df['LOW'],df['CLOSE'],dates=df.index)
    py.plot(fig,filename=company,validate=False)
#   plt.legend()
#   plt.show()
#   print df.head()

def graphStock(stock):
    #http://docs.scipy.org/doc/numpy/reference/generated/numpy.loadtxt.html
    ohlc = []
    for rows in stock:
        ohlc.append([rows[0]]+[float(rows[i]) for i in xrange(1,5)])
#   print ohlc
    ax = plt.subplot2grid((1,1),(0,0))
    #http://matplotlib.org/api/finance_api.html
    candlestick_ohlc(ax, ohlc, width=0.4, colorup='g', colordown='r')
#   plt.xlabel('Date')
#   plt.ylabel('Price')
#   plt.title(company_stock)
#   plt.legend()
#   plt.show()

