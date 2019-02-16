from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
from pyquery import PyQuery as PQ
import pymysql

conn=pymysql.connect(host='localhost',port=3306,db='tb',user='root',passwd='password',charset='utf8')
cur=conn.cursor()

def mysql_save(product):
    insert="INSERT INTO info VALUES('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')".format(product[0],product[1],product[2],product[3],product[4],product[5])
    cur.execute(insert)
    conn.commit()
    print(product)

#提取商品数据
def get_products():
    #获取页面源代码
    html=dr.page_source
    pq_file=PQ(html)
    all=pq_file('#mainsrp-itemlist .items .item').items()
    for i in all:
        product = [i.find('.pic .img').attr('data-src'),
            i.find('.price').text(),
            i.find('.deal-cnt').text(),
            i.find('.title').text(),
            i.find('.shop').text(),
            i.find('.location').text()]
        mysql_save(product)

#打开浏览器
dr=webdriver.Chrome()
wait=WebDriverWait(dr,10)
keyword='type c'

def scratch_page(page):
    #输出页面
    print('正在爬取第',page,'页')
    #防止某个页面失败导致爬虫停止
    try:
        #跳转关键词链接
        url='https://s.taobao.com/search?q='+quote(keyword)
        dr.get(url)

        if page > 1:
            #检测输入框
            input=wait.until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="mainsrp-pager"]/div/div/div/div[2]/input')))
            #检测提交框
            submit = wait.until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="mainsrp-pager"]/div/div/div/div[2]/span[3]')))
            #清空输入
            input.clear()
            #输入数字
            input.send_keys(page)
            #点击
            submit.click()

        #等待页面加载出来
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'), str(page)))
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item')))
        get_products()
    except:
        #重试
        scratch_page(page)
end_page=101
def main():

    for i in range(1, end_page):
        scratch_page(i)

if __name__ == '__main__':
    main()