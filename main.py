#! usr/bin/env python

#import initenv  # will work on this later as an enhancement 
#. importing works like this : from application.app.folder.file import func_name
import tools.DataCleaning.getfeeds as gf 
import tools.DataCleaning.webpage as wp
import os

#change directory to scratch
cur_wd = os.getcwd()
print('current working directory: ',os.getcwd())
path_cmd = cur_wd + '/scratch/'
os.chdir(path_cmd)
print('now in: ',os.getcwd())


#get me my rss feeds
gf.linker()

#get me my news page links
#gf.ParseXML()

#parse the webpage
#wp.Webpage()

#feed links into webpage this should be done inside of webpage when done 
#gf.Feeder()

# for opening up webpages and then getting word counts
#wp.Webpage()


#change directory back to top of repo 
os.chdir('../')
print('ended script. changed dir. now in: ',os.getcwd())