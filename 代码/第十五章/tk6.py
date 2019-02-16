from tkinter import *


root=Tk()
root.title("selenium自动化爬虫")

test_dic=["test1","test2","test3","test4"]
variable=IntVar()

labelframe1= LabelFrame(root,text = 'choose one',padx = 5,pady = 5)
labelframe1.pack(padx = 10,pady = 10)

counter=0
for i in test_dic:
    counter+=1
    checkbutton=Radiobutton(labelframe1,text=i,variable=variable,value=counter,indicatoron=False)
    checkbutton.pack(fill=X)


mainloop()