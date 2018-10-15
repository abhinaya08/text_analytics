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

#pages = int(input("How many pages do you want to scrape? "))
pages = 5
option = webdriver.ChromeOptions()
#option.add_argument("—incognito")
prefs = {'profile.managed_default_content_settings.images':2, 'disk-cache-size': 4096}
option.add_experimental_option("prefs", prefs)
chrome_path = r'C:\Users\abhin\Downloads\chromedriver_win32\chromedriver.exe'
url = "https://www.glassdoor.com/Reviews/Amazon-US-Reviews-EI_IE6036.0,6_IL.7,9_IN1.htm?filter.defaultEmploymentStatuses=false&filter.defaultLocation=false&filter.employmentStatus=PART_TIME&filter.employmentStatus=REGULAR"
#url = "https://forums.edmunds.com/discussion/2864/general/x/entry-level-luxury-performance-sedans/p500"
driver = webdriver.Chrome(chrome_path, chrome_options=option) 
driver.minimize_window()
driver.get(url)

page_num = 1

#**Selecting last page to navigate forward
#wait = WebDriverWait(driver, 10)
#element = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="PagerBefore"]/a[8]')))
#element.click()	

with open('glassdoor_ratings.csv', 'w',newline='') as file:
	for i in range(pages):
		w = csv.writer(file)
		w.writerow(["title", "overall_rating","sub_ratings","pros","cons","designation","location"])
		scrape_starttime = datetime.datetime.now()
		title = driver.find_elements_by_class_name("summary")
		rating = driver.find_elements_by_class_name("value-title") #choose title here
		sub_ratings = driver.find_elements_by_class_name("gdRatings") #choose title here
		pros = driver.find_elements_by_class_name("pros")
		cons = driver.find_elements_by_class_name("cons")
		employee = driver.find_elements_by_class_name("authorJobTitle") #text
		location = driver.find_elements_by_class_name("authorLocation") #text
		ul = driver.find_elements_by_class_name("undecorated")
		#print(ul)
		li_elements = [x.find_elements_by_tag_name("li") for x in ul]
		print(li_elements)
		#options =  [x for x in li_elements.find_elements_by_tag_name("gdRatings")]

		stars = {}
		# for li in [x for x in li_elements]:
		# 	for x in li:
		# 		print("****x******")
		# 		print(x)
		# 		y = x.find_element_by_tag_name('div')
		# 		print(y.text)
			#stars[li.find_element_by_tag_name('div').text] = li.find_element_by_tag_name('span').get_attribute('title')
			#stars[x.find_element_by_tag_name('div').text] = x.find_element_by_tag_name('span').get_attribute('title')
			#print(stars)
			
			#print(li.get_attribute('class'))
			#print(li.get_attribute('class'))
			#print(li.tag_name)
			#category = parse_xpath(li.xpath('.//div/text()'))
			#rating = parse_xpath(li.xpath('.//span/@title'), float)
			#stars.append({'category': category, 'rating': rating})
		# print("******stars******")
		# print(stars)
		#find_elements_by_xpath("//*[contains(text(), 'My Button')]")
		#//*[@id="empReview_19389841"]/div/div[2]/div/div[2]/div/div[1]/span/div/ul/li[1]/span

		for t,o,s,p,c,e,l in zip(title, rating,sub_ratings,pros, cons,employee,location):
			element = o
			# print(o.tag_name)
			# print(element.get_attribute('title'))
			# print(element.text)
			# print(element.tag_name)
			# #print(element.title_name)
			# print(element.get_attribute('value'))
			# print(element.get_attribute('innerHTML'))
			# print(element.parent)
			# print(element.location)
			# print(element.size)
			w.writerow([t.text, o.get_attribute('title'), s.get_attribute('title'),p.text,c.text,e.text,l.text])
			
	
	 	element = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="FooterPageNav"]/div/ul/li[7]'))) #for next page
		element.click()
		
	# 	#***Navigate backward
	# 	element = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="PagerBefore"]/a[1]')))
	# 	element.click()	

file.close()
print("\nDone!\n{} Pages Processed in {}".format(pages, datetime.datetime.now() - scrape_starttime))
driver.close()