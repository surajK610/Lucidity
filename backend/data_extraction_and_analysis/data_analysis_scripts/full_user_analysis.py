import pandas as pd
import numpy as np
from sklearn.preprocessing import MultiLabelBinarizer
import csv
from pymongo import MongoClient
import os
import certifi

import sys
# sys.path.append('../')
from data_extraction_and_analysis.data_analysis_scripts.emotion_analysis import get_most_common_emotions
from data_extraction_and_analysis.data_analysis_scripts.emoji_analysis import get_most_popular_emojis, get_fav_emoji_by_contact, get_emoji_frequency
from data_extraction_and_analysis.data_analysis_scripts.texting_profile import conversation_init_freq, get_avg_msg_length, message_sentiment, get_most_freq_words
from data_extraction_and_analysis.data_analysis_scripts.texting_profile import get_total_sent_messages, get_avg_messages_sent_per_day
from data_extraction_and_analysis.data_analysis_scripts.response_analysis import get_mean_response_time, get_top_five_times
from data_extraction_and_analysis.data_analysis_scripts.topic_analysis import get_most_common_topics
from data_extraction_and_analysis.data_analysis_scripts.personality_analysis import get_mbti_personality
from data_extraction_and_analysis.data_analysis_scripts.celeb_matches import get_celeb_matches

# from emotion_analysis import get_most_common_emotions
# from emoji_analysis import get_most_popular_emojis, get_fav_emoji_by_contact, get_emoji_frequency
# from texting_profile import conversation_init_freq, get_avg_msg_length, message_sentiment
# from response_analysis import get_mean_response_time, get_top_five_times
# from topic_analysis import get_most_common_topics
# from personality_analysis import get_mbti_personality
# from celeb_matches import get_celeb_matches

def analyze_user(textDf, userID, data_list):

    # db_usr, db_pswrd = os.getenv('ATLAS_USERNAME'), os.getenv('ATLAS_PASSWORD')
    # print(f'user is {db_usr}')
    # print(f'password is {db_pswrd}')
    # client = MongoClient(f'mongodb+srv://cs32FinalProject:{db_pswrd}@cluster0.ovkaf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
    # db = client['lucidity']['users']

    db_usr, db_pswrd = os.getenv('ATLAS_USERNAME'), os.getenv('ATLAS_PASSWORD')
    uri = f'mongodb+srv://{db_usr}:{db_pswrd}@cluster0.ovkaf.mongodb.net/lucidity?retryWrites=true&w=majority'
    client = MongoClient(uri, tlsCAFile=certifi.where())
    db = client.lucidity

    userMatching = db.userMatchingData
    wrappedStatistics = db.wrappedStatistics

    fav_emojis, contact_emojis = None, None
    msg_frequency, init_freq, avg_msg_len, sentiment = None, None, None, []
    total_messages = None
    msgs_per_day = None
    mean_res_time, top_times = None, None
    emotions, emo_freqs = [], []
    topics, topic_freqs = [], []
    personality = None
    celeb_matches = None
    word_freqs = None

    if 'emoji' in data_list:
        fav_emojis, total_emojis = get_most_popular_emojis(textDf)
        contact_emojis = get_fav_emoji_by_contact(textDf)
    if 'messaging_profile' in data_list:
        init_freq = conversation_init_freq(textDf)
        avg_msg_len = get_avg_msg_length(textDf)
        sentiment = message_sentiment(textDf)
        total_messages = get_total_sent_messages(textDf)
        msgs_per_day = get_avg_messages_sent_per_day(textDf)
    if 'word_freqs' in data_list:
        word_freqs = get_most_freq_words(textDf)
    if 'response_time' in data_list:
        mean_res_time, _ = get_mean_response_time(textDf, True)
        top_times = get_top_five_times(textDf)
    if 'emotions' in data_list:
        emotions, emo_freqs = get_most_common_emotions(textDf)
        emos_zipped = list(zip(emotions, emo_freqs))
        emo_freqs = [{'emotion': p[0], 'frequency':100 * p[1]} for p in emos_zipped]
    if 'topics' in data_list:
        topics, topic_freqs  = get_most_common_topics(textDf)
        topics_zipped = list(zip(topics,topic_freqs))
        topic_freqs = [{'topic': p[0], 'frequency': 100 * p[1]} for p in topics_zipped]
    if 'personality' in data_list:
        personality = get_mbti_personality(textDf)
    if 'celeb_matches' in data_list:
        features = ['Joy','Sadness','Anger','Fear','Love','Surprise']
        features += [
            'Politics','Love','Heavy Emotion','Health','Animals','Science',
            'Joke','Compliment','Religion','Self','Education'
            ]
        features += ['I','E','S','N','T','F','J','P']

        one_hot = MultiLabelBinarizer()
        one_hot.fit([features])
        if (len(emotions) == 0) or (len(topics) == 0) or (personality == None):
            emotions, _ =  get_most_common_emotions(textDf)
            topics, _  = get_most_common_topics(textDf)
            personality = get_mbti_personality(textDf)

            user_features = emotions[:3] + topics[:5] + list(personality)

            emotions = []
            topics = []
            personality = None
        else:
            user_features = emotions[:3] + topics[:5] + list(personality)

        user_features_one_hot = one_hot.transform([user_features]).tolist()[0]

        features_for_insertion = dict(zip(one_hot.classes_, user_features_one_hot))
        features_for_insertion['userID'] = userID

        # Use the insert method
        result = userMatching.insert_one(features_for_insertion)
        celeb_matches = get_celeb_matches(userID)


    # make an insertion into wrappedStatistics
    toInsert = {
        'avgResponseTime' : mean_res_time,
        'contactResTimes' : top_times,
        'avgTextLength' : avg_msg_len,
        'msgFreqDay' : msg_frequency,
        'convoInitFreq' : init_freq,
        'msgSentiment' : sentiment,
        'totalMessages' : total_messages,
        'messagesPerDay' : msgs_per_day, 
        'favEmojis' : fav_emojis,
        'emojisByContact' : contact_emojis,
        'emotions' : emo_freqs,
        'topics' : topic_freqs, 
        'personality' : personality,
        'celebMatches' : celeb_matches,
        'wordFreqs' : word_freqs,
        'UserID' : userID,
        'dataList' : data_list  
    }

    wrappedStatistics.delete_many({ 'UserID': userID })

    result = wrappedStatistics.insert_one(toInsert)
    return toInsert

def main():
    textDf = pd.read_csv("../../data/facebook_data/outputs/combined.csv")
    analyze_user(textDf, 12,[])


if __name__ == "__main__":
    main()