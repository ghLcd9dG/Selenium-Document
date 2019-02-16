#导入selenuim库
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#下面一行代码用于启动Chrome浏览器
driver = webdriver.Firefox()

#然后我们打开Python官方网站
driver.get("http://www.python.org")
