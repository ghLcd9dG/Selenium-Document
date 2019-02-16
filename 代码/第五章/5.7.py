# -*- coding: utf-8 -*-
# @Author: name
# @Date:   2018-07-29 14:48:01
# @Last Modified by:   name
# @Last Modified time: 2018-07-30 09:33:59
#需要特别说明的是：隐性等待对整个driver的周期都起作用，所以只要设置一次即可，我曾看到有人把隐性等待当成了sleep在用，走哪儿都来一下…、
from selenium import webdriver

dr = webdriver.Chrome()
dr.implicitly_wait(30)  # 隐性等待，最长等30秒
dr.get('https://www.csdn.net/')
#dr.current_url
print(dr.find_element_by_link_text('首页').get_attribute('href'))
dr.quit()