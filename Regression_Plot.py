import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt

df = pd.read_csv('date_to_ss.csv',header=0)
sentiment = df['Sentiment_Score']
stock_val=df['Stock_Value'] #Change According to Column name in date_to_ss

ax_sent=sns.regplot(x=sentiment,y=stock_val,data=df)
ax_sent.set_title("Stock Value v Sentiment Score")

plt.show()
