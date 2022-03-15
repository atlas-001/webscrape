#! usr/bin/env python

#import initenv  # will work on this later as an enhancement 
#. importing works like this : from application.app.folder.file import func_name
import tools.DataCleaning.getfeeds as getfeed
import tools.DataCleaning.webpage as webpage
import tools.DataCleaning.cleaners as clean
import os
import time

#time this module
start_time = time.time()
#change directory to scratch
cur_wd = os.getcwd()
print('current working directory: ',os.getcwd())
path_cmd = cur_wd + '/scratch/'
os.chdir(path_cmd)
print('now in: ',os.getcwd())


#get me my rss feeds
#print('getting rss feeds')
#gf.linker()

#get me my news page links
#print('parsing xml')
#gf.ParseXML_BBC()

#parse the webpage
#print('parsing webpages')
#wp.Webpage()

#feed links into webpage this should be done inside of webpage when done 
#print('feeding link into webpage.py')
#gf.Feeder()


'''
import time
all_webpages_list = gf.Feeder()
for webpage in all_webpages_list:
        wait_time = 0.5   #. <------------------ PUT WAIT TIME HERE
        time.sleep(wait_time)
        url = webpage
        print('waited for: ',wait_time,' sec','url accessed: ',url)
'''

#remove redundant words from allwords file 
clean.Redundant()

#change directory back to top of repo 
os.chdir('../')
end_time = time.time()
print('\nEnded script.','[Execution time: ',end_time - start_time,' sec.]' , 'Changed dir. now in: ',os.getcwd(),'\n')