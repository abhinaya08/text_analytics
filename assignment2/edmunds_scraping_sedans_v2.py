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
#url = "https://forums.edmunds.com/discussion/2864/general/x/entry-level-luxury-performance-sedans/p500"
driver = webdriver.Chrome(chrome_path, chrome_options=option) 
driver.minimize_window()
driver.get(url)

page_num = 1

#**Selecting last page to navigate forward
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="PagerBefore"]/a[8]')))
element.click()	

with open('edmunds_comments.csv', 'w',newline='') as file:
	w = csv.writer(file)
	w.writerow(["date", "username","post","quotes"])
	scrape_starttime = datetime.datetime.now()
	
	for i in range(pages):
		posts = driver.find_elements_by_class_name("userContent")
		quotes = driver.find_elements_by_class_name("QuoteText")
		username = driver.find_elements_by_class_name("Username")
		date_posted = driver.find_elements_by_class_name("DateCreated")
		
		if(len(quotes) ==0):
			for dt,us,post in zip(date_posted, username,posts):
				w.writerow([dt.text, us.text, post.text])
			
		else:
			for dt,us,post,quote in zip(date_posted, username,posts,quotes):
				w.writerow([dt.text, us.text, post.text,quote.text])
		
		print("{} Page Processed: {}".format(i+1, datetime.datetime.now()))
		#**Navigate forward
		#element = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="PagerBefore"]/a[10]'))) #for next page
		#element.click()
		
		#***Navigate backward
		element = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="PagerBefore"]/a[1]')))
		element.click()	

file.close()
print("\nDone!\n{} Pages Processed in {}".format(pages, datetime.datetime.now() - scrape_starttime))
driver.close()