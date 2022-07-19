# necessary imports
from pprint import pprint
from flask import Flask, redirect, url_for, request
from pymongo import MongoClient
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
import json
import os

# make flask object
app = Flask(__name__)
cors = CORS(app)

# important initializations for the app
app.config['CORS_HEADERS'] = 'Content-Type'
UPLOAD_FOLDER = os.getcwd()
ALLOWED_EXTENSIONS = {'txt', 'zip'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# currently 16 MB, can be increased if needed
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000

# initializing client
client = MongoClient()

# Connect to the db
db=client.termProjectDB

wrappedStatistics = db.wrappedStatistics
toInsert = {
'Average Response Time' : '3256',
'Average length of text' : '3227',
'Most active day' : 'Sunday',
'Number of Messages Received' : '5000',
'Number of Messages Sent' : '10000', 
'Number of images sent' : '4315',
'Texts per day' : "816", 
'Texts per hour' : "1382",
'UserID' : "20"  
}

# Use the insert method
result = wrappedStatistics.insert_one(toInsert)

# Query for the inserted document.
Queryresult = wrappedStatistics.find_one({'UserID': '20'})
pprint(Queryresult)

# function to check file type
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Handler for getting data associated with an id
@app.route('/getstats/<id>/')
def addname(id):
    user_stats = wrappedStatistics.find_one({'UserID' : id})
    return json.dumps(user_stats)

# Handler for file upload
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['inputFile']
    filename = secure_filename(file.filename)
    if file:
       file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
       return 'File uploaded', '200'
    else:
        return 'File not uploaded', '400'