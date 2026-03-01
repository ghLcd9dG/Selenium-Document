import requests
from requests.exceptions import MissingSchema
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import os
import time

class func:

    # 初始化
    def __init__(self):
        pass
    # 让界面滚动到底部的函数
    def scroll(self,driver):
        driver.execute_script("""
            (function () {
                var y = document.body.scrollTop;
                var step = 100;
                window.scroll(0, y);


                function f() {
                    if (y < document.body.scrollHeight) {
                        y += step;
                        window.scroll(0, y);
                        setTimeout(f, 50);
                    }
                    else {
                        window.scroll(0, y);
                        document.title += "scroll-done";
                    }
                }
                setTimeout(f, 1000);
            })();
            """)

        # 开始爬取
    def beginSpider(self,url):
        # 1. 前期工作
        driver = webdriver.Chrome()
        driver.get(url)

        try:
            # 首先加载出全部的内容，判断是否页面中存在“更多”这一个按钮
            while True:
                # 这里需要注意的是：selenium2 是不支持 类名之中 有空格的
                try:
                    self.scroll(driver)
                    time.sleep(30)
                    more = driver.find_element_by_css_selector \
                    ("div.Card:nth-child(4) > a:nth-child(1)")
                    actions=ActionChains(driver)
                    actions.move_to_element(more)
                    actions.click(more)
                    actions.perform()
                    # more.click() # 如果我们在页面中找到了更多，那么就点击更多，然后等两秒
                except NoSuchElementException as e:
                    break
            # 加载了全部的内容后，获取到所有内容，存为items
            soup = BeautifulSoup(driver.page_source,"html.parser")
            # 2. 对soup进行操作，获取出title，和包含内容的列表items
            titles = soup.find("title").text.replace('\n', '').replace('?', '').split()
            title = titles[0]
            print(title)
            # 如果当前目录下没有title命名的文件夹，则创建一个
            dirpath = os.getcwd() + "\\" + title + "\\"
            if not os.path.exists(dirpath):
                os.makedirs(dirpath)

            items = soup.find_all("div", class_="List-item")
            nimingCount = 0
            for item in items:
                # 分为两种情况：1.匿名用户，没有第一张头像 2. 匿名用户有第一张头像
                userName = item.find('img', class_="Avatar AuthorInfo-avatar").get("alt")
                if "匿名" in userName:
                    userName = "匿名用户_" + str(nimingCount)
                    nimingCount += 1
                count = 0  # 一个用户下有多个照片的
                images = item.find_all('img',class_ = "origin_image zh-lightbox-thumb lazy")

                for image in images:
                    # 保存图片
                    imageSrc = image.get("src")
                    picName = dirpath + userName + '_' + str(count) + ".jpg"
                    count += 1

                    try:
                        imageData = requests.get(imageSrc, stream=True).content
                        try:
                            with open(picName, 'wb') as jpg:
                                jpg.write(imageData)
                        except IOError as e:
                            print(userName + "的一张图片写入错误")
                    except MissingSchema as e:
                        print(userName + "的一张图片获取失败")
                        print("地址为：" + imageSrc)
        finally:
            # 最后要记得关闭浏览器，否则就会永远开着
            driver.quit()

if __name__ == '__main__':
    f = func()
    f.beginSpider("https://www.zhihu.com/question/36950102/answer/89597362")