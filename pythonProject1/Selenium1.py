from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.get("file:///Users/MacBook/Downloads/tip_calc/index.html")
billamt = driver.find_element(by="id", value="billamt")
billamt.send_keys("100")
sleep(5)