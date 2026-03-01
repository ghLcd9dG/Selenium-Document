#导入库
from tkinter import *

#创建主窗口和标题
root=Tk()
root.title("selenium自动化爬虫")

#定义变量
variable=StringVar()
#设置默认值
#variable.set("test1")

optionmenu=OptionMenu(root,variable,"test1","test2","test3")
optionmenu.grid(row=0,column=0)

#窗体循环
mainloop()
