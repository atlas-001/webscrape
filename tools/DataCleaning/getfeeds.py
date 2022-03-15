#! usr/bin/env python

#import imp_lib #from inside the repo
#import feedparser
import csv #commma seperated values
import time #for recording speed of this script and slowing down our crawling
import urllib.request #for opening links LOOOKS LIKE ITS NOT BEING USED????
import xml.etree.cElementTree as ET #for dealing with xml
import os #operating system commands
import re #regular expressions 
#from pathlib import Path #for messing with file I/O




def linker():
    ''' This object retrives xml rss files from a list of feeds 
    that are in feeds.csv for use later on. there is a small delay 
    on the script so that it doesnt overload servers 
    '''

    start = time.time() #. time my object since its a nested mess
    #print("printing from inside linker")
    #cwd = os.getcwd()
    where_feeds = '../tools/DataCleaning/feeds.csv' #at this pnt u shld b using main.py nd /scratch/
    with open(where_feeds,'r') as csv_feeds:
        print('getting you your RSS feeds!')
        csv_read = csv.reader(csv_feeds) #open RSSfeed file 
        #print(csv_read)
        for sepval in csv_read:
            #print(sepval) #put my RSSfeed file into a list
            for val in sepval:
                comman = 'wget ' + val  #when you get a chance its probably better to use curl
                print("script waiting 30sec to download next file")
                request_start = time.time()
                time.sleep(30) #we're going to start conservatively at 30sec
                os.system(comman)
                request_end = time.time()
                print("Script waited: ",request_end - request_start ,"secs")
                
    end = time.time()
    print("links execution time: ",end - start) 
                 
def Feeder():
    ''' for throwing links down the hatch in webpage.py '''
    print("starting to feed links into webpage.py")
    with open('alllinks.txt','r') as links:
        reed = links.read().splitlines()
    return reed                


def ParseXML_BBC():
    ''' This object parses xml RSS files to feed links into 
    webpage.py SPECFIC TO the BBC
    '''
    
    #. this part is for looking in my dir for files
    la = os.listdir() #lists all things dir in list 
    fi_list = []

    #FOR FINDING LINKS FROM WEBSITE RSS FEEDS
    for x in la:
        #x_pattern = re.compile('rss') #compile regex search term
        BBC_cmpld_patt = re.match('^rss',x) #use regex to find files USED FOR BBC NEWS
        #print(cmpld_patt) #print what regex found
        if BBC_cmpld_patt:
            #print(cmpld_patt.string, type(cmpld_patt.string)) #print what regex found
            fi_list.append(BBC_cmpld_patt.string) #gives list of XML files to work with
        else:
            #. other files get dumped here
            pass 
    
    #print(fi_list)

    #get those links from xml files
    xmltxt = open('xml-links.txt','w')
    for fi in fi_list:
        #fi = "'" + fi + "'"
        tree = ET.parse(fi) #open and parse the xml files
        root = tree.getroot() #get the roots
        _roots = root.getchildren()
        for channel in _roots:   
            item = channel.getchildren()
            for things in item:
                for txt in things:
                    xmltxt.write(txt.text + '\n') #write txt from insid item tag 2 txt doc
    xmltxt.close()
    xmltxt = open('xml-links.txt','r') #open and read 
    reed_xmltxt = xmltxt.read().splitlines() #get lines into list w/out newline symbols 
    #print(reed_xmltxt)
    _all_links_txt = open('alllinks.txt','w')
    for line in reed_xmltxt:
        find_links = re.match('^http',line)
        if find_links:
            _all_links_txt.write(find_links.string + '\n')
        else:
            pass



def ParseXML_CNN():
    #. this part is for looking in my dir for files
    la = os.listdir() #lists all things dir in list 
    fi_list = []

    #FOR FINDING LINKS FROM WEBSITE RSS FEEDS
    for x in la:
        #x_pattern = re.compile('rss') #compile regex search term
        BBC_cmpld_patt = re.match('^rss',x) #use regex to find files USED FOR BBC NEWS
        #print(cmpld_patt) #print what regex found
        if BBC_cmpld_patt:
            #print(cmpld_patt.string, type(cmpld_patt.string)) #print what regex found
            fi_list.append(BBC_cmpld_patt.string) #gives list of XML files to work with
        else:
            #. other files get dumped here
            pass
    

    #hint for adding more lines to the end of the document once you use BBC
    #. https://www.freecodecamp.org/news/python-create-file-how-to-append-and-write-to-a-text-file/
              


    
    

    

if __name__ == "__main__":
    print( "\nThis module should not be run directly. \nyou should have another script come in and call linker instead of trying to call this script directly. ")

