
#导入库
from tkinter import *

#创建主窗口和标题
root=Tk()
root.title("selenium自动化爬虫")

text=Text(root,width=36,height=2)
text.pack()

text.insert(END,"selenium自动化爬虫")

get_text=text.get("1.0","1.end")
text.insert(END,"\n")
text.insert(END,get_text)
text.delete("2.0",END)
#窗体循环
mainloop()
