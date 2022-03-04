

#import imp_lib #from inside the repo
import feedparser
import csv
import time
import urllib.request





def linker():
    start = time.time() #. time my object since its a nested mess
    #print("printing from inside linker")
    with open('feeds.csv','r') as csv_feeds:
        csv_read = csv.reader(csv_feeds) #open RSSfeed file 
        #print(csv_read)
        for sepval in csv_read:
            #print(sepval) #put my RSSfeed file into a list
            for val in sepval:
                with urllib.request.urlopen(val) as response:
                    html = response.read()  #fetch the XML content from RSS feeds
                    html = str(html)
                    with open('RSS.xml','w') as wr:
                        wr.write(html)
                    


    end = time.time()
    print("links execution time: ",end - start) 
                 
                
                



    
    

    

if __name__ == "__main__":
    print( "\nThis module should not be run directly. \nyou should have another script come in and call linker instead of trying to call this script directly. ")

