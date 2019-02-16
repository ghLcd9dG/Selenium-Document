# -*- coding: utf-8 -*-
# 写法一
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
dr = webdriver.Chrome()
dr.implicitly_wait(10)  # 隐性等待和显性等待可以同时用，但要注意：等待的最长时间取两者之中的大者
dr.get('https://www.csdn.net/')
locator = (By.LINK_TEXT,u'首页')

try:
    #EC.presence_of_element_located()传入的参数是一个集合，我们可以向

    WebDriverWait(dr, 20, 0.5).until(EC.presence_of_element_located(locator))

finally:
    print(dr.find_element_by_link_text('首页').get_attribute('href'))
    time.sleep(2)
    dr.quit()