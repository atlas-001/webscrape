import feedparser

# THIS SCRIPT CURRENTLY DOESNT WORK AS INTENEDED JUNE07-2021
#maybe a class can work as an insert to the rss_feeds input?

def BunchoFeeds(self):
    feed_list = [
            'http://feeds.bbci.co.uk/news/rss.xml',
            'http://www.aljazeera.com/xml/rss/all.xml',
            ]
    return print(feed_list)


# this part below works. DONT FUCK WITH IT 
# need to get rss_feeds to open up a bunch of feeds
rss_feeds = feedparser.parse(BunchoFeeds.feed_list)

count = 1 
for post in rss_feeds.entries: 
    if count % 5 == 1: 
        print("-----------------------------------------\n")
        print(post.title + "\n")
        print(post.description + "\n")
        print(post.link + "\n") 

