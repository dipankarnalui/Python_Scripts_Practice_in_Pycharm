from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys

chrome_driver_path = r"C:\scripts\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chrome_driver_path
driver = webdriver.Chrome(chrome_driver_path)

url = "https://www.amazon.in/"
driver.get(url)
driver.find_element_by_id("twotabsearchtextbox").send_keys("mobile")
driver.find_element_by_id("twotabsearchtextbox").send_keys(Keys.RETURN)



