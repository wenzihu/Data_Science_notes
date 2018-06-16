import urllib
import json

url = raw_input('Input url: ')
if len(url) < 1: url = 'http://python-data.dr-chuck.net/comments_196011.json '
uh = urllib.urlopen(url)
data = uh.read()
info = json.loads(data)
numbers = info['comments']
sum = 0
for line in numbers:
    num = line['count']
    sum = sum + int(num)
print sum
