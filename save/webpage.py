# save-webpage.py

import urllib.request, urllib.error, urllib.parse

url = 'https://www.bbc.co.uk/news/world-57386353'

response = urllib.request.urlopen(url)
webContent = response.read()

f = open('web-pg-download.html', 'wb')
f.write(webContent)
f.close

