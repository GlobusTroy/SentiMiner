import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import nltk
from nltk.tokenize import RegexpTokenizer
import tweepy
import sentiment_mod as sent

style.use("ggplot")
sent_data = {}
for line in data:
	sent_value, confidence = sent.sentiment(line)
	if confidence > .70:
		sent_data[line] = sent_value
def animate(i):
	lines = sent_data.split('\n')
	
	xar = []
	yar = []
	
	x= 0
	y= 0

	for l in lines:
		x += 1 
		if "pos" in l:
			y += 1
		elif "neg" in l:
			y -= 1
		xar.append(x)
		yar.append(y)

	ax1.clear()
	ax1.plot(xar,yar)
ani = animation.FuncAnimation(flg, animate, interval=1000)
plt.show()
