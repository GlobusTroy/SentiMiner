import nltk, csv
from nltk.tokenize import sent_tokenize, word_tokenize 

path = 'Twitter file'
#read the file and tokenize and tagging the data into POS_TAG:
#Tag 	Meaning 	English Examples
#ADJ 	adjective 	new, good, high, special, big, local
#ADP 	adposition 	on, of, at, with, by, into, under
#ADV 	adverb 	really, already, still, early, now
#CONJ 	conjunction 	and, or, but, if, while, although
#DET 	determiner, article 	the, a, some, most, every, no, which
#NOUN 	noun 	year, home, costs, time, Africa
#NUM 	numeral 	twenty-four, fourth, 1991, 14:24
#PRT 	particle 	at, on, out, over per, that, up, with
#PRON 	pronoun 	he, their, her, its, my, I, us
#VERB 	verb 	is, say, told, given, playing, would
#. 	punctuation marks 	. , ; !
#X 	other 	ersatz, esprit, dunno, gr8, univeristy
with open(path, 'rb') as csvfile:
	reader = csv.reader(csvfile)
	for line in reader:
		line = ' '.join(line)
		tokens = word_tokenize(line)
		tagged = nltk.pos_tag(tokens)
		print tagged

li = ["Apple","Amazon","Disney"]
similar = []
for brand in li:
	if wordnet.synset(brand+".n.01").wup_similarity(wordnet.synset(desired+".n.01"))>.8:
		similar.append(True)
