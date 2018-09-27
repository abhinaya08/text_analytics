#== scraping Edmunds

from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
import pandas as pd

pages = int(input("How many pages do you want to scrape? "))

def get_elements_by_xpath(driver, xpath):
    return [entry.text for entry in driver.find_elements_by_xpath(xpath)]

def get_elements_by_css(driver, css):
    return [entry.text for entry in driver.find_elements_by_css_selector(css)]

def get_elements_by_class(driver, clas):
    return [entry.text for entry in driver.find_elements_by_class_name(clas)]


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
posts_txt = []
username_txt = []
date_posted_txt = []
quotes_txt = []

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="PagerBefore"]/a[8]')))
element.click()	

#driver.find_element_by_xpath("""//*[@id="PagerBefore"]/a[8]""").click()

file = open('edmunds_sedans.txt', 'w+')
file.write("date | username | post \n")
file.close()
 
file = open('edmunds_sedans.txt', 'a+')     

for i in range(pages):
	posts = driver.find_elements_by_css_selector(".Message.userContent")
	quotes = driver.find_elements_by_class_name("QuoteText")
	#element = driver.find_elements_by_css_selector(".Message.userContent")
	#parent = driver.find_elements_by_css_selector(".Message.userContent")
	username = driver.find_elements_by_class_name("Username")
	date_posted = driver.find_elements_by_css_selector(".MItem.DateCreated")
	
	for dt,us,post in zip(date_posted, username,posts):
		file.write(dt.text +"|" + us.text + "|" + post.text +"\n")
	#
	#for dt,us,post in zip(date_posted_txt, username_txt,posts_txt):
	#	file.write(dt +"\t" + us + "\t" + post +"\n")
	#print(['\t'.join(dt.text,us.text,post.text) for dt in date_posted for us in username  for post in posts])
	#print(['\t'.join(t.text) for dt in date_posted for us in username  for post in posts])
	#print(['\t'.join(x.text) for x in temp])
	#file.write(['\t'.join(x.text) for x in temp])
	# print("Scraping page {} completed".format(page_num))
	# page_num +=1
	# if pages >1:
	# 	element = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="PagerBefore"]/a[1]')))
	# 	element.click()	
	
	#or post in posts:
	#	posts_txt.append(post.text)
	#quotes = driver.find_elements_by_class_name("Quote")
	#for quote in quotes:
	#	quotes_txt.append(quote.text)
	#for us in username:
	#	username_txt.append(us.text)
	#for dt in date_posted:
	#	date_posted_txt.append(dt.text)
	#print("************Dates**************")
	#print(['\t'.join(dt.text,us.text,post.text) for dt in date_posted for us in username  for post in posts])
	#page_data = [dt.text for dt in date_posted]+  "\t" +[us.text for us in username] + "\t" +[post.text for post in posts]
	#element = wait.until(EC.element_to_be_clickable(By.CssSelector(".Previous.Pager-nav")))
	#driver.find_element_by_css_selector(".Previous.Pager-nav").click()

file.close()
driver.close()
#df = pd.DataFrame({'date':date_posted_txt,
#	'username': username_txt,
#	'post':posts_txt})
#df.to_csv("ed2.csv")
