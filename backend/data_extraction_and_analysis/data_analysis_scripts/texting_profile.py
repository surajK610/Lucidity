import numpy as np
from datetime import datetime as dt
import datetime
import pandas as pd

import sys

from pytz import country_names
# sys.path.append("../")
from data_extraction_and_analysis.data_analysis_scripts.message_extraction import get_sent_messages
import statistics as s
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

from collections import Counter
from wordcloud import STOPWORDS

def get_avg_msg_length(textDf):
    '''
    want to count each emoji as a character?
    '''
    # _, total_emojis = ee.get_most_popular_emojis(textDf)
    sent_only = get_sent_messages(textDf)
    msg_lengths = 0
    for message in sent_only.message:
        msg_lengths += (len(message.split()))
    return "{:.2f}".format((msg_lengths)/len(sent_only))

def get_total_sent_messages(textDf):
    sent_only = get_sent_messages(textDf)
    return len(sent_only)

def get_avg_messages_sent_per_day(textDf):
    sent_only = get_sent_messages(textDf)
    # get unique days
    sent_dates = set([dt(1970, 1, 1) + datetime.timedelta(milliseconds=time_ms) for time_ms in sent_only.time])
    return "{:.2f}".format(len(sent_only)/len(sent_dates))

def conversation_init_freq(textDf):
    '''
    a conversation is when someone sends a message after 24 hours of inactivity
    a conversation is initated either when you receive a message
        found by a 24 hour gap between two messages
    how to define a conversation? 
    '''
    conversations_initiated = 0
    total_conversations = 0
    contacts = textDf.contact.unique()

    for contact in contacts:
        contact_df = textDf[textDf.contact == contact]
        contact_df.reset_index(drop=True, inplace=True)
        # need case where only 1 message is sent
        if len(contact_df) == 1:
            total_conversations += 1
            if contact_df.loc[0,"sent or rec"] == "sent":
                conversations_initiated += 1
        else:
            for i in range(len(contact_df)-1):
                # try:
                time1 = contact_df.loc[i, "time"]
                time2 = contact_df.loc[i+1, "time"]
                timeGap = (time1 - time2) // 1000
                if (timeGap > 24*3600):
                    total_conversations += 1
                    if contact_df.loc[i, "sent or rec"] == "sent":
                        conversations_initiated += 1
                # except:
                #     print("improper date format")
    return "{:.2f}".format(100*conversations_initiated/total_conversations) + "%"

def message_sentiment(textDf):
    sent_only = get_sent_messages(textDf)
    messages = list(sent_only['message'])

    # print(sent_only.head())

    analyzer = SentimentIntensityAnalyzer()
    num_pos = 0
    num_neu = 0
    num_neg = 0
    for sentence in messages:
        vs = analyzer.polarity_scores(sentence)
        if vs["compound"] >= 0.05:
            num_pos += 1
        elif vs["compound"] <= -0.05:
            num_neg += 1
        else:
            num_neu += 1
        # print("{:-<65} {}".format(sentence, str(vs)))
    sent_freqs = 100*np.array([num_pos, num_neu, num_neg])/len(messages)
    sent_freqs = ["{:.2f}".format(n) + "%" for n in sent_freqs]
    return {'positive': sent_freqs[0], 'neutral':sent_freqs[1], 'negative':sent_freqs[2]}


def get_most_freq_words(textDf):
    sent_only = get_sent_messages(textDf)
    allWords = []
    stopwords = set(STOPWORDS)
    for msg in sent_only.message:
        as_list = msg.split(" ")
        for w in as_list:
            if w.lower() not in stopwords:
                allWords.append(w.lower())

        # as_list = [w.lower() for w in as_list if w.lower() not in stopwords]
        # allWords += as_list
    c = Counter(allWords)
    # mess around with how many words are returned
    most_common_words = c.most_common(150)
    return [{'text': p[0], 'value': p[1]} for p in most_common_words]

def main():
    # titles = ["time", "sent or rec", "message", "contact"]
    textDf = pd.read_csv("../../data/facebook_data/outputs/combined.csv")

    init_freq = conversation_init_freq(textDf)
    print(init_freq)

    avg_msg_len = get_avg_msg_length(textDf)
    print(avg_msg_len)

    sentiment = message_sentiment(textDf)
    print(sentiment)

    
if __name__ == "__main__":
    main()
