# -*- coding: utf-8 -*-
# @Author: name
# @Date:   2018-08-01 19:15:54
# @Last Modified by:   name
# @Last Modified time: 2018-08-01 19:36:48
import win32api,win32con


#弹窗提示
'''
参数1代表系统，暂时只能为0
参数2代表消息内容
参数3代表标题
参数4代表不同的弹框类型从0-6有效
'''
#win32api.MessageBox(0, "数据采集全部完成\n共计xxx条\n", "Selnium自动化爬虫", 4)
# -*- coding: utf-8 -*-
#!/bin/env python

def test1():
    n=0
    for i in range(101):
        n+=i
    return n

def test2():
    return sum(range(101))

def test3():
    return sum(x for x in range(101))

if __name__=='__main__':
    from timeit import Timer
    t1=Timer("test1()","from __main__ import test1")
    t2=Timer("test2()","from __main__ import test2")
    t3=Timer("test3()","from __main__ import test3")
    print(t1.timeit(1000000))
    print(t2.timeit(1000000))
    print(t3.timeit(1000000))
