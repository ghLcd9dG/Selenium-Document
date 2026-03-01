from selenium import webdriver
dr=webdriver.Chrome()
dr.get('http://top.baidu.com/')
'''
//*[@id="hot-list"]/li[1]
//*[@id="hot-list"]/li[2]
'''

for i in range(10):
    xpath='//*[@id="hot-list"]/li['+str(i+1)+']/a[1]'
    print(dr.find_element_by_xpath(xpath).get_attribute('title'))