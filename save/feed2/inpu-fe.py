import feedparser
import csv
import pandas as pd



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
