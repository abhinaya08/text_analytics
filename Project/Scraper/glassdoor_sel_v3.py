#== scraping Edmunds

from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
import pickle as pk
import csv

def site_login():
    driver.get("https://www.glassdoor.com/profile/login_input.htm?userOriginHook=HEADER_SIGNIN_LINK")
    element = wait.until(EC.element_to_be_clickable((By.XPATH,"""//*[@id="InlineLoginModule"]/div/div/div/div[2]/div[2]/form/button""")))
    driver.find_element_by_name("username").send_keys("abhinayaanand@gmail.com")
    driver.find_element_by_name("password").send_keys("scraper123")
    #element = wait.until(EC.element_to_be_clickable((By.XPATH,"""//*[@id="InlineLoginModule"]/div/div/div/div[2]/div[2]/form/button""")))
    element.click()	
    #driver.find_element_by_xpath("""//*[@id="InlineLoginModule"]/div/div/div/div[2]/div[2]/form/button""").click()

pages = 2

num_pages = int(input("How many pages do you want to scrape? "))

option = webdriver.ChromeOptions()
option.add_argument("-incognito")
prefs = {'profile.managed_default_content_settings.images':2, 'disk-cache-size': 4096}
option.add_experimental_option("prefs", prefs)
chrome_path = r'C:\Users\abhin\Downloads\chromedriver_win32\chromedriver.exe'
base_url = "https://www.glassdoor.com/Reviews/Amazon-Reviews-E6036"
#url = "https://forums.edmunds.com/discussion/2864/general/x/entry-level-luxury-performance-sedans/p500"
driver = webdriver.Chrome(chrome_path, chrome_options=option) 
driver.minimize_window()
wait = WebDriverWait(driver, 10)
site_login()
driver.get(base_url+".htm")

star = []
outlook = []
#num_pages = 20

with open('amazon_reviews.csv','w',newline = '') as file:
    w = csv.writer(file)
    w.writerow(["date","title","overall_rating","employee_details","pros","cons","ratings_breakup","outlook"])
    
    while pages <=num_pages:
        title = driver.find_elements_by_css_selector("span.summary ")
        
        rating = driver.find_elements_by_css_selector(".value-title") #choose title here
        
        pros = driver.find_elements_by_css_selector(".pros.mainText")

        cons = driver.find_elements_by_css_selector(".cons.mainText")
        
        employee = driver.find_elements_by_css_selector("span.authorJobTitle.middle.reviewer") #text
        
        ul = driver.find_elements_by_css_selector(".subRatings.module")
        for x in ul:
            div_elements = x.find_elements_by_css_selector(".minor")
            span_elements = x.find_elements_by_css_selector(".gdBars.gdRatings")
            star.append(list(zip([y.get_attribute('innerHTML') for y in div_elements],[y.get_attribute('title') for y in span_elements])))

        ul = driver.find_elements_by_css_selector(".flex-grid.recommends")
        for x in ul:
            #div_elements = x.find_elements_by_class_name("minor")
            span_elements = x.find_elements_by_tag_name("span")
            outlook.append([y.text for y in span_elements])


        dt = driver.find_elements_by_css_selector(".date.subtle.small")

        rows = zip(dt , title , rating  ,employee, pros , cons,star,outlook)        
        for d , t , r  , e , p , c,s,o in rows:
            w.writerow([d.text.encode("utf-8"),t.text.encode("utf-8"),r.get_attribute('title').encode("utf-8")
                ,e.text.encode("utf-8"),p.text.encode("utf-8"),c.text.encode("utf-8"),s,o])
        
        driver.get(base_url + "_P"+str(pages)+".htm")
        pages +=1
        print("Pages {} completed".format(pages))
    

driver.close()
file.close()