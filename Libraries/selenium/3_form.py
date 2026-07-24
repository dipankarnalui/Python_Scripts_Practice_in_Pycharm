from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://demoqa.com/")
driver.maximize_window()

time.sleep(2)
driver.find_element(By.LINK_TEXT,"Forms").click()
time.sleep(2)

driver.find_element(By.LINK_TEXT,"Practice Form").click()
time.sleep(2)

driver.find_element(By.ID,"firstName").send_keys("Dipankar")
driver.find_element(By.ID,"lastName").send_keys("Nalui")
driver.find_element(By.ID,"userEmail").send_keys("Dipankar@gmail.com")

driver.find_element(By.NAME,"gender")

input()

