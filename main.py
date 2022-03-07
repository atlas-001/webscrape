#! usr/bin/env python

#import initenv  # will work on this later as an enhancement 
#. importing works like this : from application.app.folder.file import func_name
import tools.DataCleaning.getfeeds as gf 
import tools.DataCleaning.webpage as wp
 
#get me my rss feeds
#gf.linker()

#get me my news page links
#gf.ParseXML()

#parse the webpage
#wp.Webpage()

#feed links into webpage this should be done inside of webpage when done 
#gf.Feeder()
'''
import time 
all_webpages_list = gf.Feeder()
def webpages():
    for things in all_webpages_list:
        webpage = things
        yield print(webpage)
webpages()
'''

wp.Webpage()

