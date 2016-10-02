#SentiMiner

To extract stock information, run *StockMining.py* from the terminal


To execute, run *mining.py* from the terminal

By default, the program will listen indefinitely for incoming tweets with the keyword(s) specified in *mining.py*

The output will be a csv file.  It will be named <Timestamp of first tweet collected>.csv
CSV file information is returned in the following order:
ID, text, isVerified, #retweets, #favorites, #followers, sentiment, #capitals, # of !, # of ?, #emoticons

1. How to set a tweet limit before disconnecting:
	* In mining.py, go to the line which instantiates MineListener
		* `listener = MineListener()`
	* Add an argument tweet_limit
		* ex: `listener = MineListener(tweet_limit = 10)`
	* Now after 10 tweets are gathered and sent to the csv file, the stream will disconnect
	* Similarly to the above, one can override the path of the file to which the data will be sent
		* ex: `listener = MineListener(csv_path = 'myFile.csv')`

2. How to specify what keywords to search for in mining.py as well
	* In *mining.py*, go to the line where the stream starts running
		* `stream.filter(track = ["party"])`
	* Add items to the list which track is set to
		* ex: `stream.filter(track = ["party","feelings","fun"])`
	* Now all the specified keywords will be included in the search

3. How to extract stock information:
	* In *StockMining.py*, change `stockTicker` to desired stock symbol/ticker
	* Change `intervalInSeconds` to desired time interval in seconds
	* Change `periodInDays` to number of days that you wish to extract the stock info of
	* To write the extracted data to a CSV file, uncomment the final two lines
