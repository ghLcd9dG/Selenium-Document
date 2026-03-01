#导入库
from tkinter import *

#创建主窗口和标题
root=Tk()
root.title("selenium自动化爬虫")

#Text控件
text=Text(root,width=36,height=2)
text.pack()

#插入字符
text.insert(END,"selenium自动化爬虫")

#设置
text.mark_set('mark1', '1.10') #第一行第三列做一个标记
text.mark_unset('mark1')
text.insert('mark1', 'MARK') #利用标记插入字符串
text.tag_config("tag1",background="BLACK",foreground="WHITE")
text.tag_add("tag1","1.10","1.14")


#窗体循环
mainloop()
