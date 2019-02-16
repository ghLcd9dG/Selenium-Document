from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://192.168.1.51/oneCard/login")
#将用户名密码写入浏览器cookie中
driver.add_cookie({'name':'username','value':'super'})
driver.add_cookie({'name':'password','value':'asd,./123*.'})
#再次访问网站，将会自动登录
driver.get("http://192.168.1.51/oneCard/login")