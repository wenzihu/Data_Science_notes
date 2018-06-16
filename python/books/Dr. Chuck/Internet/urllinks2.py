# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

addr = raw_input('Enter address: ')
if len(addr) < 1: 
    addr =' https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Sahra.html'

position = int(raw_input('Enter position:'))
loop  = int(raw_input('Enter loop:'))
loops = range(loop)


for i in loops:
    html = urllib.urlopen(addr).read()
    soup = BeautifulSoup(html)

    # Retrieve all of the anchor tags
    tags = soup('a')
    addr = tags[position-1].get('href',None)
    print addr
