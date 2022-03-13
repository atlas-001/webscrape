#! usr/bin/env python


import json

def neural():
    #get the file and reconstruct the dict
    wordcount = open('wordcount.txt','r')
    reed = wordcount.read()
    counts = json.loads(reed) #reconstruct the dictionary
    print(type(counts))
