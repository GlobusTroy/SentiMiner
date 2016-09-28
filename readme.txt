#SentiMiner

To execute, run mining.py from the terminal

By default, the program will listen indefinitely for incoming tweets with the keyword(s) specified in mining.py

The output will be a csv file.  It will be named <Timestamp of first tweet collected>.csv
CSV file information is returned in the following format:
        ID, text, isVerified, #retweets, #favorites, #followers, sentiment, #capitals, # of !, # of ?, #emoticons

How to set a tweet limit before disconnecting:
	-in mining.py, go to the line which instantiates MineListener
		--listener = MineListener()
	-add an argument tweet_limit
		--ex: listener = MineListener(tweet_limit = 10)  
	-now after 10 tweets are gathered and sent to the csv file, the stream will disconnect

How to specify what keywords to search for in mining.py as well
	-in mining.py, go to the line where the stream starts running
		--stream.filter(track = ["party"])
	-add items to the list which track is set to
		--ex: --stream.filter(track = ["party","feelings","fun"]) 
	-now all the specified keywords will be included in the search




