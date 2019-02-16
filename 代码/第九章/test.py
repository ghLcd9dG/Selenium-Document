from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
from pyquery import PyQuery as pq
import pymysql

#连接到数据库
conn=pymysql.connect(host='localhost',port=3306,db='tb',user='root',passwd='password',charset='utf8')
cur=conn.cursor()

#定义存储到数据库函数
def save_to_mysql(product):

	insert="INSERT INTO info VALUES('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')".format(product[0],product[1],product[2],product[3],product[4],product[5])
	cur.execute(insert)
	conn.commit()


#提取商品数据
def get_products():
	#获取页面源代码
    html = browser.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product = [item.find('.pic .img').attr('data-src'),
        	item.find('.price').text(),
            item.find('.deal-cnt').text(),
            item.find('.title').text(),
            item.find('.shop').text(),
            item.find('.location').text()]
        print(product)
        save_to_mysql(product)
        print("done")

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)
KEYWORD = 'iPad'

def scratch_page(page):
    """
    抓取索引页
    :param page: 页码
    """
    print('正在爬取第', page, '页')
    try:
        url = 'https://s.taobao.com/search?q=' + quote(KEYWORD)
        browser.get(url)
        if page > 1:
            input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form > input')))
            submit = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager div.form > span.btn.J_Submit')))
            input.clear()
            input.send_keys(page)
            submit.click()
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'), str(page)))
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item')))
        get_products()
    except TimeoutException:
        scratch_page(page)
end_page=101
def main():

    for i in range(1, end_page):
        scratch_page(i)

if __name__ == '__main__':
    main()
