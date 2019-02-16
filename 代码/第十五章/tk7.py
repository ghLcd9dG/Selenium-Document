
#导入库
from tkinter import *

#创建主窗口和标题
root=Tk()
root.title("selenium自动化爬虫")

def check():
    ID=entry1.get()
    password=entry2.get()

    checkID="1234567890"
    checkpassword="1234567890"
    if ID==checkID and password==checkpassword:
        print("you have logged in ")
        return True
    else:
        print("password error")
        return False

def check2():
    print("error")
    return True
#创建控件框架
labelframe1= LabelFrame(root,text ="登录框",padx = 5,pady = 5)
labelframe1.pack(padx = 10,pady = 10)

#输入框前面的文字部分
Label1=Label(labelframe1,text="账号")
#使用grid()方式进行布局
Label1.grid(row=0,column=0,padx=5,pady=5)

Label2=Label(labelframe1,text="密码")
Label2.grid(row=1,column=0,padx=5,pady=5)

#输入框
entry1=Entry(labelframe1)
#使用grid()方式进行布局
entry1.grid(row=0,column=1,padx=5,pady=5)
entry2=Entry(labelframe1,show="*",validate="focusout",validatecommand=check,invalidcommand=check2)
entry2.grid(row=1,column=1,padx=5,pady=5)

entry1.insert(0,"1234567890")

button=Button(root,text="登录",command=check)
button.pack(padx=5,pady=5)

mainloop()
