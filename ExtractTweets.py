# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 13:15:24 2017

@author: Casey
"""

"""

This script is used to extract tweets relevant to Glossier, including Glossier 
tweets, post comments, and tweets containing associated hashtags.

"""

import tweepy
import requests
import pandas as pd
import numpy as np
import os
import json
import datetime

consumer_key = "kkpWJspPKj2hgvKsFbxSB7AuJ"
consumer_secret = "Y6NBohDkAsZkUc2HBjHJYq6CnmLpQfOQcmRE2JUfj8p3BlpqVd"
access_token = "	164444620-6qFUAcmai3UI88Key8FNCNkYFe0tYxWE46QcL7P8"
access_token_secret = "y8aWNlVJPGpGoQz604IrXGugcKp6h4XPR41PbmYfCL9YJ"

auth = tweepy.AppAuthHandler(consumer_key,consumer_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
api