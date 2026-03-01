#常规的导入库
from selenium import webdriver
import time

#启动浏览器，打开页面
dr=webdriver.Chrome()
dr.get("https://www.python.org/")

#退出
driver.quit()