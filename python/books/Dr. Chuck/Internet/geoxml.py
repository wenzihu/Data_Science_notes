import urllib
import xml.etree.ElementTree as ET

url = 'http://python-data.dr-chuck.net/comments_196007.xml'
uh = urllib.urlopen(url)
data = uh.read()
tree = ET.fromstring(data)
lines = tree.findall('comments/comment')

sum = 0
print len(lines)
for line in lines:
    number = line.find('count').text
    sum = sum + int(number)
print sum


'''
while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
    print data
    tree = ET.fromstring(data)


    results = tree.findall('result')
    lat = results[0].find('geometry').find('location').find('lat').text
    lng = results[0].find('geometry').find('location').find('lng').text
    location = results[0].find('formatted_address').text

    print 'lat',lat,'lng',lng
    print location
    '''
