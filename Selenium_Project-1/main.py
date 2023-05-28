from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

path= "/Users/ameydesai/Desktop/chromedriver_mac64 (1)"
s = Service(path)
driver = webdriver.Chrome(service=s)
driver.get("https://www.google.com/")
time.sleep(60)

box = driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea")
box_input.send_keys("House of the dragon")
box_input.send_keys(Keys.ENTER)
time.sleep(3)

driver.find_element_by_xpath("""//*[@id="kp-wp-tab-overview"]/div[4]/div/div/div/div/div/div[1]/div/a""").click() #anchor tag
time.sleep(2)
drive.save_screenshot("/Users/ameydesai/Desktop/Webscraping Projects/Selenium_Project-1/dragon1.png")

driver.quit()