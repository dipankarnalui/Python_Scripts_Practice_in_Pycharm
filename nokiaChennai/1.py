import subprocess
from selenium import webdriver
import time

output = subprocess.check_output("netsh wlan show interfaces")
output = output.decode("ascii") # needed in python 3
output = output.replace("\r","")
#print(output)
all_lines = output.splitlines()
for line in all_lines:
    if "SSID" in line and line.strip().startswith("S"):
        #print(line)
        SSID=line.split(":")[1]
        #print(SSID)
    if "BSSID" in line:
        print(line)
    if "Authentication" in line:
        print(line)
password="abcd1234"

'''
cmd = "netsh wlan connect name={0} ssid={0}".format(SSID)
connection_result = subprocess.run(cmd, capture_output=True, text=True).stdout
print(connection_result)
'''

AP_URL = "http://192.168.0.1/"

driver = webdriver.Chrome(executable_path=r"C:\chromedriver.exe")

#driver = webdriver.Firefox(executable_path=r'C:\geckodriver.exe')

driver.get(AP_URL)
driver.maximize_window()
try:
    driver.find_element_by_id("pc-login-password").send_keys("act@123")
    print("entered the password")
except:
    print("failed to enter the password")
try:
    driver.find_element_by_id("pc-login-btn").click()
    print("Clicked Login button")
except:
    print("failed to Clicked Login button")
time.sleep(2)
network_option_xpath="/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div/ul/li[3]/a/span[2]"
driver.find_element_by_xpath(network_option_xpath).click()
time.sleep(2)
Lan_Settings_option_xpath="/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div/ul/li[3]/ul/li[2]/a/span"
driver.find_element_by_xpath(Lan_Settings_option_xpath).click()
time.sleep(2)
target = driver.find_element_by_id('tableClientList')
target.location_once_scrolled_into_view
time.sleep(2)
table_id = driver.find_element_by_id('tableClientList')
print(table_id)
rows = table_id.find_elements_by_tag_name("tr")
for row in rows:
    cols = row.find_elements_by_css_selector('td')
for col in cols:
    print(col.text())






