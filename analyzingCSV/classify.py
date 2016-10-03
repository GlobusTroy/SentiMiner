import nltk
import random
from nltk.corpus import movie_reviews

documents = []

for category in data.categories():
	for fileid in data.fileids(category):
		documents.append(list(data.words(fileid)), category)

random.shuffle(documents)


