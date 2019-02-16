from tkinter import *

root=Tk()
root.title("selenium自动化爬虫")

test_dic=["test1","test2","test3","test4"]
variable=IntVar()

counter=0
for i in test_dic:
    counter+=1
    checkbutton=Radiobutton(root,text=i,variable=variable,value=counter,indicatoron=False)
    checkbutton.pack(fill=X)
mainloop()