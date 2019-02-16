# -*- coding: utf-8 -*-
# @Author: name
# @Date:   2018-07-28 22:03:13
# @Last Modified by:   name
# @Last Modified time: 2018-07-28 23:06:17
#引入webdriver和time
from selenium import webdriver
import time

#打开浏览器和打开百度
driver=webdriver.Chrome()
driver.get("https://www.baidu.com/")

#通过id查找，然后输入，并点击
driver.find_element_by_name("wd").send_keys("selenium")
driver.find_element_by_id("su").click()
