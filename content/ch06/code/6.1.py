#导入库
from selenium import webdriver

#打开浏览器和网页
dr=webdriver.Chrome()
dr.get('http://top.baidu.com/')

#整合 Xpath
for i in range(10):
	xpath='//*[@id="hot-list"]/li['+str(i+1)+']/a[1]'
	print(dr.find_element_by_xpath(xpath).get_attribute('title'))
