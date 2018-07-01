# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 16:24:13 2018

@author: Vineet
"""
#required libraris import 
import json

import difflib

#loading json dataset file 
try:
    data = json.load(open("data.json"))
    print("Data set loaded")
except:
    print("Data set failed to load")

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(difflib.get_close_matches(word, data.keys())) > 0:
        suggestion = input("Did you mean %s instead! Enter Y for yes, N for no:  " % difflib.get_close_matches(word, data.keys())[0])
        if suggestion.lower().upper() == "Y":
            return data[difflib.get_close_matches(word, data.keys()) [0]]
        elif suggestion.lower().upper() == "N":
            return "word dosen't exist"
        else:
            return "Try again"
    else:
        print("Word dosen't exist! Try again")
        

word_definations = input("Enter word: ")

print(translate(word_definations))
