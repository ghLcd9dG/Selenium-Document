# -*- coding: utf-8 -*-
# @Author: name
# @Date:   2018-08-01 14:58:04
# @Last Modified by:   name
# @Last Modified time: 2018-08-01 14:59:01
from selenium import webdriver
dr=webdriver.Chrome()
dr.get('http://top.baidu.com/')

hw_dict=[]

for i in range(10):
    xpath='//*[@id="hot-list"]/li['+str(i+1)+']/a[1]'
    value=dr.find_element_by_xpath(xpath).get_attribute('title')
    hw_dict.append(value)

keyword=hw_dict[0]
URL='https://www.toutiao.com/search/?keyword=%s' %keyword
dr.get(URL)