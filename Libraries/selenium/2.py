from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://demoqa.com/")
driver.maximize_window()

time.sleep(2)
driver.find_element(By.LINK_TEXT,"Elements").click()
time.sleep(2)
driver.find_element(By.LINK_TEXT,"Text Box").click()
time.sleep(2)
driver.find_element(By.ID,"userName").send_keys("Dipankar")
driver.find_element(By.ID,"userEmail").send_keys("dipankar@gmail.com")
driver.find_element(By.ID,"currentAddress").send_keys("Bangalore")
driver.find_element(By.ID,"permanentAddress").send_keys("Howrah")
driver.find_element(By.ID,"submit").click()

input()

