from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("/home/smsc/Documents/chromedriver")      #chromedriver_path
driver.get("http://www.injectsolar.com/portal/#/login")             #navigating to that page

user_id=driver.find_element_by_id("login_id")
user_id.send_keys('triose')
user_password=driver.find_element_by_id("password")#fetch element by id
time.sleep(2)
user_password.send_keys('triose123')# password
time.sleep(2)
user_password.submit()#login disabled so use submit by submit key_word
time.sleep(2)
data=driver.find_elements_by_xpath('/html/body/app-root/app-inject-solar/div/div[2]/div[2]/div/app-dashboard/div/div/div[1]/div/div/div[1]/div[1]/div[3]/div')
daily_generation = [i.text for i in data] 
print(daily_generation)
driver.get("http://www.injectsolar.com/portal/#/inject-solar/errore-log")

