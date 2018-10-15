from bs4 import BeautifulSoup
from urllib.request import urlopen 
import requests
import logging
 
def set_custom_log_info(filename):
    logging.basicConfig(filename=filename, level=logging.INFO)
     
def report(e:Exception):
    logging.exception(str(e))

page_link = "https://www.glassdoor.com/Reviews/Amazon-Reviews-E6036.htm"


hdr = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36',
      'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
      'dnt': 1,
      'upgrade-insecure-requests': 1,
      'accept-encoding': 'gzip, deflate, sdch, br',
      'accept-language': 'en-US,en;q=0.8'
      }

page_response = requests.get(page_link)
print(page_response.text[:500])
print(page_response.content[:500])


html_soup = BeautifulSoup(page_response.content, "html.parser")

review_containers = html_soup.find_all('p', class_ = 'pros')
print(type(review_containers))
print(len(review_containers))

#reviews = soup.find(id='ReviewsFeed')

# for i in range(0, 20):
#     paragraphs = page_content.find_all("p")[i].text
#     textContent.append(paragraphs)