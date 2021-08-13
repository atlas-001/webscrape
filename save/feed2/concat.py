# save-webpage.py
import pandas as pd 

import urllib.request, urllib.error, urllib.parse

url = feeds.csv

response = urllib.request.urlopen(url)
webContent = response.read()

f = open('web-pg-download.html', 'wb')
f.write(webContent)
f.close


