#!/usr/bin/python3
# -*- coding:utf-8 -*-
# project:
# user:哦！再见
# Author: _bggacyy
# createtime: 2020/12/2 20:49
import time
from tkinter.ttk import Entry
import sys
from DataBaseProject import TestProjectOne, ConnDataBase, CountTime
from tkinter import Tk, StringVar
from tkinter import Button, ttk, messagebox, Label


class PlantVisualAdmin:
    def __init__(self):
        self.adminWin = Tk()
        self.SettingWindow()
        self.SettingComponent()
        self.get_time()
        self.adminWin.mainloop()
        self.adminWin.protocol("WM_DELETE_WINDOW", self.Close())
    def Close(self):
        """
        杀死进程,并且关闭数据库连接
        :return:
        """
        connData = ConnDataBase.Operation()
        connData.cur.close()
        connData.conn.close()
        sys.exit(0)

    def SettingWindow(self):
        self.adminWin.title("Admin")
        screenwidth = self.adminWin.winfo_screenwidth()
        screenheight = self.adminWin.winfo_screenheight()
        width = 600
        height = 400
        # 设置窗口在屏幕居中
        size = "%dx%d+%d+%d" % (width,
                                height,
                                (screenwidth - width) / 2,
                                (screenheight - height) / 2)
        self.adminWin.geometry(size)

    def SettingComponent(self):

        # 第一个复选框设置
        label = Label(self.adminWin, text='请选择仓库：')
        label.place(x=30, y=40)
        self.material = StringVar()
        materialChoose = ttk.Combobox(
            self.adminWin,
            width=20,
            textvariable=self.material,
            state="readonly")
        ListOne = ["塑料", "五金原材料", "电子类材料", "电器类材料"]
        materialChoose['values'] = ListOne
        materialChoose.bind("<<ComboboxSelected>>", self.addCheckBox1)
        materialChoose.place(x=100, y=40)

        # 第二个复选框
        label_1 = Label(self.adminWin, text="请选择物料:")
        label_1.place(x=30, y=80)
        self.material_1 = StringVar()
        self.material_1Choose = ttk.Combobox(
            self.adminWin,
            width=20,
            textvariable=self.material_1,
            state="readonly")
        # self.material_1Choose.bind("<<ComboboxSelected>>",self.alterPrice)
        self.material_1Choose.place(x=100, y=80)

        self.showFrom = ttk.Treeview(self.adminWin, show="headings", height=7)
        self.showFrom.place(x=310, y=40)
        self.showFrom["columns"] = ("物料名", "库存", "价格")
        self.showFrom.column("物料名", width=85, anchor='center')
        self.showFrom.column("库存", width=85, anchor='center')
        self.showFrom.column("价格", width=85, anchor='center')
        self.showFrom.heading("物料名", text="物料名")
        self.showFrom.heading("库存", text="库存/吨")
        self.showFrom.heading("价格", text="¥/吨")
        showButton = Button(self.adminWin, text="  查看库存  ", command=self.showData)
        showButton.place(x=320, y=250)

        showButton2 = Button(self.adminWin,text = "  转仓须知  ",command = self.showMessage)
        showButton2.place(x = 470,y = 250)

        self.getValue1 = StringVar()
        Labelstock = Entry(self.adminWin, width=10, textvariable=self.getValue1)
        Labelstock.place(x=30, y=200)
        stockBtn = Button(self.adminWin, text="  申请出库  ", command=self.StockOp)
        stockBtn.place(x=150, y=200)

        self.getValue2 = StringVar()
        LabelEnter = Entry(self.adminWin, width=10, textvariable=self.getValue2)
        LabelEnter.place(x=30, y=250)
        EnterBtn = Button(self.adminWin, text="  申请入库  ", command=self.EnterOp)
        EnterBtn.place(x=150, y=250)

        self.getValue3 = StringVar()
        LabelEnter = Entry(self.adminWin, width=10, textvariable=self.getValue3)
        LabelEnter.place(x=30, y=300)
        EnterBtn = Button(self.adminWin, text="  修改价格  ",command = self.alterPrice)
        EnterBtn.place(x=150, y=300)

        label_2 = Label(self.adminWin, text='请选转入仓：')
        label_2.place(x=30, y=120)
        self.material_2 = StringVar()
        materialChoose = ttk.Combobox(
            self.adminWin,
            width=20,
            textvariable=self.material_2,
            state="readonly")
        # ListOne = ["塑料", "五金原材料", "电子类材料", "电器类材料"]
        materialChoose['values'] = ListOne
        materialChoose.place(x=100, y=120)

        alterBtn = Button(self.adminWin, text="  确认转仓  ",command =self.alterBank)
        alterBtn.place(x=150, y=160)

    def get_time(self):
        """
        显示当前时间
        :return:
        """
        global time1
        time1 = ''
        time2 = time.strftime('%Y-%m-%d %H:%M:%S')
        # 能动态显示系统时间
        if time2 != time1:
            time1 = time2
            clock = Label(self.adminWin, text=time1, font=28)
            clock.configure(text=time2)
            clock.place(x=320, y=350)
            clock.after(200, self.get_time)

    def addCheckBox1(self, *args):
        """
        下拉列表绑定的事件和功能
        :param args:
        :return:
        """
        listTable = [
            "materialone",
            'materialtwo',
            'materialthree',
            'materialfour']
        ListTwo = []
        tableName = self.material.get()
        connData = ConnDataBase.Operation()
        if tableName == '塑料':
            ListTwo = connData.selectList(listTable[0])
        elif tableName == "五金原材料":
            ListTwo = connData.selectList(listTable[1])
        elif tableName == "电子类材料":
            ListTwo = connData.selectList(listTable[2])
        elif tableName == "电器类材料":
            ListTwo = connData.selectList(listTable[3])
        self.material_1Choose['values'] = ListTwo
        self.material_1Choose.current(0)
        return ListTwo

    def showData(self, *args):
        """
        查看库存按钮事件驱动
        :param args:
        :return:
        """
        tableName = self.material.get()
        if tableName != "":
            listTable = [
                "materialone",
                'materialtwo',
                'materialthree',
                'materialfour']
            ListBoard = []
            # print(tableName)
            connData = ConnDataBase.Operation()
            if tableName == '塑料':
                ListBoard = connData.showBoard(listTable[0])
            elif tableName == "五金原材料":
                ListBoard = connData.showBoard(listTable[1])
            elif tableName == "电子类材料":
                ListBoard = connData.showBoard(listTable[2])
            elif tableName == "电器类材料":
                ListBoard = connData.showBoard(listTable[3])
            # 每次显示前清空表格
            x = self.showFrom.get_children()
            for item in x:
                self.showFrom.delete(item)
            # 讲获取的值显示在表格上
            for i in ListBoard:
                list = [i[0], i[1], i[2]]
                self.showFrom.insert("", 'end', values=list)
        else:
            messagebox.showinfo("Message", "请选择物料!")
    def StockOp(self):
        value = self.getValue1.get()  # 获取出库数量
        if value != "":
            name = self.material_1.get()  # 获取复选框的物料小类的值
            # 得到对应数据库
            if name != "":
                listTable = [
                    "materialone",
                    'materialtwo',
                    'materialthree',
                    'materialfour']
                index = False
                tableName = self.material.get()
                connData = ConnDataBase.Operation()
                if tableName == '塑料':
                    index = connData.UpdateOne(listTable[0], value, name)
                elif tableName == "五金原材料":
                    index = connData.UpdateOne(listTable[1], value, name)
                elif tableName == "电子类材料":
                    index = connData.UpdateOne(listTable[2], value, name)
                elif tableName == "电器类材料":
                    index = connData.UpdateOne(listTable[3], value, name)
                if index:
                    # countime = CountTime.CountDown('出库', "出库成功")
                    messagebox.showinfo("Message", "出库成功")
                else:
                    # countime = CountTime.CountDown('出库', "出库成功，【库存数量不足】")
                    messagebox.showinfo("Message", "出库失败，【库存数量不足】")
            else:
                messagebox.showinfo("Message", "请选择出库物料")
        else:
            messagebox.showinfo("Message", "请输入出库数量!")

    def EnterOp(self):
        value = self.getValue2.get()  # 获取入库数量
        if value != "":
            name = self.material_1.get()  # 获取复选框的物料小类的值
            if name != "":
                listTable = [
                    "materialone",
                    'materialtwo',
                    'materialthree',
                    'materialfour']
                index = False
                tableName = self.material.get()  # 获取大类的值
                connData = ConnDataBase.Operation()
                # 得到对应数据库
                if tableName == '塑料':
                    index = connData.UpdateTwo(listTable[0], value, name)
                elif tableName == "五金原材料":
                    index = connData.UpdateTwo(listTable[1], value, name)
                elif tableName == "电子类材料":
                    index = connData.UpdateTwo(listTable[2], value, name)
                elif tableName == "电器类材料":
                    index = connData.UpdateTwo(listTable[3], value, name)
                if index:
                    # countime = CountTime.CountDown('入库',"入库成功")
                    messagebox.showinfo("Message", "入库成功!")
                else:
                    countime = CountTime.CountDown('入库', "入库失败!")
                    messagebox.showinfo("Message", "入库失败!")
            else:
                messagebox.showinfo("Message", "请选择入库物料!")
        else:
            messagebox.showinfo("Message", "请输入入库数量!")
    def alterPrice(self):
        global index
        name = self.material_1.get()
        price = self.getValue3.get()
        tableName = self.material.get()
        if tableName!="" and name!="" and price!= "":
            if tableName != "":
                listTable = [
                    "materialone",
                    'materialtwo',
                    'materialthree',
                    'materialfour']
                connData = ConnDataBase.Operation()
                if tableName == '塑料':
                    index = connData.updateThree(listTable[0], name, price)
                elif tableName == "五金原材料":
                    index = connData.updateThree(listTable[1], name, price)
                elif tableName == "电子类材料":
                    index = connData.updateThree(listTable[2], name, price)
                elif tableName == "电器类材料":
                    index = connData.updateThree(listTable[3], name, price)

                if index:
                    messagebox.showinfo("Message", "改价成功")
                else:
                    messagebox.showinfo("Message", "改价失败")
        else:
            messagebox.showinfo("Message","请选择物料或输入价格")
    def alterBank(self):
        global index
        tableName1 = self.material.get()
        name = self.material_1.get()
        tableName2 = self.material_2.get()
        print(tableName1,name,tableName2)
        if tableName1 != "":
            listTable = [
                "materialone",
                'materialtwo',
                'materialthree',
                'materialfour']
            connData = ConnDataBase.Operation()
            if tableName1 == '塑料':
                if tableName2 == "五金原材料":
                    index = connData.alter(listTable[0], name, listTable[1])
                elif tableName2 == "电子类材料":
                    index = connData.alter(listTable[0], name, listTable[2])
                elif tableName2 == "电器类材料":
                    index = connData.alter(listTable[0], name, listTable[3])
                else:
                    index = connData.alter(listTable[0], name, listTable[0])
            elif tableName1 == "五金原材料":
                if tableName2 == "塑料":
                    index = connData.alter(listTable[1], name, listTable[0])
                elif tableName2 == "电子类材料":
                    index = connData.alter(listTable[1], name, listTable[2])
                elif tableName2 == "电器类材料":
                    index = connData.alter(listTable[1], name, listTable[3])
                else:
                    index = connData.alter(listTable[1], name, listTable[1])
            elif tableName1 == "电子类材料":
                if tableName2 == "塑料":
                    index = connData.alter(listTable[2], name, listTable[0])
                elif tableName2 == "五金原材料":
                    index = connData.alter(listTable[2], name, listTable[1])
                elif tableName2 == "电器类材料":
                    index = connData.alter(listTable[2], name, listTable[3])
                else:
                    index = connData.alter(listTable[2], name, listTable[2])
            elif tableName1 == "电器类材料":
                if tableName2 == "塑料":
                    index = connData.alter(listTable[3], name, listTable[0])
                elif tableName2 == "五金原材料":
                    index = connData.alter(listTable[3], name, listTable[1])
                elif tableName2 == "电子类材料":
                    index = connData.alter(listTable[3], name, listTable[2])
                else:
                    index = connData.alter(listTable[3], name, listTable[3])
            if index:
                messagebox.showinfo("Message", "转仓成功")
            else:
                messagebox.showinfo("Message", "转仓失败")



    def showMessage(self):
        str = "若转仓，请先选择物料，再选择要转的仓"
        messagebox.showinfo("Message",str)


# if __name__ == '__main__':
#     p = PlantVisualAdmin()
