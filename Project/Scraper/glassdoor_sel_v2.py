#== scraping Edmunds

from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
import pickle as pk

def site_login():
	driver.get("https://www.glassdoor.com/profile/login_input.htm?userOriginHook=HEADER_SIGNIN_LINK")
	driver.find_element_by_name("username").send_keys("abhinayaanand@gmail.com")
	driver.find_element_by_name("password").send_keys("scraper123")
	element = wait.until(EC.element_to_be_clickable((By.XPATH,"""//*[@id="InlineLoginModule"]/div/div/div/div[2]/div[2]/form/button""")))
	element.click()	
	#driver.find_element_by_xpath("""//*[@id="InlineLoginModule"]/div/div/div/div[2]/div[2]/form/button""").click()

pages = 2
option = webdriver.ChromeOptions()
option.add_argument("-incognito")
prefs = {'profile.managed_default_content_settings.images':2, 'disk-cache-size': 4096}
option.add_experimental_option("prefs", prefs)
chrome_path = r'C:\Users\abhin\Downloads\chromedriver_win32\chromedriver.exe'
base_url = "https://www.glassdoor.com/Reviews/Amazon-Reviews-E6036"
#url = "https://forums.edmunds.com/discussion/2864/general/x/entry-level-luxury-performance-sedans/p500"
driver = webdriver.Chrome(chrome_path, chrome_options=option) 
driver.minimize_window()
site_login()
driver.get(base_url+".htm")

t = []
r = []
p = []
c = []
e = []
l = []
star = []
outlook = []
num_pages = 2000

while pages <=num_pages:
	title = driver.find_elements_by_class_name("summary")
	pk.dump(t.append([x.text for x in title]),open('title','wb'))
	
	rating = driver.find_elements_by_class_name("value-title") #choose title here
	r.append([x.text for x in rating])
	pk.dump(r,open('rating','wb'))
	
	pros = driver.find_elements_by_css_selector(".pros.mainText")
	p.append([x.text for x in pros])
	pk.dump(p,open('pros','wb'))
	
	cons = driver.find_elements_by_css_selector(".cons.mainText")
	c.append([x.text for x in cons])
	pk.dump(c,open('cons','wb'))
	
	employee = driver.find_elements_by_class_name("authorJobTitle") #text
	e.append([x.text for x in employee])
	pk.dump(e,open('employee','wb'))
	
	location = driver.find_elements_by_class_name("authorLocation") #text
	l.append([x.text for x in location])
	pk.dump(l,open('location','wb'))

	ul = driver.find_elements_by_css_selector(".subRatings.module")
	for x in ul:
		div_elements = x.find_elements_by_css_selector(".minor")
		span_elements = x.find_elements_by_css_selector(".gdBars.gdRatings")
		star.append(list(zip([y.get_attribute('innerHTML') for y in div_elements],[y.get_attribute('title') for y in span_elements])))
	pk.dump(star,open('star','wb'))

	ul = driver.find_elements_by_css_selector(".flex-grid.recommends")
	for x in ul:
		#div_elements = x.find_elements_by_class_name("minor")
		span_elements = x.find_elements_by_tag_name("span")
		outlook.append([y.text for y in span_elements])
	pk.dump(outlook,open('outlook','wb'))

	driver.get(base_url + "_P"+str(pages)+".htm")
	pages +=1

driver.close()