#导入库
import tkinter as tk

#实例化对象
root=tk.Tk()
#设置标题
root.title("selenium 自动化爬虫")

#简单的函数
def hello_world():
    print("hello_world")

#创建按钮并居中
button=tk.Button(root,text="i'm a button",fg="blue",command=hello_world)
button.pack(fill=X)

#程序循环
root.mainloop()




