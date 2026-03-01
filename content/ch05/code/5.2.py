
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

#弹窗显示现在的标题
time.sleep(1)
JS2=r"alert($(document).attr('title'));"
dr.execute_script(JS2)




