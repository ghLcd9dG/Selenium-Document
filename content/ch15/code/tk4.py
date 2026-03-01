from tkinter import *

root=Tk()
root.title("selenium自动化爬虫")

test_dic=["test1","test2","test3","test4"]
variable=[]

for i in test_dic:
    variable.append(IntVar())

    checkbutton=Checkbutton(root,text=i,variable=variable[-1])
    checkbutton.pack(anchor=W)

    label=Label(root,textvariable=variable[-1])
    label.pack()
mainloop()