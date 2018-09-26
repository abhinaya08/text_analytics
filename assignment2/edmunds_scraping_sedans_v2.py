#== scraping Edmunds

from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
import datetime
import time
import csv
import pandas as pd

pages = int(input("How many pages do you want to scrape? "))

option = webdriver.ChromeOptions()
option.add_argument("—incognito")
prefs = {'profile.managed_default_content_settings.images':2, 'disk-cache-size': 4096}
option.add_experimental_option("prefs", prefs)
chrome_path = r'C:\Users\abhin\Downloads\chromedriver_win32\chromedriver.exe'
url = "https://forums.edmunds.com/discussion/2864/general/x/entry-level-luxury-performance-sedans"
driver = webdriver.Chrome(chrome_path, chrome_options=option) 
driver.minimize_window()
driver.get(url)

page_num = 1

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="PagerBefore"]/a[8]')))
element.click()	

def clean_quotes(s):
	quotes = df['quotes']
	for q in quotes:
		if q in s:
			return(s.replace(q,""))
		else:
			return(s)

# file = open('edmunds_sedans.txt', 'w+')
# file.write("date \t username \t post \t quotes \n")
# file.close()
 
# #file = open('edmunds_sedans.txt', 'a+')     
# file = open('edmunds_sedans.txt', 'a')
posts_c = []

with open('edmunds_comments.csv', 'w',newline='') as file:
	w = csv.writer(file)
	w.writerow(["date", "username","post","quotes"])
	scrape_starttime = datetime.datetime.now()
	print("Pages Processed: {}".format(page_num, datetime.datetime.now()))

	for i in range(pages):
		posts = driver.find_elements_by_css_selector(".Message.userContent")
		quotes = driver.find_elements_by_class_name("QuoteText")
		#posts = [str.replace(post.text, quote.text, "") if post.text==quote.text else post.text for post in posts for quote in quotes]
		#for p in posts:
		#	posts_c.append(p.text.replace(quote.text, ""))
		
		#element = driver.find_elements_by_css_selector(".Message.userContent")
		#parent = driver.find_elements_by_css_selector(".Message.userContent")
		username = driver.find_elements_by_class_name("Username")
		date_posted = driver.find_elements_by_css_selector(".MItem.DateCreated")
		#print(list(zip(date_posted, username,posts,quotes)))
		#for dt,us,post,quote in zip(date_posted, username,posts,quotes):
		#	w.writerow([dt.text, us.text,  post.text , quote.text])
		
		for dt,us,post,quote in zip(date_posted, username,posts,quotes):
			w.writerow([dt.text, us.text, post.text,quote.text])
			#w.writerow([dt.text, us.text, post.text])

		print("{} Page Processed: {}".format(i+1, datetime.datetime.now()))

				#file.write(dt.text +"|" + us.text + "|" + post.text + "|" + quote.text + "\n")

file.close()

# print("Cleaning quotes")
# df = pd.read_csv("edmunds_comments.csv")
# df["post_clean"] = post.map(clean_quotes)
# df.to_csv("edmunds_comments_clean.csv")

print("\nDone!\n{} Pages Processed in {}".format(page_num, datetime.datetime.now() - scrape_starttime))


driver.close()
#df = pd.DataFrame({'date':date_posted_txt,
#	'username': username_txt,
#	'post':posts_txt})
#df.to_csv("ed2.csv")
