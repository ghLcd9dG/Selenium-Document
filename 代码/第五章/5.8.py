# -*- coding: utf-8 -*-
# @Author: name
# @Date:   2018-07-29 14:48:01
# @Last Modified by:   name
# @Last Modified time: 2018-07-30 09:34:15
#需要特别说明的是：隐性等待对整个driver的周期都起作用，所以只要设置一次即可，我曾看到有人把隐性等待当成了sleep在用，走哪儿都来一下…、
from selenium import webdriver
import time
dr = webdriver.Chrome()

dr.get('https://www.csdn.net/')
time.sleep(3)
print(dr.current_url)
dr.quit()