#导入库
from tkinter import *

#创建主窗口和标题
root=Tk()
root.title("selenium自动化爬虫")

def action():
    pass

menubar=Menu(root)

menu1=Menu(menubar,tearoff=0)
menu1.add_command(label="新建文件",command=action)
menu1.add_command(label="打开文件",command=action)
menu1.add_command(label="打开文件夹",command=action)
menubar.add_cascade(label="菜单",menu=menu1)


menu2=Menu(menubar,tearoff=0)
menu2.add_command(label="撤销",command=action)
menu2.add_command(label="重做",command=action)
menubar.add_cascade(label="编辑",menu=menu2)

root.config(menu=menubar)

#窗体循环
mainloop()
