
from selenium import webdriver
import time
driver_path = r'C:\Users\dnalui\drivers\geckodriver.exe'
driver = webdriver.Firefox(executable_path=driver_path)
url="https://www.flipkart.com/"
xpath1="//*[@id='container']/div/div[1]/div/div/div/div/div[1]/div/div/div/div[2]/div[1]/div/div[1]/div/div/div/div/div[1]/div[2]/div/div/span/span[1]"

driver.get(url)
time.sleep(20)