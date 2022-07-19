import tweepy
import pandas as pd
import json

def main():
    import tweepy
 
    # API keyws that yous saved earlier
    # api_key = "ymB5t7tt4aQ7Won5MQLeLEgCR"
    # api_secrets = "rkWASnKAOY95pegrbHlqjjpz83NbbW0hwGekPZXM7luq9VIhfv"
    # access_token = "1519142963456135173-gqcsp0o8ielRZ2RkchivhekUF7w9ed"
    # access_secret = "sFgltyMepEQeOw95VeAY83CRwpN80rg1XSPg734uhZl1w"
    
    # # Authenticate to Twitter
    # auth = tweepy.OAuthHandler(api_key,api_secrets)
    # auth.set_access_token(access_token,access_secret)
    
    # api = tweepy.API(auth)
    BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAABRocAEAAAAA4UyFIqfluWRVckU4NprO8kW4myE%3DKZl2OV0k2JUw7CorLD0sEelYbCardHdE0HBPvcJ700nROccQm1"
    # BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAKjBbwEAAAAA4%2B1OeUBqmu2v5dlOl3oRHhnmack%3D1b2n9Q2Pw56b800NIlq75umvCj81StRx9ISB32qlrziiVZFF5K"
    client = tweepy.Client(bearer_token = BEARER_TOKEN)

    # try:
    #     api.verify_credentials()
    #     print('Successful Authentication')
    # except:
    #     print('Failed authentication')

    top_celebs = pd.read_csv("../data/Top-1000-Celebrity-Twitter-Accounts.csv")
    top_celebs = top_celebs.drop_duplicates()
    top_accounts = list(top_celebs.twitter)
    celeb_names = list(top_celebs.name)

    data_dict = {}
    n = 0

    for i in range(100):
        
        account = top_accounts[i]
        name = celeb_names[i]
        # print(str(account))
        # get most recent n tweets, make a row for each one 
        # maybe get twitter id, then use it to get most recent tweets
        try:

            celeb_data = client.get_user(username=account)
            user_id = celeb_data.data.id

            all_tweets  = []

            next_token = None
            pages = 0
            while (next_token != -1) and (pages < 5):
                celeb_tweets = client.get_users_tweets(id = user_id, max_results=100, 
                                                        pagination_token=next_token)
                all_tweets += celeb_tweets.data
                next_token = celeb_tweets.meta.get('next_token', -1)
                pages += 1

            print(i, name)
            for tweet in all_tweets:
                text = tweet.text.replace('\n', ' ')
                new_tweet = {'name': name, 'celeb':account, 'message': text}
                data_dict[n] = new_tweet
                n += 1
        except:
            print(name, "Something went wrong")
        
    celeb_df = pd.DataFrame.from_dict(data_dict, "index")
    output_path = '../data/celeb_tweets.csv'
    celeb_df.to_csv(output_path, index=False)
    
if __name__ == '__main__':
    main()