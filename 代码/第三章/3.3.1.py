
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

try:
    driver.find_element_by_tag_name("input")
    print ('test pass: successfully found by tag name')
except Exception as e:
    print ("Exception found", format(e))

driver.quit()