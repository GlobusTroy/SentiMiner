#SentiMiner

To execute, run *mining.py* from the terminal
To extract stock information, run *StockMining.py* from the terminal

By default, the program will listen indefinitely for incoming tweets with the keyword(s) specified in *mining.py*

The output will be a csv file.  It will be named <Timestamp of first tweet collected>.csv
CSV file information is returned in the following order:
ID, text, isVerified, #retweets, #favorites, #followers, sentiment, #capitals, # of !, # of ?, #emoticons

How to set a tweet limit before disconnecting:
	-in mining.py, go to the line which instantiates MineListener
		--listener = MineListener()
	-add an argument tweet_limit
		--ex: listener = MineListener(tweet_limit = 10)
	-now after 10 tweets are gathered and sent to the csv file, the stream will disconnect
Similarly to the above, one can override the path of the file to which the data will be sent
	-ex: listener = MineListener(csv_path = 'myFile.csv')

How to specify what keywords to search for in mining.py as well
	-in mining.py, go to the line where the stream starts running
		--stream.filter(track = ["party"])
	-add items to the list which track is set to
		--ex: --stream.filter(track = ["party","feelings","fun"])
	-now all the specified keywords will be included in the search

How to extract stock information:
	-in *StockMining.py*, change `stockTicker` to desired stock symbol/ticker
	- change `intervalInSeconds` to desired time interval in seconds
	- change `periodInDays` to number of days that you wish to extract the stock info of
	- to write the extracted data to a CSV file, uncomment the final two lines
