# -*- coding: utf-8 -*-
# @Author: name
# @Date:   2018-07-30 12:39:18
# @Last Modified by:   name
# @Last Modified time: 2018-07-30 13:59:13
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import bs4
from bs4 import BeautifulSoup
import os
url="https://www.toutiao.com/"
driver=webdriver.Chrome()

def get_urls(url):

    driver.get(url) #打开网址
    time.sleep(1)
    driver.refresh() #这里要刷新一下，不然第一次加载没反应
    driver.implicitly_wait(2) #隐性等待2秒
    for i in range(100): #这里循环次数尽量大，保证加载到底
        ActionChains(driver).key_down(Keys.DOWN).perform() #相当于一直按着DOWN键
        print(f'已完成{i}次')
    time.sleep(3)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    body = soup.find_all(class_='link title') #提取网址
    print(soup)
    print(body)
    for i in range(len(body)):
        url = 'https://www.toutiao.com' + body[i].get('href')
        print(f'已完成{i}个')
        with open('urls.txt', 'w+') as f: #把网址按行保存到urls.txt
            print(url)
            f.writelines(url)
            f.write('\n')



def get_htmls():
    with open('urls.txt', 'r') as f:
        urls = f.readlines()
    l = len(urls)
    htmls = []
    for i in range(l):
        print(urls[i])
        driver.get(urls[i])
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight)') #加载到底部，保证图片文章中的图片加载完
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        try: #如果异常，刷新一下
            body = str(soup.find_all(class_='article-title')[0]) + str(soup.find_all(
                class_='article-sub')[0]) + str(soup.find_all(class_='article-content')[0]) #获取标题，时间，正文
        except IndexError:
            driver.refresh()
            time.sleep(2)
        if not os.path.exists('htmls'):
            os.mkdir('htmls')
        with open(f'htmls/{i}.html', 'w') as f: #保存到htmls文件夹下
            f.write(body)
        print(f'{i}.html 完成, 共{l}个')
        time.sleep(3)
    driver.quit()
get_urls(url)