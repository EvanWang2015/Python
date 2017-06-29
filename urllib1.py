import urllib
from BeautifulSoup import *
html = urllib.urlopen('https://finance.yahoo.com/').read()
soup = BeautifulSoup(html)
# for line in fhand:
    # print (line.strip())
tags = soup('a')
for tag in tags:
    print (tag.get('href',None))
# counts = dict()
# for line in fhand:
    # words = line.split()
    # for word in words:
        # counts[word] = counts.get(word,0)+1
# for key, val in counts.items():
    # print((key, val))
