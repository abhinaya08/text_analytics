from pycookiecheat import chrome_cookies
import os, re, lxml, requests, time
from bs4 import BeautifulSoup as bs
import pickle as pk

baseurl = 'http://www.glassdoor.com'

cookFile = os.path.expanduser('~/.config/google-chrome/Default/Cookies')

cooks = chrome_cookies(baseurl, cookie_file = cookFile)

address = 'http://www.glassdoor.com/Reviews/Pearson-Reviews-E3322.htm'
adds = [address]
address_ranges = range(2, 168) # right now pages go like _P1, _P2, etc
for add in address_ranges:
    adds.append(address[:-4] + '_P' + str(add) + '.htm')

# I got these headers from inspecting the 'Network' tab in the 'More Tools'->'Developer Tools' from the Chrome menu
hdr = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36',
      'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
      'dnt': 1,
      'upgrade-insecure-requests': 1,
      'accept-encoding': 'gzip, deflate, sdch, br',
      'accept-language': 'en-US,en;q=0.8'
      }

s = requests.Session()

# this section is for testing to make sure it works first
'''
r = s.get(adds[0], headers = hdr, cookies=cooks)

soup = bs(r.text, 'lxml')

times = []
cons = []
pros = []

reviews = soup.find(id='ReviewsFeed')
eachReview = reviews.findAll('div', class_='hreview')

for review in eachReview:
    cons.append(review.find('p', class_=re.compile('cons')).getText())
    pros.append(review.find('p', class_=re.compile('pros')).getText())
    times.append(review.find('time', class_=re.compile('date')).getText())

print(cons)
'''

# here is the 'production' run
times = []
cons = []
pros = []
soups = [] # the raw webpage responses
for ad in adds:
    cooks = chrome_cookies(baseurl, cookie_file = cookFile)
    r = s.get(ad, headers = hdr, cookies=cooks)
    soup = bs(r.text, 'lxml')

    reviews = soup.find(id='ReviewsFeed')
    while reviews == None:
        # it will think you're a bot and put up a captcha page, unless you set the time.sleep to a longer time
        # if you refresh the browser it will work again until the captcha page comes up
        # if you're lucky, you will catch the captcha page on your browser, then it should work without interruption
        print('refresh browser and hit enter')
        continuing = input()
        cooks = chrome_cookies(baseurl, cookie_file = cookFile)
        r = s.get(ad, headers = hdr, cookies=cooks)
        soup = bs(r.text, 'lxml')
        soups.append(soup)
        reviews = soup.find(id='ReviewsFeed')

    reviews = soup.find(id='ReviewsFeed')
    eachReview = reviews.findAll('div', class_='hreview')

    for review in eachReview:
        cons.append(review.find('p', class_=re.compile('cons')).getText())
        pros.append(review.find('p', class_=re.compile('pros')).getText())
        times.append(review.find('time', class_=re.compile('date')).getText())

    print('completed', ad)
    #time.sleep(3)

# saves the data locally for more analysis later
pk.dump(soups, open('soups','wb'))
pk.dump(cons, open('cons','wb'))
pk.dump(pros, open('pros','wb'))
pk.dump(times, open('times','wb'))