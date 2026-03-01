#coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver import ActionChains
#今日头条首页为例,下拉第二条思路
#我们利用将鼠标移动到最后一个元素位置模拟下拉
driver=webdriver.Chrome()
driver.get("https://www.toutiao.com/")

driver.save_screenshot("save_1.png")#图片是为了比较变化

ac=driver.find_element_by_xpath("//ul[@infinite-scroll-disabled]/li[last()]")
ActionChains(driver).move_to_element(ac).perform()#定位鼠标到指定元素

time.sleep(2)#给加载内容预留2秒
driver.save_screenshot("save_2.png")
