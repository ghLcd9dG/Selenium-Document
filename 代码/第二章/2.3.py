from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://baidu.com")

time.sleep(2)
driver.get("http://news.baidu.com")

time.sleep(2)
driver.back()

time.sleep(2)
driver.forward()

time.sleep(2)
driver.refresh()

time.sleep(2)
driver.quit()