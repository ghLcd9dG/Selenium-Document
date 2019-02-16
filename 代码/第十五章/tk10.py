
#导入库
from tkinter import *

#创建主窗口和标题
root=Tk()
root.title("selenium自动化爬虫")

text=Text(root,width=36,height=2)
text.pack()

text.insert(END,"selenium自动化爬虫")
text.tag_config("tag1",background="blue")
text.tag_add("tag1","1.0","1.end")

#窗体循环
mainloop()
