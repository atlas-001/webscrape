

#import imp_lib #from inside the repo
#import feedparser
import csv
import time #for recording speed of this script and slowing down our crawling
import urllib.request #for opening links
import xml.etree.cElementTree as et #for dealing with xml
import os
import re 
from pathlib import Path #for messing with file I/O




def linker():
    ''' This object retrives xml rss files from a list of feeds 
    that are in feeds.csv for use later on. there is a small delay 
    on the script so that it doesnt overload servers 
    '''

    start = time.time() #. time my object since its a nested mess
    #print("printing from inside linker")
    with open('feeds.csv','r') as csv_feeds:
        csv_read = csv.reader(csv_feeds) #open RSSfeed file 
        #print(csv_read)
        for sepval in csv_read:
            #print(sepval) #put my RSSfeed file into a list
            for val in sepval:
                comman = 'wget ' + val
                print("script waiting 30sec to download next file")
                request_start = time.time()
                time.sleep(30) #we're going to start conservatively at 30sec
                os.system(comman)
                request_end = time.time()
                print("Script waited: ",request_end - request_start ,"secs")
                
    end = time.time()
    print("links execution time: ",end - start) 
                 
                


def ParseXML():
    ''' This object parses xml RSS files to feed links into 
    webpage.py 
    '''
    
    #. this part is for looking in my dir for files
    la = os.listdir() #lists all things dir in list 
    fi_list = []
    for x in la:
        #x_pattern = re.compile('rss') #compile regex search term
        cmpld_patt = re.match('^rss',x) #use regex to find files
        #print(cmpld_patt) #print what regex found
        if cmpld_patt:
            #print(cmpld_patt.string, type(cmpld_patt.string)) #print what regex found
            fi_list.append(cmpld_patt.string) #gives list of XML files to work with
            
        else:
            #. other files get dumped here
            pass 
        
    #print(fi_list)

    #get those xml files
    for fi in fi_list:
        #fi = "'" + fi + "'"
        with open(fi,'r') as concat_xml:
            reed = concat_xml.read()
            print(reed)

        


    
    

    

if __name__ == "__main__":
    print( "\nThis module should not be run directly. \nyou should have another script come in and call linker instead of trying to call this script directly. ")

