import feedparser
import csv
import pandas as pd


# SUMMARY: june07-2021 --- this program grabs a bunch of links from a certain rss link and then make a list of the links in one csv file. 


# from - https://stackoverflow.com/questions/55792260/how-to-parse-multiple-feeds-from-csv-file-with-feedparser 

reader = csv.reader(open('feeds.csv', 'r'))
next(reader) # column headings
df = pd.DataFrame(columns=['links'])  # you can add more column titles from the feeds.csv 
for row in reader:
    url = row[0]
    print (url)

    feed = feedparser.parse(url)

    for i, post in enumerate(feed.entries):
        df.loc[len(df)] = post.link    # here is where you should add the extra column titles 
                                       # so you can print them out in the final csv

df.to_csv('alllinks.csv', index=False)
