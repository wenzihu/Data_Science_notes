# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *
import re

url = raw_input('Enter - ')
if len(url) < 1: url ='http://python-data.dr-chuck.net/comments_196010.html '
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
sum = 0
tags = soup('span')

for tag in tags:
    line = str(tag)
    #print line
    num = re.findall('comments">([0-9]+)',line)
    sum = sum + int(num[0])
print sum
