import pandas as pd

def get_sent_messages(textDf):
    '''
    extracts a user's sent messages
    input: textDf, a dataframe containing text messages
    returns: a dataframe containing only sent messages 
    '''
    sent_only = textDf[textDf["sent or rec"] == "sent"]
    sent_only.reset_index(drop=True, inplace=True)
    return sent_only

def split_messages_by_contacts(textDf):
    '''
    gets a list of dataframes where each dataframe contains only the messages
    from one contact
    '''
    messages_by_contact = []
    currDf = textDf
    while (len(currDf) > 0):
        mask = currDf["contact"] == currDf.loc[0, "contact"]
        contact_messages = currDf[mask]
        currDf = currDf[~mask]
        currDf.reset_index(drop=True, inplace=True)
        if len(contact_messages) >= 1:
            messages_by_contact.append(contact_messages)
    return messages_by_contact