# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 13:15:24 2017

@author: Casey
"""

"""

This script is used to extract tweets relevant to Glossier, including Glossier 
tweets, post comments, and tweets containing associated hashtags.

"""

#%%

import tweepy
import json

#%% Keys and Authentication

consumer_key = "kkpWJspPKj2hgvKsFbxSB7AuJ"
consumer_secret = "Y6NBohDkAsZkUc2HBjHJYq6CnmLpQfOQcmRE2JUfj8p3BlpqVd"
access_token = "164444620-6qFUAcmai3UI88Key8FNCNkYFe0tYxWE46QcL7P8"
access_token_secret = "y8aWNlVJPGpGoQz604IrXGugcKp6h4XPR41PbmYfCL9YJ"

auth = tweepy.AppAuthHandler(consumer_key,consumer_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
apis


#%% Get Tweets
# From In Class Demo

user = "glossier"
get_count = 200

maxTweets = 10000
tweet_count = 10

max_id = -1
sinceId = None

tweet_count = 0

print("Downloading at least {} tweets".format(maxTweets))

with open("Glossier_tweets.json","w") as f:
    print("Opened Glossier_tweets.json")
    
    while tweet_count <= maxTweets:
        
        try:
            
            if(max_id <= 0):
                if(not sinceId):
                    new_tweets = api.user_timeline(screen_name = user, 
                                                   count = get_count)
                    print("Got new tweets")
                else:
                    new_tweets = api.user_timeline(screen_name = user, 
                                                   count = get_count, 
                                                   since_id = sinceId)
                    print("Got new tweets since ", sinceId)
            else:
                if(not sinceId):
                    new_tweets = api.user_timeline(screen_name = user, 
                                                   count = get_count, 
                                                   max_id = str(max_id-1))
                    print("Got new tweets up to ", max_id)
                else:
                    new_tweets = api.user_timeline(screen_name = user, 
                                                   count = get_count, 
                                                   max_id = str(max_id-1), 
                                                   since_id = sinceId)
                    print("Got new tweets up to ", max_id, " since ", sinceId)
            
            if not new_tweets:
                print('no more tweets found')
                break
            		
            for tweet in new_tweets:
                json.dump(tweet._json, f, indent = 4, sort_keys = True)
                f.write('\n')
                print("Wrote tweets")
            
            
            tweet_count += len(new_tweets)
            max_id = new_tweets[-1].id
                
        except tweepy.TweepError as e:
            print('some error : ' + str(e))
            break




