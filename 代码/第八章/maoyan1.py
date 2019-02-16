from selenium import webdriver
import time
numbers_list=[0,10,20,30,40,50,60,70,80,90]

url_list=[]
for i in numbers_list:
    url="https://maoyan.com/board/4?offset=%d" %i
    url_list.append(url)
    print("获取地址:%s" %url)

dr=webdriver.Chrome()

for i in url_list:
    dr.get(i)
    time.sleep(1)
    for j in range(1,10):
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

        print('电影标题：%s' %title)
        print("演员：%s" %actor)
        print("分数：%s" %score)
        print(introduce)
        dr.get(i)







#导演
'''

//*[@id="app"]/div/div/div[1]/dl/dd[2]/div/div/div[1]/p[2]
'''

dr.close()
