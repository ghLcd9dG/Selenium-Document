# 对于动态加载的网页，例如知乎，需要使用Selenium+ChromeDriver(或PhantomJS)
from bs4 import BeautifulSoup
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
import time

# 让界面滚动的函数 --
def scroll(driver):
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

def func():
    for story in storys :
        nameLabel = story.find('meta',itemprop="name")
        name=nameLabel["content"]
        storyText=story.find('div',class_="RichContent-inner")
        #打印看标签内容到底是什么
        try:
          string=name+'--------'+storyText.text+'\n'
          f.write(string)
          print('answer By '+str(name)+' has been finished')
        except Exception:
            print('Something is wrong while writing to txt')
if __name__ == '__main__':
    url='https://www.zhihu.com/question/54732849'
    driver = webdriver.Chrome()
    driver.get(url)
    scroll(driver)
    time.sleep(5)
    html = driver.page_source
    soup = BeautifulSoup(html,'lxml')
    storys = soup.find_all('div',class_="List-item")
    f=open('tmp.txt','w+')
    func()
    f.close()
    print('That is all')