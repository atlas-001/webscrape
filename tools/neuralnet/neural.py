#! usr/bin/env python


import json

def neural():
    #get the file and reconstruct the dict
    wordcount = open('wordcount.txt','r')
    reed = wordcount.read()
    counts = json.loads(reed) #reconstruct the dictionary
    print(type(counts))
    _count_keys = list(counts.keys()) #full list of words
    _count_values = list(counts.values()) #full list of values mapped to words

    

    
