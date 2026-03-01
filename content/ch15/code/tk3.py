import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.say_hi = tk.Button(self,text="click me to say\nHello World",command=self.say_hi)
        #self.say_hi["text"] = "Hello World\n(click me)"
        #self.say_hi["command"] = self.say_hi
        self.say_hi.pack(side="top",pady=10)

        self.quit = tk.Button(self, text="退出", fg="blue",
                              command=root.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hello_world")


#实例化对象
root=tk.Tk()
#设置标题
root.title("selenium 自动化爬虫")

#类的继承
app = Application(master=root)
#程序循环
app.mainloop()