import threading
import time

from selenium import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

CHROME_DRIVER_PATH = "/Users/austinkasekende/Desktop/CodeWork/Development/chromedriver"

services = Service(executable_path=CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=services)
driver.get(url="https://www.linkedin.com/jobs/search/?currentJobId=3244190147&f_E=1&f_JT=F&f_WT=1%2C3&geoId=101165590&keywords=Summer%20&location=United%20Kingdom&refresh=true")

sign_in = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in.click()

username = driver.find_element(By.ID, "username").send_keys("austin.kasekende12@gmail.com")
password = driver.find_element(By.ID, "password").send_keys("HLakeview25")
log_in = driver.find_element(By.CSS_SELECTOR, "BUTTON")
log_in.click()

# save = driver.find_element(By.CLASS_NAME, "a11y-text")
# save = driver.find_element(By.CSS_SELECTOR, "span.a11y-text")
# jobs-save-button artdeco-button artdeco-button--3 artdeco-button--secondary
# artdeco-button--3
# jobs-s-apply jobs-s-apply--fadein inline-flex mr2
# jobs-s-apply
# save.click()
# apply_button = driver.find_element(By.TAG_NAME, "button").text

# appy_list = []
# for i in apply_button:
#     appy_list.append(i.text)

# print(apply_button)

time.sleep(1000000000)

driver.quit()
