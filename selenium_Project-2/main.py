from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

path="/usr/local/bin/chromedriver"
s = Service(path)
driver = webdriver.Chrome(service=s)

#url of nike men's shoes section
url = "https://www.nike.com/in/w/mens-shoes-nik1zy7ok"
driver.get(url)
time.sleep(4)

height= driver.execute_script("return document.body.scrollHeight")
# print(height)

while True:

    driver.execute_script("window.scrollTO(0,document.body.scrollHeight)")
    time.sleep(2)
    new_height = driver.execute_script("return document.body.scrollHeight")

    if height == new_height:
        break
    height = new_height
