#! usr/bin/env python

import urllib.request, urllib.error, urllib.parse
import enchant #for the english dictionary
import html2text #for cleanup of html
import os
from collections import Counter
import json
import tools.DataCleaning.getfeeds as gf 
import time


def Webpage():

    ed = enchant.Dict("en_US") # voila the english dictionary
    #ht = html2text.HTML2Text() #for cleanup

    #given URL
    all_webpages_list = gf.Feeder()
    for webpage in all_webpages_list:
        wait_time = 30   #. <------------------ PUT WAIT TIME HERE
        time.sleep(wait_time)
        url = webpage
        print('waited for: ',wait_time,' sec','url accessed: ',url)
        return url, print('waited for: ',wait_time,' sec','url accessed: ',url)
    url = url



    response = urllib.request.urlopen(url)
    webContent = response.read()

    #open and download a webpage
    f = open('web-pg-download.html', 'wb') # 'wb' is for writing bytes specifically
    f.write(webContent)


    #start parsing up things 
    webpage = open('web-pg-download.html','r')
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
            pass
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
    fi_word_count.close()
    #. a new dict scratch file is now made


    #. remove previous scratch files
    '''might want to let something else clean these out'''
    #os.system("rm scratch1.txt")
    #os.system("rm scratch2.txt")

