#from pycookiecheat import chrome_cookies
import os, re, lxml, requests, time
from bs4 import BeautifulSoup as bs
import pickle as pk

baseurl = 'http://www.glassdoor.com'
address = 'http://www.glassdoor.com/Reviews/Pearson-Reviews-E3322.htm'
ad = "https://www.glassdoor.com/Reviews/Amazon-Reviews-E6036.htm"
s = requests.Session()

times = []
cons = []
pros = []
soups = [] # the raw webpage responses

r = s.get(ad)
soup = bs(r.text, 'lxml')
print(soup)
#print(soup[:500])


reviews = soup.find(id='ReviewsFeed')
eachReview = reviews.find_all('div', class_='hreview')

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