#导入库
from selenium import webdriver
import time
import re

#打开浏览器
driver = webdriver.Chrome()

#登录账户
def log_in(username, password):
    #进入页面并暂停
    driver.get('https://passport.weibo.cn/signin/login')
    time.sleep(3)

    #输入账户密码，点击登录
    driver.find_element_by_id("loginName").send_keys(username)
    driver.find_element_by_id("loginPassword").send_keys(password)
    driver.find_element_by_id("loginAction").click()
    time.sleep(3)
    #查看cookie
    cookies = driver.get_cookies()
    cookie_list = []
    #把cookie循环写入到cookie_list
    for dict in cookies:
        cookie=dict['name'] + '=' + dict['value']
        cookie_list.append(cookie)
    cookie=';'.join(cookie_list)
    print(cookie)


def user_info(user_id):
    string='http://weibo.cn/' + user_id
    driver.get(string)
    print('********************')
    print('用户资料')

    #用户ID
    string_id='用户id:' + user_id
    print(string_id)

    #用户资料
    str_list=driver.find_element_by_xpath("//div[@class='ut']").text.split(' ')
    string_name='昵称:'+str_list[0]
    print(string_name)

    # 3.微博数、粉丝数、关注数
    string_num=driver.find_element_by_xpath("//div[@class='tip2']")
    pattern=r"\d+\.?\d*"      # 匹配数字，包含整数和小数
    result=re.findall(pattern, string_num.text)
    print(string_num.text)
    print("微博数：" + str(result[0]))
    print("关注数：" + str(result[1]))
    print("粉丝数：" + str(result[2]))
    print('\n********************')
    # 4.将用户信息写到文件里
    '''
    with open("userinfo.txt", "w", encoding = "gb18030") as file:
        file.write("用户ID：" + user_id + '\r\n')
        file.write("昵称：" + nickname + '\r\n')
        file.write("微博数：" + str(result[0]) + '\r\n')
        file.write("关注数：" + str(result[1]) + '\r\n')
        file.write("粉丝数：" + str(result[2]) + '\r\n')'''


def user_message(user_id):
    page_list_1 = driver.find_element_by_xpath("//div[@class='pa']")
    print(page_list_1.text)
    page_list_2 = re.findall(r"\d+\d*",page_list_1.text)
    #总共有多少页微博
    total_page = page_list_2[1]
    print("页数："+total_page)
    #第几页
    page_num=1
    #当前页的第几条微博内容
    curr_msg=1
    #全部微博中的第几条微博
    curr_msg_in_all = 0
    content_path="//div[@class='c'][{0}]"
    while(page_num <= int(total_page)):
        try:
            conten_url = "http://weibo.cn/" + user_id + "?page=" + str(page_num)
            driver.get(conten_url)
            content = driver.find_element_by_xpath(content_path.format(curr_msg)).text
            #print("\n" + content)                  # 微博内容，包含原创和转发
            if "设置:皮肤.图片.条数.隐私" not in content:
                curr_msg += 1
                curr_msg_in_all += 1
                temp=str(curr_msg_in_all)+content
                print(temp)

            else:
                page_num += 1
                curr_msg = 1
                time.sleep(20)
        except exception as e:
            print("curr_msg_in_all:" + curr_msg_in_all)
            print(e)
        finally:
            pass
    print("finish!")

if __name__ == '__main__':
    #输入微博账号
    username = '15037168088'
    #输入密码
    password = 'qscrgn123'
    #登录
    log_in(username, password)

    time.sleep(3)
    #部分域名
    uid='guangxianliuyan'
    #获取用户基本信息
    user_info(uid)
    #获取微博内容
    user_message(uid)
