

#import imp_lib #from inside the repo
#import feedparser
import csv
import time #for recording speed of this script and slowing down our crawling
import urllib.request #for opening links
import xml.etree.cElementTree as et #for dealing with xml
import os




def linker():
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
                 
                
                



    
    

    

if __name__ == "__main__":
    print( "\nThis module should not be run directly. \nyou should have another script come in and call linker instead of trying to call this script directly. ")

