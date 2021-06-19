#!/usr/bin/python3
# -*- coding:utf-8 -*-
# project:
# user:哦！再见
# Author: _bggacyy
# createtime: 2020/12/2 20:02
import tkinter
import sys
import time
import threading
from tkinter import messagebox


class CountDown:
    def __init__(self,text,text2):
        self.textOne = text
        self.textTwo = text2
        self.timeWin = tkinter.Tk()
        self.SettingOne()
        t = threading.Thread(target=self.SettingTwo)
        t.start()
        self.timeWin.mainloop()
        self.timeWin.protocol("WM_DELETE_WINDOW", self.Close())

    def Close(self):
        sys.exit(0)

    def SettingOne(self):
        self.timeWin.title("请稍后")
        screenwidth = self.timeWin.winfo_screenwidth()
        screenheight = self.timeWin.winfo_screenheight()
        width = 400
        height = 200
        # 设置窗口在屏幕居中
        size = "%dx%d+%d+%d" % (width,
                                height,
                                (screenwidth - width) / 2,
                                (screenheight - height) / 2)
        self.timeWin.geometry(size)
        self.timeWin.resizable(False, False)

        self.Label1 = tkinter.Label(self.timeWin, fg='red',font = 15)
        self.Label1.place(x=50, y=80)
        Label2 = tkinter.Label(self.timeWin,fg = 'red',font = 15)
        Label2['text'] = "{}中".format(self.textOne)
        Label2.place(x = 150,y = 20)


    def SettingTwo(self):
        for i in range(5):
            self.Label1['text'] = '还有{}秒完成...请等待'.format(5 - i)
            time.sleep(1)
        self.timeWin.destroy()
        messagebox.showinfo("Message",self.textTwo)
