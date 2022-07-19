import pickle
import pandas as pd
# import text_preprocessing
import sys
import os
# sys.path.append('../')
from data_extraction_and_analysis.data_analysis_scripts.text_preprocessing import preprocess_text_sklearn
import numpy as np

def get_most_common_emotions(textDf):
    path_to_dir = os.path.dirname(__file__)

    vector_loc = path_to_dir + "/classification_models/emotion_vectorizer.pickle"
    vectorizer = pickle.load(open(vector_loc, "rb"))
    convertor_loc = path_to_dir + "/classification_models/emotion_convertor.pickle"
    convertor = pickle.load(open(convertor_loc, "rb"))
    data = preprocess_text_sklearn(textDf, vectorizer, convertor)

    model_loc = path_to_dir + '/classification_models/emotion_classifier_linearSVC_V2.sav'

    with open(model_loc, 'rb') as training_model:
        model = pickle.load(training_model)
    preds = model.predict(data)
    emotions = pd.Series(['Joy','Sadness','Anger','Fear','Love','Surprise'])
    bins = [0,1,2,3,4,5,6]
    counts, bins = np.histogram(preds, bins=bins)
    sorted_count_idx = list(np.argsort(-1*counts))
    sorted_counts = -1*np.sort(-1*counts)
    emos = emotions[sorted_count_idx[:5]]
    freqs = sorted_counts[:5]/sum(counts)
    return list(emos), freqs
    
def main():
    # titles = ["time", "sent or rec", "message", "contact"]
    textDf = pd.read_csv("../../data/facebook_data/outputs/combined.csv")
    model_loc =  "classification_models/emotion_classifier_linearSVC_V2.sav"
    preds = get_most_common_emotions(textDf, model_loc)
    print(preds)
if __name__ == "__main__":
    main()