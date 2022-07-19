from pymongo import MongoClient
import os
import sys 
sys.path.append('../')
# sys.path.append(os.path.join(os.path.dirname(__file__), '../data_extraction_and_analysis/data_analysis_scripts'))

from data_extraction_and_analysis.file_extraction import extract_files
from data_extraction_and_analysis.data_analysis_scripts.full_user_analysis import analyze_user


def main():
    client = MongoClient()

    # Connect to the db
    db=client.termProjectDB
    wrappedStatistics = db.wrappedStatistics

    file_path = '../data/facebook_data/facebook_zipped/facebook-vigneshp20.zip'
    data_list = [
        'emoji', 'messaging_profile', 'response_time', 'emotions',
        'topics', 'personality', 'celeb_matches'
        ]

    CONVO_DF = extract_files(file_path)
    user_id = max(wrappedStatistics.distinct('UserID')) + 1
    user_stats = analyze_user(CONVO_DF, user_id, data_list)

    print(user_stats)

if __name__ == "__main__":
    main()