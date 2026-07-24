from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get("https://google.com")
time.sleep(50)
driver.quit()

