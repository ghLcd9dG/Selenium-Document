#导入库
from tkinter import *
from tkinter.filedialog import *

#创建主窗口和标题
root=Tk()
root.title("selenium自动化爬虫")

def choose():
    file_path=askopenfilename(filetypes=(('PNG', '.png'), ('JPG', '.jpg'), ('GIF', '.gif')))
    print(file_path)

button=Button(root,text="choose file",command=choose)
button.pack()

#窗体循环
mainloop()
