def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts
# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import operator
import json
import matplotlib.pyplot as plt


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = input('Enter url: )
url = 'https://stackoverflow.com/jobs?l=Remote=20&u=Km&sort=i&pg='
page = 0
count = 0
text = ' '
while page < 10:
    page = page + 1
    pageStr = str(page)
    newUrl = url + pageStr
    print(newUrl)
    html = urllib.request.urlopen(newUrl, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
    mt12 = soup.find_all("div", {"class": "mt12 -tags"})
    if not mt12:
        print("Finished")
#tags = soup('class')
    for tag in mt12:
        count = count + 1
        skills = tag.get_text(separator=' ')
        text = text + skills
        #print(skills)
    print('counts: ', count)
x = word_count(text)
sorted_x = sorted(x.items(), key=lambda kv: kv[1])
print(sorted_x)
dictlist = [ ]
temp = [ ]
for key, value in sorted_x:
    if value > 20:
        temp = [key,value]
        dictlist.append(temp)
print(dictlist)
x,y = zip(*dictlist)
xn = range(len(x))
plt.bar(xn, y)
plt.xticks(xn, x)
plt.show()
