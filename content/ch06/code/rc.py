# -*- coding: utf-8 -*-
import time
from selenium import webdriver

url="http://top.baidu.com/"
dr=webdriver.Chrome()
dr.implicitly_wait(2)
dr.get(url)

list_=[]
for i in dr.find_elements_by_class_name('num-top'):
    print(i)
    print(i.get_attribute('title'))
