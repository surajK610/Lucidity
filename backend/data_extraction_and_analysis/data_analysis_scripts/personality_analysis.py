import pickle
import pandas as pd
# import text_preprocessing
import sys
# sys.path.append("../")
from data_extraction_and_analysis.data_analysis_scripts.text_preprocessing import preprocess_text_sklearn
import numpy as np
import os

def get_trait(textDf, options, vector_loc, convertor_loc, model_loc):
    vectorizer = pickle.load(open(vector_loc, "rb"))
    convertor = pickle.load(open(convertor_loc, "rb"))
    data = preprocess_text_sklearn(textDf, vectorizer, convertor)

    with open(model_loc, 'rb') as training_model:
        model = pickle.load(training_model)
    preds = model.predict(data)
    prob_1 = np.mean(preds)
    if prob_1 > 0.5:
        return options[1]
    else:
        return options[0]

def get_mbti_personality(textDf):
    path_to_dir = os.path.dirname(__file__)

    IE_vectorizer = path_to_dir + "/classification_models/IE_vectorizer.pickle"
    IE_convertor = path_to_dir + "/classification_models/IE_convertor.pickle"
    IE_model = path_to_dir + "/classification_models/IE_classifier_linearSVC.sav"
    i_or_e = get_trait(textDf, ["E","I"], IE_vectorizer, IE_convertor, IE_model)

    SN_vectorizer = path_to_dir + "/classification_models/SN_vectorizer.pickle"
    SN_convertor = path_to_dir + "/classification_models/SN_convertor.pickle"
    SN_model = path_to_dir + "/classification_models/SN_classifier_MNBayes.sav"
    s_or_n = get_trait(textDf, ["N","S"], SN_vectorizer, SN_convertor, SN_model)

    TF_vectorizer = path_to_dir + "/classification_models/TF_vectorizer.pickle"
    TF_convertor = path_to_dir + "/classification_models/TF_convertor.pickle"
    TF_model = path_to_dir + "/classification_models/TF_classifier_linearSVC.sav"
    t_or_f = get_trait(textDf, ["F","T"], TF_vectorizer, TF_convertor, TF_model)

    JP_vectorizer = path_to_dir + "/classification_models/TF_vectorizer.pickle"
    JP_convertor = path_to_dir + "/classification_models/TF_convertor.pickle"
    JP_model = path_to_dir + "/classification_models/TF_classifier_linearSVC.sav"
    j_or_p = get_trait(textDf, ["P","J"], JP_vectorizer, JP_convertor, JP_model)

    return i_or_e + s_or_n + t_or_f + j_or_p

def main():
    # titles = ["time", "sent or rec", "message", "contact"]
    textDf = pd.read_csv("../../data/facebook_data/outputs/combined.csv")
    preds = get_mbti_personality(textDf)
    print(preds)
if __name__ == "__main__":
    main()