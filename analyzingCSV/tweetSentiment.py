import nltk
import random
from nltk.tokenize import word_tokenize


pos = open("","r").read()
neg = open("","r").read()

documents = []

for r in pos.split('\n'):
	documents.append((r,"pos"))

for r in neg.split('\n'):
	documents.append((r,"neg"))

all_words = []

pos_words = word_tokenize(pos)
neg_words = word_tokenize(neg)

for w in pos_words:
	all_words.append(w.lower())

for w in neg_words:
	all_words.append(w.lower())

word_features = list(all_words.keys())[:5000]

def find_features(document):
	words = word_tokenize(document) 
	features = {}
	for w in word_features:
		features[w] = (w in words)
	return features

featuresets = [(find_features(rev),category) for (rev, category) in documents]
random.shuffle(featuresets)

training_set = featuresets[:10000]
testing_set = featuresets[10000:]

