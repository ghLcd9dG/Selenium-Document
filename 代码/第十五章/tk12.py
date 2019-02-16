#导入库
from tkinter import *

#创建主窗口和标题
root=Tk()
root.title("selenium自动化爬虫")


#Text控件
canvas=Canvas(root,width=500,height=300)
canvas.pack()

def track(motion):
    x1=motion.x-0.1
    x2=motion.x+0.1
    y1=motion.y-0.1
    y2=motion.y+0.1

    canvas.create_oval(x1,y1,x2,y2,fill="black")

canvas.bind("<B1-Motion>",track)


#窗体循环
mainloop()
