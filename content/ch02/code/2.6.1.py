#coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver import ActionChains

driver=webdriver.Chrome()
driver.get("https://www.baidu.com/")

driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()

#获取cookie
cookies=driver.get_cookies()
#返回字典的key为的BAIDUID的cookie
cookie=driver.get_cookie("BAIDUID")
print(cookies)
print(cookie)

#删除所有cookie信息。
driver.delete_all_cookies()

#退出
driver.quit()
