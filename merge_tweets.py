import glob

companies = ['AAPL','FB','GOOG','MSFT','TSLA','TWTR']

for company in companies:
    files = glob.glob('Tweet Data/%s*.csv' % company)
    with open('Tweet Data/%s.csv' % company, 'w') as outfile:
        for file in files:
            with open(file, 'r') as csvfile:
                outfile.write(csvfile.read())
                outfile.write('\n')
