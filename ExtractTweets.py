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
import sys
import os


#%% Add path for import

# Have to add the path of the current project so that python knows where to 
# import the TweetsFunctions.py from

sys.path.append("C:\\Users\\cdpha\\Google Drive\\Classes\\INFX 547 Social Media Data Mining\\INFX547Proj")
sys.path.append("C:\\Users\\Casey\\Google Drive\\Classes\\INFX 547 Social Media Data Mining\\INFX547Proj")

print(sys.path)

#%%

import TweetsFunctions as tf

#%% Keys and Authentication

consumer_key = "kkpWJspPKj2hgvKsFbxSB7AuJ"
consumer_secret = "Y6NBohDkAsZkUc2HBjHJYq6CnmLpQfOQcmRE2JUfj8p3BlpqVd"
access_token = "164444620-6qFUAcmai3UI88Key8FNCNkYFe0tYxWE46QcL7P8"
access_token_secret = "y8aWNlVJPGpGoQz604IrXGugcKp6h4XPR41PbmYfCL9YJ"

auth = tweepy.AppAuthHandler(consumer_key,consumer_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
api


#%% Get Tweets

tf.getTweets("glossier", "Glossier_tweets.json", api)

#%% Search Tweets

tf.searchTweets("#glossier", "Hashtag_glossier.json", api)

tf.searchTweets("#glossierpink", "Hashtag_glossierpink.json", api)

tf.searchTweets("#nofilterjustglossier", "Hashtag_nofilterjustglossier.json", api)
