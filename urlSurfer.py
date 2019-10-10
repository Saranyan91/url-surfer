from urllib.request import urlopen, Request
import re


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
reg_url = 'https://tamilarasan.net/tamil-movies-online/play-comali-2019-tamil-movie-online-gomovies/'
rulz_url = 'https://1movierulzfree.me/comali-2019-tamil/full-movie-watch-online-free.html'
mov_url = 'https://rocksdvd.com/v/6072ka0xxpq2q27'
req = Request(url=reg_url, headers=headers) 
html = urlopen(req).read().decode('utf-8')

# print(html)
#use re.findall to get all the links
links = re.findall(r'http[s]?:\/\/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', html)

print(links)



""" from urllib.request import urlopen
import re

url = 'https://1movierulzfree.me/comali-2019-tamil/full-movie-watch-online-free.html'
#connect to a URL
website = urlopen(url)

#read html code
html = website.read()

#use re.findall to get all the links
links = re.findall('"((http|ftp)s?://.*?)"', html)

print(links) """