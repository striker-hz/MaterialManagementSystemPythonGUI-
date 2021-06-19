#!/usr/bin/python3
# -*- coding:utf-8 -*-
# project:
# user:哦！再见
# Author: _bggacyy
# createtime: 2020/11/27 14:26

import tkinter
import tkinter.messagebox
from tkinter import ttk

from DataBaseProject import ConnDataBase
from DataBaseProject import LoginProject
import sys


class SignIn:
    def __init__(self):
        self.sign = tkinter.Tk()
        self.SettingOne()
        self.SettingTwo()
        self.sign.mainloop()
        self.sign.protocol("WM_DELETE_WINDOW", self.Close())

    def Close(self):
        """
        杀死进程,并且关闭数据库连接
        :return:
        """
        connData = ConnDataBase.Operation()
        connData.cur.close()
        connData.conn.close()
        sys.exit(0)

    def SettingOne(self):
        """
        基础设置
        :return:
        """
        self.sign.title("工厂物料-注册")
        screenwidth = self.sign.winfo_screenwidth()
        screenheight = self.sign.winfo_screenheight()
        width = 400
        height = 500
        # 设置窗口在屏幕居中
        size = "%dx%d+%d+%d" % (width,
                                height,
                                (screenwidth - width) / 2,
                                (screenheight - height) / 2)
        self.sign.geometry(size)

    def SettingTwo(self):
        """
        设置控件
        :return:
        """
        self.textE1 = tkinter.StringVar()
        label1 = tkinter.Label(self.sign, text="用户名").place(x=80, y=50)
        text1 = tkinter.Entry(
            self.sign,
            textvariable=self.textE1).place(
            x=150,
            y=50)

        self.textE2 = tkinter.StringVar()
        label2 = tkinter.Label(self.sign, text="密码").place(x=80, y=100)
        text2 = tkinter.Entry(
            self.sign,
            show='*',
            textvariable=self.textE2).place(
            x=150,
            y=100)

        self.textE3 = tkinter.StringVar()
        label3 = tkinter.Label(self.sign, text="电话").place(x=80, y=150)
        text3 = tkinter.Entry(
            self.sign,
            textvariable=self.textE3).place(
            x=150,
            y=150)

        self.textE4 = tkinter.StringVar()
        label4 = tkinter.Label(self.sign, text="姓名").place(x=80, y=200)
        text4 = tkinter.Entry(
            self.sign,
            textvariable=self.textE4).place(
            x=150,
            y=200)

        self.textE5 = tkinter.StringVar()
        label5 = tkinter.Label(self.sign, text="身份").place(x=80, y=250)
        signSex = ttk.Combobox(self.sign, width=17, textvariable=self.textE5, state="readonly")
        signSex.place(x=150, y=250)
        ValueList = ["员工"]
        signSex['values'] = ValueList

        self.textE6 = tkinter.StringVar()
        label5 = tkinter.Label(self.sign, text="性别").place(x=80, y=300)
        signStatus = ttk.Combobox(self.sign, width=17, textvariable=self.textE6, state="readonly")
        signStatus.place(x=150, y=300)
        ValueList = ["男", "女"]
        signStatus['values'] = ValueList


        signBtn = tkinter.Button(
            self.sign, text="注册", command=self.onCLickSignIn)
        signBtn.place(x=150, y=350)
        backBtn = tkinter.Button(
            self.sign, text="返回", command=self.onClickBack)
        backBtn.place(x=230, y=350)

    def onCLickSignIn(self):
        """
        注册按钮点击设置
        :return:
        """
        userName = self.textE1.get()
        passWord = self.textE2.get()
        Phone = self.textE3.get()
        name = self.textE4.get()
        status = self.textE5.get()
        sex = self.textE6.get()
        databases = ConnDataBase.Operation()
        if userName != "" and passWord != "" and Phone != "" and name != "" and status != "" and sex != "":
            indexSign = databases.SignIn(name,userName, passWord, Phone,sex,status)
            if indexSign:
                tkinter.messagebox.showinfo("Message", "注册成功")
                self.sign.destroy()
                login = LoginProject.Login()
            else:
                tkinter.messagebox.showinfo("Message", "注册失败")
        else:
            tkinter.messagebox.showinfo("Message", "输入不能为空")

    def onClickBack(self):
        """
        返回按钮点击设置
        :return:
        """
        self.sign.destroy()
        login = LoginProject.Login()


# if __name__ == '__main__':
#     signWin = SignIn()
