#== scraping Edmunds

from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import pandas as pd

pages = int(input("How many pages do you want to scrape? "))
chrome_path = r'C:\Users\abhin\Downloads\chromedriver_win32\chromedriver.exe'

driver = webdriver.Chrome(chrome_path) 
driver.minimize_window()
driver.get("https://forums.edmunds.com/discussion/2864/general/x/entry-level-luxury-performance-sedans")
page_num = 1
posts_txt = []
username_txt = []
date_posted_txt = []
quotes_txt = []

driver.find_element_by_xpath("""//*[@id="PagerBefore"]/a[8]""").click()

for i in range(pages):
	posts = driver.find_elements_by_css_selector(".Message.userContent")
	for post in posts:
		posts_txt.append(post.text)
	#quotes = driver.find_elements_by_class_name("Quote")
	#for quote in quotes:
	#	quotes_txt.append(quote.text)
	username = driver.find_elements_by_class_name("Username")
	for us in username:
		username_txt.append(us.text)
	date_posted = driver.find_elements_by_css_selector(".MItem.DateCreated")
	for dt in date_posted:
		date_posted_txt.append(dt.text)
	print("Scraping page {} completed".format(page_num))
	page_num +=1
	driver.find_element_by_css_selector(".Previous.Pager-nav").click()

driver.close()
df = pd.DataFrame({'date':date_posted_txt,
	'username': username_txt,
	'post':posts_txt})
df.to_csv("ed2.csv")
