import nltk, csv
from nltk.tokenize import sent_tokenize, word_tokenize 

path = '2016-10-03 08:07:52.csv'
with open(path, 'rb') as csvfile:
	reader = csv.reader(csvfile)
	for line in reader:
		line = ' '.join(line)
		tokens = word_tokenize(line)
		tagged = nltk.pos_tag(tokens)
		print tagged
