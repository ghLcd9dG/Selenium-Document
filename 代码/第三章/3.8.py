# -*- coding: utf-8 -*-
# @Author: name
# @Date:   2018-07-29 12:41:17
# @Last Modified by:   name
# @Last Modified time: 2018-07-29 12:41:43

#常规的导入库
from selenium import webdriver
import time

#打开浏览器和打开百度
driver=webdriver.Chrome()
driver.get("https://www.baidu.com/")

#打开新闻
time.sleep(2)
driver.find_element_by_partial_link_text("新闻").click()
driver.back()

#打开地图
time.sleep(2)
driver.find_element_by_partial_link_text("地图").click()
driver.back()

#打开视频
time.sleep(2)
driver.find_element_by_partial_link_text("视频").click()
driver.back()
#退出
time.sleep(2)
driver.quit()