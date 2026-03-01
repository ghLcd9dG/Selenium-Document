
#导入库
from tkinter import *

#创建主窗口和标题
root=Tk()
root.title("selenium自动化爬虫")


labelframe= LabelFrame(root,text='Listbox',padx=5,pady=5)
labelframe.pack(padx=10,pady=10)


#定义scrollbar的属性和窗体
scrollbar=Scrollbar(labelframe)
scrollbar.pack(side=RIGHT,fill=Y)

#将Y轴控制设置为scrollbar
listbox=Listbox(labelframe,selectmode=SINGLE,yscrollcommand=scrollbar.set)
listbox.pack(side=LEFT,fill=BOTH)

dic=[]
for i in range(0,100):
    dic.append("text{}".format(i))
for i in dic:
    listbox.insert(END,i)

#负责实现拖动滚动条后窗体内容的改变
scrollbar.config(command=listbox.yview)

def delete():
    listbox.delete(ACTIVE)

button=Button(root,text="DELETE",command=delete)
button.pack(padx=5,pady=5)

mainloop()
