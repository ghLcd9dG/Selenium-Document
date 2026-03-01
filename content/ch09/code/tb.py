# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

url="https://detail.tmall.com/item.htm?spm=a230r.1.14.3.113f5268zyhZo2&id=552925823079&cm_id=140105335569ed55e27b&abbucket=6&sku_properties=10004:97505;5919063:6536025"

dr=webdriver.Chrome()
dr.get(url)

time.sleep(0.5)
xpath1='//*[@id="J_TabBar"]/li[3]/a'
dr.find_element_by_xpath(xpath1).click()

time.sleep(1)xpath2='//*[@id="J_Reviews"]/div/div[1]/div[3]/div[2]/div'
comment_all=dr.find_element_by_xpath(xpath2)
print(comment_all.text)
for i in range(1,101):
	url='https://rate.tmall.com/list_detail_rate.htm?itemId=552925823079&spuId=697786254&sellerId=2616970884&order=3&currentPage=%d&append=0&content=1' %i
	dr.get(url)
	content=dr.find_element_by_xpath("/html/body").text
	print(text)
