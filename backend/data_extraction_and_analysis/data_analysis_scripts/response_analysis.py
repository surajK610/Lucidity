from dateutil.parser import parse
import numpy as np
from datetime import datetime as dt
from datetime import timedelta
import pandas as pd
# from sochiatrist.timetool import get_datetime
# from utils import split_messages_by_contacts
# from timetool import get_datetime

# TODO: STOPPING POINT: PARSETIME SECONDS NOT WORKING!!!! 
def parseTime(resTimeMilli):
    print(resTimeMilli)
    # 36061 sec -> 1 hr 0 min 1 sec 
    resTime = resTimeMilli // 1000
    hours = resTime//3600
    mins = (resTime//60)%60
    sec = resTime - hours*3600 - mins*60
    if hours > 0:
        return str(hours) + " hr " + str(mins) + " min " + str(sec) + " sec"
    elif mins > 0:
        return str(mins) + " min " + str(sec) + " sec"
    else:
        return str(sec) + " sec"

def get_mean_response_time(textDf, retString):
    res_times = []
    num_responses = 0
    textDf.reset_index(drop=True, inplace=True)
    for i in range(len(textDf)-1):
        if (((textDf.loc[i+1,"sent or rec"] == "received") 
            and (textDf.loc[i,"sent or rec"] == "sent"))
            and (textDf.loc[i, "contact"] == textDf.loc[i+1, "contact"])):
            try:
                # print(textDf.loc[i-1, "time"])
                sentTime = textDf.loc[i, "time"] #dt.strptime(textDf.loc[i, "time"], "%Y-%m-%d %H:%M:%S.%f") #[:-3]
                # print(sentTime)
                recTime = textDf.loc[i+1, "time"] #recTime = dt.strptime(textDf.loc[i+1, "time"], "%Y-%m-%d %H:%M:%S.%f") #[:-3]
                resTime = sentTime - recTime
            except:
                print("improper datetime format")
                continue
            # print(resTime.total_seconds())
            if ((resTime < 24*3600) and (resTime > 0)):
                res_times.append(resTime)
                num_responses += 1
    avg_time = sum(res_times)/len(res_times) if len(res_times) > 0 else 0 #np.mean(np.array(res_times))
    if avg_time != 0 and retString:
        # print(type(avg_time))
        return parseTime(avg_time), num_responses
    else:
        return avg_time, num_responses

def get_top_five_times(textDf):
    '''
    dictionary of contact to (number of sent, average time) pair
    a way to do them sorted?
    list of tuples 
    (response time, num messages responded to, contact)

    parse by contact? then call get_mean_response_time for each df, storing return
    values in a tuple. This tuple put into the list of contacts, then at the end
    we just return top 5 if > 5, otherwise, return whole list

    call split_messages_by_contacts, then for each df in the returned list, we
    construct a tuple, insert into sorted list, then proceed.
    '''
    contacts = textDf.contact.unique()
    # print(messages_by_contact[0])
    response_info_by_contact = []
    for contact in contacts:
        # print(messages_by_contact[i])
        contact_df = textDf[textDf.contact == contact]
        avg_res_time, num_responses = get_mean_response_time(contact_df, retString = False)
        if num_responses >= 5:
            response_info_by_contact.append(tuple((avg_res_time, num_responses, contact)))

    sorted_response_info = sorted(response_info_by_contact)

    if len(sorted_response_info) >= 5:
        return [{'name': t[2], 'responseTime':parseTime(t[0])} for t in sorted_response_info[0:5]]
    else:
        return [{'name': t[2], 'responseTime':parseTime(t[0])} for t in sorted_response_info]


def main():
    # message_csv = "/Users/neilxu/Desktop/CSVs/neilxu2001/neilxu2001_instagramDMs.csv"
    # titles = ["time", "sent or rec", "message", "contact"]
    titles = ["time", "sent or rec", "message", "contact", "type"]
    combined = pd.read_csv("../../data/facebook_data/outputs/combined.csv")
    textDf = combined.sort_values(["contact", "time"], ascending= False) 
    # print(textDf.head())
    mean, _ = get_mean_response_time(textDf, True)
    top_times = get_top_five_times(textDf)
    print(mean)
    print(top_times)

if __name__ == "__main__":
    main()