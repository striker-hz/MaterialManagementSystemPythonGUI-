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
from DataBaseProject import SignInProject
from DataBaseProject import TestProjectOne,TestProjectTwo
import sys


class Login:
    def __init__(self):
        self.login = tkinter.Tk()
        self.SettingOne()
        self.SettingTwo()
        self.login.mainloop()
        self.login.protocol("WM_DELETE_WINDOW", self.Close())

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
        窗口基础设置
        :return:
        """
        self.login.title("工厂物料-登录")
        screenwidth = self.login.winfo_screenwidth()
        screenheight = self.login.winfo_screenheight()
        width = 400
        height = 300
        # 设置窗口在屏幕居中
        size = "%dx%d+%d+%d" % (width,
                                height,
                                (screenwidth - width) / 2,
                                (screenheight - height) / 2)
        self.login.geometry(size)

    def SettingTwo(self):
        """
        控件设置
        :return:
        """
        labelType = tkinter.Label(self.login,text = "登录类型")
        labelType.place(x = 80,y =50 )
        self.loginTypeStr = tkinter.StringVar()
        loginType = ttk.Combobox(self.login,width = 17,textvariable = self.loginTypeStr,state="readonly" )
        loginType.place(x =150,y = 50)
        loginTypeValueList = ["员工", "管理员"]
        loginType['values'] = loginTypeValueList


        labelUser = tkinter.Label(self.login, text="用户名")
        labelUser.place(x=80, y=90)
        self.textE1 = tkinter.StringVar()
        text1 = tkinter.Entry(
            self.login,
            textvariable=self.textE1)
        text1.place(x=150,y=90)

        labelPassword = tkinter.Label(self.login, text="密码")
        labelPassword.place(x=80, y=130)
        self.textE2 = tkinter.StringVar()
        text2 = tkinter.Entry(
            self.login,
            show='*',
            textvariable=self.textE2)
        text2.place(x=150,y=130)

        loginBtn = tkinter.Button(
            self.login,
            text="  登录  ",
            command=self.onClickLogin)
        loginBtn.place(x=130,y=180)
        SignInBtn = tkinter.Button(
            self.login,
            text="  注册  ",
            command=self.onCLickSignIn)
        SignInBtn.place(x=230,y=180)

    def onClickLogin(self):
        """
        登录按钮点击事件
        :return:
        """
        databases = ConnDataBase.Operation()
        UserNameLogin = self.textE1.get()
        PasswordLogin = self.textE2.get()
        loginType = self.loginTypeStr.get()
        if UserNameLogin != "" and PasswordLogin != "":
            indexLogin = databases.selectData(UserNameLogin, PasswordLogin,loginType)
            if indexLogin:
                if loginType == "员工":
                    tkinter.messagebox.showinfo('Message', '【{}】登录成功'.format(loginType))
                    self.login.destroy()
                    test = TestProjectOne.PlantVisual()
                else:
                    tkinter.messagebox.showinfo('Message', '【{}】登录成功'.format(loginType))
                    self.login.destroy()
                    test = TestProjectTwo.PlantVisualAdmin()
            else:
                tkinter.messagebox.showinfo('Message', '账号或密码错误')
        else:
            tkinter.messagebox.showinfo('Message', '账号或密码不能为空')

    def onCLickSignIn(self):
        """
        注册按钮点击事件
        :return:
        """
        self.login.destroy()
        signBtn = SignInProject.SignIn()


if __name__ == '__main__':
    login = Login()
