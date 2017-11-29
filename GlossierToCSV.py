# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 18:42:06 2017

@author: Casey
"""

#%%

import pandas as pd
import json
import os
import codecs

#%%

os.chdir("C:\\Users\\cdpha\\Google Drive\\Classes\\INFX 547 Social Media Data Mining\\INFX547Proj\\Tweepy JSON\\")

#%%

json_objects = []

with open("Glossier_tweets.json", "r") as f:

    for line in f:
        
        while True:
            try:
                obj = json.loads(line)
                break
            
            except ValueError:
                # Not yet a complete JSON value
                try:
                    line += next(f)
                except StopIteration:
                    print("reached end of file")
                    break
                
        json_objects.append(obj)
            
print("Done")

#%%

with codecs.open("Glosser_tweets.csv", "w+", "utf-8-sig") as out:
    
    out.write("tweet, time\n")
    
    for tweet in json_objects:
        text = tweet["text"]
        text = text.replace(",",";")
        text = text.replace("|",";")
        text = text.replace("\n",";")
        text = text.replace("\r",";")
        
        time = tweet["created_at"]
        
        out.write(text + "," + time + "\n")