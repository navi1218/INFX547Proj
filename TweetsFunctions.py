# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 08:39:48 2017

@author: Casey
"""

#%%

import tweepy
import json

#%% NOTES

"""

Hashtags

Restricting JSON to:
    Text
    Retweets
    Favorites
    Location
    @ reply
    date
    
    user:
        profile background color

"""

#%% Constants

get_count = 200

maxTweets = 10000
    

#%% Get Tweets

def getTweets(user, filename, api):
    
    max_id = -1
    sinceId = None
    
    tweet_count = 0
    
    print("Downloading at least {} tweets".format(maxTweets))
    
    with open(filename,"r+") as f:
#        print("Opened " + filename)
#        
#        data = json.load(f)
#        
#        if len(data) > 0:
#        
#            last_tweet = data[-1]
#            max_id = last_tweet["id"]
        
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
#                    print("Wrote tweets")
                
                
                tweet_count += len(new_tweets)
                print(tweet_count)
                
                max_id = new_tweets[-1].id
                    
            except tweepy.TweepError as e:
                print('some error : ' + str(e))
                break
            
        print("Reached max tweets")
            
            
#%% Search Tweets

def searchTweets(query, filename, api):
    
    max_id = -1
    sinceId = None
    
    tweet_count = 0
    
    print("Downloading at least {} tweets".format(maxTweets))
    
    with open(filename,"r+") as f:
        
#        data = json.load(f)
#        
#        if len(data) > 0:
#        
#            last_tweet = data[-1]
#            max_id = last_tweet["id"]
        
        print("Opened " + filename)
        
        while tweet_count <= maxTweets:
            
            try:
                
                if(max_id <= 0):
                    if(not sinceId):
                        new_tweets = api.search(q = query, 
                                                       count = get_count)
                        print("Got new tweets")
                    else:
                        new_tweets = api.search(q = query, 
                                                       count = get_count, 
                                                       since_id = sinceId)
                        print("Got new tweets since ", sinceId)
                else:
                    if(not sinceId):
                        new_tweets = api.search(q = query, 
                                                       count = get_count, 
                                                       max_id = str(max_id-1))
                        print("Got new tweets up to ", max_id)
                    else:
                        new_tweets = api.search(q = query, 
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
#                    print("Wrote tweets")
                
                
                tweet_count += len(new_tweets)
                print(tweet_count)
                
                max_id = new_tweets[-1].id
                    
            except tweepy.TweepError as e:
                print('some error : ' + str(e))
                break
            
        print("Reached max tweets")

#%% Example code from Github

        
#!/usr/bin/env python
# encoding: utf-8

#import tweepy #https://github.com/tweepy/tweepy
#import csv

#Twitter API credentials
#consumer_key = ""
#consumer_secret = ""
#access_key = ""
#access_secret = ""


#def get_all_tweets(screen_name):
#	#Twitter only allows access to a users most recent 3240 tweets with this method
#	
#	#authorize twitter, initialize tweepy
#	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#	auth.set_access_token(access_key, access_secret)
#	api = tweepy.API(auth)
#	
#	#initialize a list to hold all the tweepy Tweets
#	alltweets = []	
#	
#	#make initial request for most recent tweets (200 is the maximum allowed count)
#	new_tweets = api.user_timeline(screen_name = screen_name,count=200)
#	
#	#save most recent tweets
#	alltweets.extend(new_tweets)
#	
#	#save the id of the oldest tweet less one
#	oldest = alltweets[-1].id - 1
#	
#	#keep grabbing tweets until there are no tweets left to grab
#	while len(new_tweets) > 0:
#		print "getting tweets before %s" % (oldest)
#		
#		#all subsiquent requests use the max_id param to prevent duplicates
#		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
#		
#		#save most recent tweets
#		alltweets.extend(new_tweets)
#		
#		#update the id of the oldest tweet less one
#		oldest = alltweets[-1].id - 1
#		
#		print "...%s tweets downloaded so far" % (len(alltweets))
#	
#	#transform the tweepy tweets into a 2D array that will populate the csv	
#	outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]
#	
#	#write the csv	
#	with open('%s_tweets.csv' % screen_name, 'wb') as f:
#		writer = csv.writer(f)
#		writer.writerow(["id","created_at","text"])
#		writer.writerows(outtweets)
#	
#	pass


#if __name__ == '__main__':
#	#pass in the username of the account you want to download
#	get_all_tweets("J_tsar")
