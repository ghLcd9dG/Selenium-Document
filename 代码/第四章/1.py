# 导入 webdriver
from selenium import webdriver
import time

# 要想调用键盘按键操作需要引入keys包
from selenium.webdriver.common.keys import Keys

# 调用环境变量指定的PhantomJS浏览器创建浏览器对象
driver = webdriver.PhantomJS()

# get方法会一直等到页面被完全加载，然后才会继续程序，通常测试会在这里选择 time.sleep(2)
driver.get("http://cn.bing.com/")

#打印页面标题
title_=driver.title
print(title_)

# id="sb_form_q"是bing搜索输入框，输入字符串"SELENIUM自动化测试"
keywords = 'SELENIUM自动化测试'
driver.find_element_by_id("sb_form_q").send_keys(keywords)

# 生成当前页面快照并保存
driver.save_screenshot("bing_1.png")

#点击搜索按钮
driver.find_element_by_id("sb_form_go").click()

# 生成当前页面快照并保存
driver.save_screenshot("bing_2.png")

# 进行当前页面点击第一项
driver.find_element_by_xpath("/html/body/div/ol/li/h2/a").click()

# 生成当前页面快照并保存，在这里由于没有页面重定位，仍停留在这个页面
driver.save_screenshot("bing_3.png")

# 关闭浏览器
driver,quit()
