import pandas as pd
import numpy as np
import os
import json
import datetime
from zipfile import ZipFile
import shutil

def extract_files(file_loc):
    # THIS IS A PRELIMINARY IMPLEMENTATION HARDCODED TO VIGNESH'S FILE

    # TODO: need to add mkdir functionality to create the facebook_data and facebook_extracted if they are not there
    data_folder = 'data/facebook_data/facebook_zipped/'
    if not os.path.exists(data_folder):
	    os.makedirs(data_folder)

    extract_dest = 'data/facebook_data/facebook_extracted/'
    if not os.path.exists(extract_dest):
	    os.makedirs(extract_dest)

    zipped_folder = data_folder
    # file_name = 'facebook-vigneshp20.zip'

    fname = os.path.splitext(os.path.basename(file_loc))[0]
    print("file name:", fname)
    
    # need to use os to check that the file actually exists and is valid
    with ZipFile(file_loc, 'r') as f:
        print("extract dest:", extract_dest)
        f.extractall(extract_dest)

    # getting path to messages
    messages_path = os.path.join(extract_dest, fname, "messages")
    print('messages path:', os.getcwd() + '/' + messages_path + '/autofill_information.json')

    # getting user's name
    with open(os.getcwd() + '/' + messages_path + '/autofill_information.json', 'r') as f:
        data = json.load(f)
    user_name = data['autofill_information_v2']['FULL_NAME'][0]

    # getting all conversations
    inbox_path = os.path.join(messages_path, "inbox")
    convos = [x for x in os.listdir(inbox_path)]
    convos.sort()
    print(convos)

    with open(messages_path + '/autofill_information.json', 'r') as f:
        data = json.load(f)
    user_name = data['autofill_information_v2']['FULL_NAME'][0]

    # loop through all conversations and get the files that start with "message"
    # parse the files by extrafcting the necessary components and converting to a csv

    '''
    /Users/neilxu/Documents/cs32/term-project-abao5-dgrossm5-nxu4-onaphade-sanand14-vpandiar/backend/data/facebook_data/facebook_extracted/facebook-vigneshp20/messages/autofill_information.json
    '''

    data_dict = {}
    i = 0

    for convo in convos:
        if convo == '.DS_Store':
            continue
        convo_path = os.path.join(inbox_path, convo)
        for file in np.sort(os.listdir(convo_path)):
            if file.startswith('message'):
                with open(convo_path + "/" + file, 'r') as f:
                    data = json.load(f)
                contact_list = []
                for p in data['participants']:
                    contact_list.append(p['name'])
                contact_list.remove(user_name)
                contact = ", ".join(contact_list)
                for message in data['messages']:
                    if 'content' in message:
                        time = message['timestamp_ms']
                        content = message['content'].replace("\n", " ")
                        sender_name = message['sender_name']
                        sent_or_rec = 'sent' if sender_name == user_name else 'received'
                        reaction = None
                        reactor = None
                        if 'reactions' in message:
                            reaction = message['reactions'][0]['reaction']
                            if message['reactions'][0]['actor'] == user_name:
                                reactor = 'user'
                            else:
                                reactor = 'other'
                        new_message = {'time': time, 'sent or rec': sent_or_rec, 'message': content, 
                            'contact':contact, 'reaction':reaction, 'reactor':reactor}
                        data_dict[i] = new_message
                        i += 1
                    
    convo_df = pd.DataFrame.from_dict(data_dict, "index")
    # output_path = '../data/facebook_data/outputs/combined.csv'
    # convo_df.to_csv(output_path, index=False)

    shutil.rmtree(extract_dest + fname)
    return convo_df

def main():
    # textdf = extract_files('../data/facebook_data/facebook_zipped/facebook-vigneshp20.zip')
    # print(textdf.head())
    return
if __name__ == "__main__":
    main()