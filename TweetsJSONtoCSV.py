# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 20:08:36 2017

@author: Casey
"""

import json
import pandas as pd
import os
import codecs

#%%

files = ("Hashtag_balmdotcom.json", 
         "Hashtag_boybrow.json", 
         "Hashtag_glossier.json", 
         "Hashtag_glossiergirl.json", 
         "Hashtag_glossierpink.json",
         "Search_balmdotcom.json",
         "Search_boybrow.json",
         "Search_glossier.json",
         "Search_glossiergirl.json")

os.chdir("C:\\Users\\Casey\\Google Drive\\Classes\\INFX 547 Social Media Data Mining\\INFX547Proj\\Tweepy JSON\\")

#%%

json_objects = []

for file in files:
    
    with open(file, "r") as f:
        print("Opened " + file)
        
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

users = []

for obj in json_objects:
    users.append(obj["user"])

#%%
    
keys = []
count = 0

for key in users[00]:
    keys.append(key)

with codecs.open("Users.csv", "w+", "utf-8-sig") as out:
    
    end = len(users[0])
    c = 0
    
    # Write Header LIne
    for key in keys:
        c += 1
        
        out.write(key)
        
        if c != end:
            out.write(",")
            
    # Write values for each user
    for user in users:
        
        print(count)
        count += 1
        c = 0
        out.write("\n")
        
        for key in keys:
            c += 1
            
            if key in user:
                line = str(user[key])
                line = line.replace(",", ";")
                line = line.replace("|", ";")
                line = line.replace("\n", ";")
                line = line.replace("\r", ";")
            else:
                line = ""
            
            out.write(line)
            
            if c != end:
                out.write(",")
        
