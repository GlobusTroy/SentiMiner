from afinn import Afinn
from collections import Counter
import pandas as pd

class gen_training_set(object):
    """docstring for gen_training_set."""
    def __init__(self, filename):
        self.filename = filename

    def clean_data(self):
        df = pd.read_csv(self.filename + ".csv",low_memory=False)
        keys = df.columns

        afinn = Afinn(emoticons=True)


        df_2 = pd.DataFrame()

        df_2.insert(0,"Date",0)
        df_2.insert(1,"Tweet","")
        df_2.insert(2,"Sentiment_Score",0)

        for i in range(0,len(df)):
            date = df.get_value(i,keys[1])
            tweet = df.get_value(i,keys[6])
            if isinstance(date,float) or isinstance(tweet,float):
                continue
            Sentiment_Score = afinn.score(tweet)

            df_2.set_value(i,"Date",date)
            df_2.set_value(i,"Tweet",repr(tweet))
            df_2.set_value(i,"Sentiment_Score",Sentiment_Score)

        df_2.to_csv(self.filename + "_info.csv", sep=',')

    def format_date(self,date):
        date = date.replace("-","/")
        date_split = date.split("/")
        date = date_split[2] + "/" + date_split[1] + "/" + date_split[0][2:]

        return date

    def make_training_set(self):
        stock_df = pd.read_csv(self.filename+"/"+self.filename +"_stock.csv",low_memory=False)
        keys  = stock_df.columns

        dates_to_stock = {}

        #stock data
        for i in range(0,len(stock_df)):
            date = stock_df.get_value(i,keys[1])
            if "-" in date:
                date = format_date(self,date)
            elif self.filename == "FB":
                date_split = date.split("/")
                date = date_split[1] + "/" + date_split[0] + "/" + date_split[2]

            opening = stock_df.get_value(i,keys[3])
            closing = stock_df.get_value(i,keys[6])
            dates_to_stock[date] = abs(opening-closing)

        #Senitment scores and Tweets
        df = pd.read_csv(self.filename+"/"+self.filename+"_info.csv",low_memory=False)
        info_keys = df.columns

        dates_to_scores = {}

        prev_date = df.get_value(0,info_keys[1])
        sentiments = []



        for i in range(0,len(df)):
            date = df.get_value(i,info_keys[1])
            score = float(df.get_value(i,info_keys[3]))

            if prev_date!=date:
                #aggregate all data for that day
                prev_date = self.format_date(prev_date)
                data = Counter(sentiments)
                dates_to_scores[prev_date] = [data.most_common(1)[0][0],round(sum(sentiments)/len(sentiments),0)]#[mod,average sentiment]
                sentiments = []
                sentiments.append(score)
            else:
                #don't consider sentiment with scores of zero
                if score!=0.0:
                    sentiments.append(score)
            prev_date = date

        #New dataframe
        df_2 = pd.DataFrame()

        df_2.insert(0,"Date",0)
        df_2.insert(1,"Mod Score",0)
        df_2.insert(2,"Average Score",0)
        df_2.insert(3,"Stock Price",0)

        keys = dates_to_scores.keys()
        ctr = 0
        for i in range(0,len(keys)):
            try:

                d = [int(x) for x  in keys[i].split("/")]
                d[0] = d[0] + 1

                if d[0] > 30:
                    d[0] = 1
                    d[1] = d[1] + 1
                nxt_date = str(d[0]) + "/0" + str(d[1]) + "/" + str(d[2])
                vals = dates_to_scores[nxt_date]
                dates_to_stock_value = dates_to_stock[keys[i]]
                df_2.set_value(i,"Date",keys[i])
                df_2.set_value(i,"Mod Score",vals[1])
                df_2.set_value(i,"Average Score",vals[0])
                df_2.set_value(i,"Stock Price",dates_to_stock_value)
                print keys[i],vals[1],vals[0],dates_to_stock_value
                ctr+=1
            except KeyError:
                pass

        print ctr
        df_2.to_csv(self.filename+"/"+self.filename+"_training_set.csv",sep=",")



obj = gen_training_set("FB")
#obj.clean_data()
obj.make_training_set()
