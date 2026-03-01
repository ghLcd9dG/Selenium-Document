# coding=utf-8

from selenium import webdriver
import time

#打开浏览器，窗口最大化
driver=webdriver.Chrome()
driver.maximize_window() #

driver.get("http://baidu.com")

#停留两秒后打开搜狗搜索
time.sleep(2)
JS1='window.open("https://www.sogou.com");'
driver.execute_script(JS1)
#停留两秒后打开有道翻译
time.sleep(2)
JS2='window.open("https://fanyi.youdao.com/");'
driver.execute_script(JS2)

#退出
#driver.quit()
