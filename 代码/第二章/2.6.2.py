#coding=utf-8

from selenium import webdriver
import time
from selenium.webdriver import ActionChains

driver=webdriver.Chrome()

driver.get ("http://www.youdao.com")
# 向cookie中name和value中添加会话信息
driver.add_cookie({"name":"testname_1234567890"},{"value":"testvalue_1234567890"})

# 遍历cookie中name和value信息并打印对应的信息，并包括添加对应的信息
for cookie in driver.get_cookies ():
    print("%s<->%s" % (cookie['name'], cookie['value']))

#退出
driver.quit()
print("all_done")

