import pandas as pd
import numpy as np
import sys
import os
import certifi
from data_analysis_scripts.similarityIndexer import SimilarityIndexer
# sys.path.append("../")
from data_extraction_and_analysis.data_analysis_scripts.personality_analysis import get_mbti_personality
from data_extraction_and_analysis.data_analysis_scripts.emotion_analysis import get_most_common_emotions
from data_extraction_and_analysis.data_analysis_scripts.topic_analysis import get_most_common_topics
from data_extraction_and_analysis.data_analysis_scripts import similarityIndexer

from pymongo import MongoClient
from sklearn.preprocessing import MultiLabelBinarizer
from collections import OrderedDict as od
import os

import csv

features = ['Joy','Sadness','Anger','Fear','Love','Surprise']
features += [
    'Politics','Love','Heavy Emotion','Health','Animals','Science',
    'Joke','Compliment','Religion','Self','Education'
    ]
features += ['I','E','S','N','T','F','J','P']

one_hot = MultiLabelBinarizer()

one_hot.fit([features])

'''
Next steps:
    1. try celeb extraction with the dataframe.
    2. insert user data into a dataframe
    3. work with vignesh to get it working with the database (mongoDB)
'''

# MAYBE HAVE THIS TAKE IN  A ONE HOT ENCODER?
def calc_celeb_scores(celeb_csv):
    '''
    For each celebrity, we want to compute their personality, message topics, and emotions 
    and store these values in a database
    '''
    # initializing client
    # client = MongoClient()

    # # # Connect to the db
    # db=client.termProjectDB

    # celebStatistics = db.celebStatistics

    all_tweets = pd.read_csv(celeb_csv)
    all_tweets['sent or rec'] = ['sent' for i in range(len(all_tweets))]

    # features = []
    # features += ['Joy','Sadness','Anger','Fear','Love','Surprise']
    # features += ['Politics','Love','Heavy Emotion','Health','Animals','Science','Joke','Compliment','Religion','Self','Education']
    # features += ['I','E','S','N','T','F','J','P']

    # one_hot = MultiLabelBinarizer()

    # one_hot.fit([features])

    celeb_dict = {}
    i = 0
    
    celeb_names = all_tweets.name.unique()
    for celeb_name in celeb_names:
        # getting tweets from this celebrity
        celeb_df = all_tweets[all_tweets.name  == celeb_name] 
        # getting celeb personality
        personality = get_mbti_personality(celeb_df)
        # getting celeb emotions
        emo_model_loc =  "classification_models/emotion_classifier_linearSVC_V2.sav"
        emotions, emo_freqs = get_most_common_emotions(celeb_df, emo_model_loc)
        # getting celeb topics'
        topic_model_loc = "classification_models/topic_classifier_linearSVC.sav"
        topics, topic_freqs = get_most_common_topics(celeb_df, topic_model_loc)

        celeb_features = emotions[:3] + topics[:5] + list(personality)
        
        celeb_features_one_hotted = one_hot.transform([celeb_features])
        feature_dict = dict(zip(one_hot.classes_,celeb_features_one_hotted[0]))
        feature_dict['name'] = celeb_name

        celeb_dict[i] = feature_dict
        i += 1
        if i % 20 == 0:
            print(i)

        # result = celebStatistics.insert_one(feature_dict)

        # NEED TO MAKE AN INSERTION INTO THE DATABASE
        # take the top three emotions, top 5 topics, personality 
        # 6: ['Joy','Sadness','Anger','Fear','Love','Surprise']
        # 11: ['Politics','Love','Heavy Emotion','Health','Animals','Science','Joke','Compliment','Religion','Self','Education']
        # 8: ['I','E','S','N','T','F','J','P']
        # maybe we ought to have them as one hotted vectors of length 25
        
        # INSERT INTO A DATAFRAME FIRST
    celeb_df = pd.DataFrame.from_dict(celeb_dict, "index")
    output_path = '../../data/celeb_data.csv'
    celeb_df.to_csv(output_path, index=False)
    return

def upload_to_mongo():

    db_usr, db_pswrd = os.getenv('ATLAS_USERNAME'), os.getenv('ATLAS_PASSWORD')
    uri = f'mongodb+srv://{db_usr}:{db_pswrd}@cluster0.ovkaf.mongodb.net/lucidity?retryWrites=true&w=majority'
    client = MongoClient(uri, tlsCAFile=certifi.where())
    db = client.lucidity.celebData

    dict_from_csv = {}

    with open('/Users/neilxu/Documents/cs32/term-project-abao5-dgrossm5-nxu4-onaphade-sanand14-vpandiar/data/celeb_data.csv', mode='r') as inp:
        reader = csv.reader(inp)
        dict_from_csv = {rows[0]:rows[1] for rows in reader}

    print(dict_from_csv)


    for key in dict_from_csv:
        result = db.insert_one(dict_from_csv[key])


def get_celeb_matches(user_id):
    '''
    for a given user, we want to compute a score with each celebrity and return
    the top 3 celebrities whose scores match the most. 

    assume it's one hotted stuff
    '''

    # # initializing client
    db_usr, db_pswrd = os.getenv('ATLAS_USERNAME'), os.getenv('ATLAS_PASSWORD')
    uri = f'mongodb+srv://{db_usr}:{db_pswrd}@cluster0.ovkaf.mongodb.net/lucidity?retryWrites=true&w=majority'
    client = MongoClient(uri, tlsCAFile=certifi.where())
    # Connect to the db
    db=client.lucidity
    userMatchingData = db.userMatchingData
    celebData = db.celebData

    Queryresult = userMatchingData.find_one({'userID': user_id})
    user_vector = list(Queryresult.values())[1:-1]

    celebs = celebData.distinct('name')
    scores = []
    for celeb_name in celebs:
        # celeb_info = celeb_stats[celeb_stats.name == celeb_name].values.tolist()
        celeb_info = celebData.find_one({'name': celeb_name})
        celeb_vec = [int(e) for e in list(celeb_info.values())[1:-1]]
        # celeb_vec = celeb_info[0][:-1]
        score = get_percent_similarity(user_vector, celeb_vec) # we are passing in two bit vectors
        # print(score)
        scores.append((score*100, celeb_name))

    scores.sort(reverse=True)

    return [
        {
            'name': p[1], 
            'matchPercent': "{:.2f}".format(p[0]) + '%', 
            'imgPath': p[1].replace(" ", "_") + '.png'
            } for p in scores[:3]]

def get_percent_similarity(vec1, vec2):
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    sim_indexer = SimilarityIndexer(vec1, vec2)
    return sim_indexer.get_similarity("percent similarity")
    # return np.mean(vec1 == vec2)

def main():
    # calc_celeb_scores('../../data/celeb_tweets.csv')
    upload_to_mongo()
    # print(get_celeb_matches(65396))

if __name__ == "__main__":
    main()








