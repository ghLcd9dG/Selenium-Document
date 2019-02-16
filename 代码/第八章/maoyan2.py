from selenium import webdriver
import time
import csv

numbers_list=[0,10,20,30,40,50,60,70,80,90]

url_list=[]
for i in numbers_list:
    url="https://maoyan.com/board/4?offset=%d" %i
    url_list.append(url)
    print("获取地址:%s" %url)

dr=webdriver.Chrome()

csv_file=open("writer.csv","w+",newline='',encoding='utf-8-sig')
writer=csv.writer(csv_file)

for i in url_list:

    dr.get(i)
    time.sleep(1)
    print("正在链接为%s的页面" %i)

    for j in range(1,11):

        #获取演员
        xpath2='//*[@id="app"]/div/div/div[1]/dl/dd[%d]/div/div/div[1]/p[2]' %j
        actor=dr.find_element_by_xpath(xpath2).text

        #获取分数
        xpath3='//*[@id="app"]/div/div/div[1]/dl/dd[%d]/div/div/div[2]/p' %j
        score=dr.find_element_by_xpath(xpath3).text

        #获取标题
        xpath1='//*[@id="app"]/div/div/div[1]/dl/dd[%d]/div/div/div[1]/p[1]/a' %j
        title=dr.find_element_by_xpath(xpath1).get_attribute('title')

        #获取电影介绍
        dr.find_element_by_xpath(xpath1).click()
        xpath4='//*[@id="app"]/div/div[1]/div/div[2]/div[1]/div[1]/div[2]/span'
        introduce=dr.find_element_by_xpath(xpath4).text

        #拼接
        text=[]
        text.append(title)
        text.append(actor)
        text.append(score)
        text.append(introduce)

        #写入CSV
        writer.writerow(text)
        print("-----正在获取第%s条" %j)
        #返回初始页面
        dr.get(i)

print("all_done")
dr.close()
