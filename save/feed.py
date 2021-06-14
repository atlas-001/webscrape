import feedparser 
bbci_co_uk = feedparser.parse('http://feeds.bbci.co.uk/news/rss.xml')

count = 1 
for post in bbci_co_uk.entries: 
    if count % 5 == 1: 
        print("-----------------------------------------\n")
        print(post.title + "\n")
        print(post.description + "\n")
        print(post.link + "\n") 

