import threading                            # 导入threading模块
import time                             # 导入time模块
class thread_test(threading.Thread):                   # 通过继承创建类
    def __init__(self,threadname):                  # 初始化方法
        threading.Thread.__init__(self,name = threadname)
    def run(self):                          # 重载run方法
        global number                        # 使用global表明number为全局变量
                   # 调用lock的acquire方法
        number = number + 1
        time.sleep(1)
        print("the value of number is {}".format(number))
             # 调用lock的release方法
          # 类实例化
threadlist = []                          # 定义列表
for i in range(5):
    t = thread_test(str(i))            # 类实例化
    threadlist.append(t)              # 将类对象添加到列表中
number=0                   # 将number赋值为0
for i in threadlist:
    i.start()                     # 依次运行线程