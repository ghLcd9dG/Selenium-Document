from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def getinfo():
        id_=dr.find_element_by_xpath('//*/div[@class="article-sub"]/span[1]')
        time_=dr.find_element_by_xpath('//*/div[@class="article-sub"]/span[2]')
        title_=dr.find_element_by_xpath('//*/h1[@class="article-title"]')
        text_=dr.find_element_by_xpath('//*/div[@class="article-content"]')
        item=[id_.text,time_.text,title_.text,text_.text]
        return item

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


XPath='//*[@id="J_section_0"]/div/div/div[1]/div/div[1]/a/span'

try:
    WebDriverWait(dr, 20, 0.5).until(EC.presence_of_element_located((By.XPATH,XPath)))
finally:
    dr.find_element_by_xpath(XPath).click()

time.sleep(1)

all_handles = dr.window_handles
dr.switch_to_window(all_handles[-1])

info=getinfo()
print(info)

