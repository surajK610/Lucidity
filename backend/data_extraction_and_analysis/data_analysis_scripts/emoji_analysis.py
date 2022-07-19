from cgitb import text
from re import S
import numpy as np
from datetime import datetime as dt
import pandas as pd
import emoji
# from sochiatrist_wrapped.utils import get_sent_messages, split_messages_by_contacts
from data_extraction_and_analysis.data_analysis_scripts.message_extraction import get_sent_messages
# from message_extraction import get_sent_messages

# TODO: FIX BUG WITH THE COUPLE KISSING EMOJI!!!

def extract_emojis_from_message(message):
    emojis_only = []
        
    for word in message.split(' '):
        try:
            decoded = word.encode('latin1').decode('utf8')
        except: 
            decoded = word.encode('utf8').decode('utf8')
        if decoded in emoji.UNICODE_EMOJI['en']:
            emojis_only.append(emoji.emojize(decoded))

    return emojis_only

def get_most_popular_emojis(textDf):
    '''
    gets the 5 emojis a user uses most
    input: a dataframe containing the user's sent messages
    returns:
        a dict containing the top 5 emojis a user uses and the counts
        the total number of emojis in the user's messages
    '''
    sent_only = get_sent_messages(textDf)

    emoji_dict = {}
    # iterating through messages to get only the emojis
    for message in sent_only.message:
        # emojis_only = ''.join(c for c in message if c in emoji.UNICODE_EMOJI['en'])
        # print(message)
        message = str(message)
        emojis_only = extract_emojis_from_message(message)
        for e in emojis_only:
            # mapping emojis to the dictionary to keep count
            e = emoji.emojize(e)
            if e in emoji_dict.keys():
                emoji_dict[e] = emoji_dict[e] + 1
            else:
                emoji_dict[e] = 1

    # iterating through reactions to get only the emojis
    sent_reactions_df = textDf[textDf.reactor == 'user']
    for reaction in sent_reactions_df.reaction:
        reaction = str(reaction)
        emojis_only = extract_emojis_from_message(reaction)
        for e in emojis_only:
            # mapping emojis to the dictionary to keep count
            e = emoji.emojize(e)

            if e in emoji_dict.keys():
                emoji_dict[e] = emoji_dict[e] + 1
            else:
                emoji_dict[e] = 1

    # sorting the dictionary
    sorted_Dict = sorted(emoji_dict.items(), key = lambda pair : (pair[1], pair[0]), reverse = True)
    total_emojis = sum(emoji_dict.values())
    # returning the top 5 emojis
    if len(sorted_Dict) >= 10:
        return sorted_Dict[0:10], total_emojis
    else:
        return sorted_Dict, total_emojis
    
    
def get_emoji_frequency(sent_only, measure):
    '''
    the average numebr of emojis you send per message
    input:
        sent_only, a dataframe of a user's sent messages
    returns:
        the average frequency of emoji usage, per message
    '''
    if len(sent_only) < 10:
        return 0
    _, total_emojis = get_most_popular_emojis(sent_only)
    return total_emojis/len(sent_only)

def get_fav_emoji_by_contact(textDf):
    '''
    Gets the 5 people that you sent emojis the most with
    input:
        textDf, a dataframe containing all user messages
    return:
        a list of tuples 
    '''
    contacts = textDf.contact.unique()
    emojis_by_contact = []
    # iterating through each contact
    for contact in contacts:
        # getting only messages with that contact
        contact_df = textDf[textDf.contact == contact]
        # getting most popular emojis for each contact
        # sent_with_contact = get_sent_messages(contact_df)
        most_freq, _ = get_most_popular_emojis(contact_df)
        freq_emojis_only = [emoji.emojize(e[0]) for e in most_freq]
        # getting how frequently the user uses emojis with that contact
        emoji_freq = get_emoji_frequency(contact_df, "message")
        emojis_by_contact.append(tuple((emoji_freq, contact, freq_emojis_only)))

    # sorting and getting the contacts with most frequent emoji usage
    sorted_by_contact = sorted(emojis_by_contact, reverse = True)
    if len(sorted_by_contact) >= 5:
        return [{'name':t[1], 'rate': "{:.2f}".format(t[0]), 'emojis': " ".join(t[2])} for t in sorted_by_contact[0:5]]
    else:
        return [{'name':t[1], 'rate': "{:.2f}".format(t[0]), 'emojis': " ".join(t[2])}  for t in sorted_by_contact]
    
def main():
    # message_csv = "/Users/neilxu/Desktop/CSVs/neilxu2001/neilxu2001_instagramDMs.csv"
    # titles = ["time", "sent or rec", "message", "contact"]
    # textDf = pd.read_csv("/Users/neilxu/Desktop/CSVs/neilxu2001/neilxu2001_instagramDMs.csv", names = titles)
    
    textDf = pd.read_csv("../../data/facebook_data/outputs/combined.csv")

    sent_only = get_sent_messages(textDf)
    # print(get_most_popular_emojis(sent_only))

    most_popular, total_emojis = get_most_popular_emojis(textDf)
    # most_popular = [p[0] for p in most_popular]
    print(most_popular, total_emojis)

    print(emoji.emojize('👨\u200d❤️\u200d💋\u200d👨'))
    print('👨‍👩‍👧‍👧')
    e = emoji.UNICODE_EMOJI['en']['👨\u200d❤️\u200d💋\u200d👨']
    print(emoji.emojize(e))
    # print(emoji.UNICODE_EMOJI['en'])
    
    # # day_frequency = get_emoji_frequency(textDf, "day")
    msg_frequency = get_emoji_frequency(textDf, "message")
    # # print(day_frequency)
    print(msg_frequency)

    contact_emojis = get_fav_emoji_by_contact(textDf)
    print(contact_emojis)

if __name__ == "__main__":
    main()