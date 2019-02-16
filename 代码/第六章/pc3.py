#coding:utf-8
import csv
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
def write(item):
    with open(r"F:\DOCUMENT\SELENIUM\第六章\jjtt.csv","a") as f:
        writer=csv.writer(f)
        try:
            writer.writerow(item)
        except:
            print("error")

def getinfo():
        id_=dr.find_element_by_xpath('//*/div[@class="article-sub"]/span[1]')
        time_=dr.find_element_by_xpath('//*/div[@class="article-sub"]/span[2]')
        title_=dr.find_element_by_xpath('//*/h1[@class="article-title"]')
        text_=dr.find_element_by_xpath('//*/div[@class="article-content"]')
        item=[id_.text,time_.text,title_.text,text_.text]
        return item

url="https://www.toutiao.com/search/?keyword=selenium"
dr=webdriver.Chrome()
dr.implicitly_wait(2)
dr.get(url)

time.sleep(1)

for i in range(100): #这里循环次数尽量大，保证加载到底

        ActionChains(dr).key_down(Keys.DOWN).perform() #相当于一直按着DOWN键
        print(f'下拉已完成{i}次')

time.sleep(1)
url_=dr.find_elements_by_css_selector('.title')
print(url_)

url_list=[]
for i in url_:
    url_list.append(i.get_attribute('href'))
print(url_list)

for i in url_list:
    try:
        dr.get(i)
        write(getinfo())
        dr.get(url)
        print('已完成书写')
    except:
        print("error")

