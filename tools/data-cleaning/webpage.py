#! usr/bin/env python

import urllib.request, urllib.error, urllib.parse
import enchant #for the english dictionary
import html2text #for cleanup of html
import os
from collections import Counter
import json


ed = enchant.Dict("en_US") # voila the english dictionary
#ht = html2text.HTML2Text() #for cleanup

#given URL
#url = 'https://www.bbc.com/news/world-europe-60365017'
#url = 'https://www.bbc.co.uk/news/world-57386353'



response = urllib.request.urlopen(url)
webContent = response.read()

#open and download a webpage
f = open('./webpage-DLs/web-pg-download.html', 'wb')
f.write(webContent)


#start parsing up things 
webpage = open('./webpage-DLs/web-pg-download.html','r')
redwp = webpage.readlines()
#print(type(redwp))

#close intial file and delete it too
f.close()
os.system("rm web-pg-download.html")

for x in redwp:
    #print(html2text.html2text(x))
    cleanwp = html2text.html2text(x)
    scratch = open('scratch1.txt','w')
    scratch.writelines(cleanwp)
    scratch.close()
webpage.close()

#open scratch file
scratch = open('scratch1.txt','r')
rescra = scratch.readlines()

#cleanup the webpage for easier detection of english
rescra = str(rescra)
rescra = rescra.splitlines()
rescra = str(rescra)
rescra = rescra.split()
#print(rescra)

#detect english words and print to scratch file
wordscra = open('scratch2.txt','w')
for x in rescra:
    if ed.check(x) is False:
        # Do nothing
        y = None #some false flag thing 
    else:  
        x = x + "\n" #make new lines
        wordscra.writelines(x) #print lines to scratch file
#close second scratch file 
wordscra.close()               
#close first scratch file
scratch.close()   

#open second scratch file


#automatically strips all newlines
lst = []
with open('scratch2.txt', 'r') as fi:
    for lines in fi:
        lines = lines.rstrip()
        lst.append(lines)        
#print(lst)
fi.close()


#count the words 
cnt = Counter()
for words in lst:
    cnt[words] += 1
cnt = dict(cnt)   
#print(cnt)

fi_word_count = open('wordcount.txt','w')
fi_word_count.write(json.dumps(cnt)) #write dictionary thru json
fi_word_count.close
#. a new dict scratch file is now made

#. remove previous scratch files
#os.system("rm scratch1.txt")
#os.system("rm scratch2.txt")

