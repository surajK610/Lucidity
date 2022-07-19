# necessary imports
from pickle import GLOBAL
from pprint import pprint
from random import random
from flask import Flask, redirect, url_for, request
from numpy import full
from pymongo import MongoClient
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
from bson import ObjectId
import os
import shutil
import sys
import certifi
import urllib
import bcrypt

sys.path.append('.')
sys.path.append('data_extraction_and_analysis/data_analysis_scripts')
sys.path.append('data_extraction_and_analysis')

from data_extraction_and_analysis.file_extraction import extract_files
from data_extraction_and_analysis.data_analysis_scripts.full_user_analysis import analyze_user

# make flask object
app = Flask(__name__)
cors = CORS(app)

# load env variables
load_dotenv()

# important initializations for the app
app.config['CORS_HEADERS'] = 'Content-Type'
UPLOAD_FOLDER = os.getcwd() + "/data/facebook_data/facebook_zipped"
ALLOWED_EXTENSIONS = {'txt', 'zip'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# currently 16 MB, can be increased if needed
app.config['MAX_CONTENT_LENGTH'] = 300 * 1000 * 1000
FILE_PATH = ''
DATA_LIST = []

CONVO_DF = None

# connect to mongo atlas cluster
db_usr, db_pswrd = os.getenv('ATLAS_USERNAME'), os.getenv('ATLAS_PASSWORD')
uri = f'mongodb+srv://{urllib.parse.quote(db_usr)}:{urllib.parse.quote(db_pswrd)}@cluster0.ovkaf.mongodb.net/lucidity?retryWrites=true&w=majority'
client = MongoClient(uri, tlsCAFile=certifi.where())

db = client.lucidity.users

wrappedStatistics = client.lucidity.wrappedStatistics

# function to check file type
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Handler for getting data
@app.route('/getstats')
def getstats():
    global DATA_LIST
    user_id = request.json.args('user_id')
    user_data = wrappedStatistics.find_one({'UserID': user_id})
    user_data['dataList'] = DATA_LIST

    return user_data

# Handler for file upload
@app.route('/upload', methods=['POST'])
def upload():
    global FILE_PATH
    file = request.files['inputFile']
    filename = secure_filename(file.filename)
    if file:
        FILE_PATH = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(FILE_PATH)
        return 'File uploaded', '200'
    else:
        return 'File not uploaded', '400'


@app.route('/analysistypes', methods=['POST'])
def analysistypes():
    global DATA_LIST
    global FILE_PATH
    DATA_LIST = request.json.get('dataList')
    # For Testing purposes
    # DATA_LIST = [
    #     'emoji', 'messaging_profile', 'response_time', 'emotions',
    #     'topics', 'personality', 'celeb_matches', 'word_freqs'
    #     ]

    user_id = request.json.get('userID')
    print(DATA_LIST)
    print(user_id)
    print(FILE_PATH)
    CONVO_DF = extract_files(FILE_PATH)
    # user_id = max(wrappedStatistics.distinct('UserID')) + 1
    user_stats = analyze_user(CONVO_DF, user_id, DATA_LIST)
    # print(user_stats)
    del CONVO_DF
    os.remove(FILE_PATH)
    user_id = str(user_stats['UserID'])
    print("user_id", user_id)
    
    user = db.find_one({ '_id': ObjectId(user_id) })

    if user is None:
        return 'User registered but failed to load', 400

    print("ID AS STRING:", str(user['_id']))

    stats = wrappedStatistics.find_one({ 'UserID': user_id })
    print("stats:", stats)

    if stats is not None:
        user.update(stats)

    user['_id'] = str(user['_id'])
    del user['password']
    return user, 200
    
@app.route('/user', methods=['POST'])
def create_account():
    name = request.json.get('name')
    email = request.json.get('email')
    password = request.json.get('password')

    if name is None or email is None or password is None:
        return 'Requires name, email, and password', 400

    if db.find_one({ 'email': email }) is not None:
        return 'Email already exists', 400

    if len(password) < 6:
        return 'Password must be 6+ characters', 400

    encoded_password = password.encode('utf-8')
    hashed_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt(10)) 

    new_user = { 'name': name, 'email': email, 'password': hashed_password }
    insertion_res = db.insert_one(new_user)
    
    if insertion_res.acknowledged:
        user = db.find_one({ 'email': email })

        if user is None:
            return 'User registered but failed to load', 400

        stats = wrappedStatistics.find_one({ 'UserID': user['_id'] })

        if stats is not None:
            user.update(stats)

        user['_id'] = str(user['_id'])
        del user['password']
        return user, 200
    
    return 'Insertion failed', 400

@app.route('/user/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')

    if email is None or password is None:
        return 'Requires email and password', 400

    user = db.find_one({ 'email': email })

    if user is None:
        return 'User registered but failed to load', 400

    encoded_password = password.encode('utf-8')

    if not bcrypt.checkpw(encoded_password, user['password']):
        return 'Incorrect password', 400

    stats = wrappedStatistics.find_one({ 'UserID': user['_id'] })
    
    if stats is not None:
        user.update(stats)

    user['_id'] = str(user['_id'])
    del user['password']
    return user, 200

@app.route('/test')
def test_function():
    response_body = {
        "name": "Test",
        "about": "This is a test for my Flask integration"
    }
    return response_body
