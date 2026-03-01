from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://baidu.com")
print("设置浏览器宽800、高480显示")
driver.set_window_size(800, 480)
