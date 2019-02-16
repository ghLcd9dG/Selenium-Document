
#常规的导入库
from selenium import webdriver
import time

#启动浏览器，打开页面
dr=webdriver.Chrome()
dr.get("https://www.python.org/")

#修改标题
time.sleep(1)
JS1="document.title='xxxxxx';"
dr.execute_script(JS1)


time.sleep(1)
dr.find_element_by_id("id-search-field").send_keys("pycon")
dr.find_element_by_id("submit").click()

#通过CSS样式
dr.find_element_by_css_selector(r'#content > div > section > form > ul > li:nth-child(1) > h3 > a').click()
dr.save_screenshot("codingpy.png")



