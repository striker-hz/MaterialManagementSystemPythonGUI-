#!/usr/bin/python3
# -*- coding:utf-8 -*-
# project:
# user:哦！再见
# Author: _bggacyy
# createtime: 2020/11/27 10:31


from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import sys
import time
from DataBaseProject import ConnDataBase,CountTime



class PlantVisual:
    def __init__(self):
        self.oneWin = Tk()
        self.Setting_Windows()
        self.setting_Component()
        self.oneWin.mainloop()
        self.oneWin.protocol("WM_DELETE_WINDOW", self.Close())

    def Close(self):
        """
        杀死进程,并且关闭数据库连接
        :return:
        """
        connData = ConnDataBase.Operation()
        connData.cur.close()
        connData.conn.close()
        sys.exit(0)

    def Setting_Windows(self):
        """
        对窗口基础信息进行设置
        :return:
        """
        self.oneWin.title('工厂物料简型操作系统')
        screenwidth = self.oneWin.winfo_screenwidth()
        screenheight = self.oneWin.winfo_screenheight()
        width = 600
        height = 400
        # 设置窗口在屏幕居中
        size = "%dx%d+%d+%d" % (width,
                                height,
                                (screenwidth - width) / 2,
                                (screenheight - height) / 2)
        self.oneWin.geometry(size)

    def setting_Component(self):
        """
        设置窗口组件
        :return:
        """
        # 第一个复选框设置
        label = Label(self.oneWin, text='请选择仓库：')
        label.place(x=30, y=40)
        self.material = StringVar()
        materialChoose = ttk.Combobox(
            self.oneWin,
            width=20,
            textvariable=self.material,
            state="readonly")
        ListOne = ["塑料", "五金原材料", "电子类材料", "电器类材料"]
        materialChoose['values'] = ListOne
        materialChoose.bind("<<ComboboxSelected>>", self.addCheckBox1)
        materialChoose.place(x=100, y=40)
        # 第二个复选框
        label_1 = Label(self.oneWin, text="选择物料:")
        label_1.place(x=310, y=40)
        self.material_1 = StringVar()
        self.material_1Choose = ttk.Combobox(
            self.oneWin, width=20, textvariable=self.material_1, state="readonly")
        # self.material_1Choose.bind("<<ComboboxSelected>>")
        self.material_1Choose.place(x=370, y=40)

        # 显示板
        self.showFrom = ttk.Treeview(self.oneWin, show="headings", height=7)
        self.showFrom.place(x=100, y=80)
        self.showFrom["columns"] = ("物料名", "库存")
        self.showFrom.column("物料名", width=85, anchor='center')
        self.showFrom.column("库存", width=85, anchor='center')
        self.showFrom.heading("物料名", text="物料名")
        self.showFrom.heading("库存", text="库存/吨")
        showButton = Button(self.oneWin, text="查看库存", command=self.showData)
        showButton.place(x=150, y=270)

        # 设置出库
        self.getValue1 = StringVar()
        Labelstock = Entry(self.oneWin, width=10, textvariable=self.getValue1)
        Labelstock.place(x=370, y=150)
        stockBtn = Button(self.oneWin, text="申请出库", command=self.StockOp)
        stockBtn.place(x=470, y=150)
        self.getValue2 = StringVar()
        LabelEnter = Entry(self.oneWin, width=10, textvariable=self.getValue2)
        LabelEnter.place(x=370, y=200)
        EnterBtn = Button(self.oneWin, text="申请入库", command=self.EnterOp)
        EnterBtn.place(x=470, y=200)

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
                list = [i[0], i[1]]
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
                    countime = CountTime.CountDown('出库', "出库成功")
                    # messagebox.showinfo("Message", "出库成功")
                else:
                    countime = CountTime.CountDown('出库', "出库成功，【库存数量不足】")
                    # messagebox.showinfo("Message", "出库失败，【库存数量不足】")
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
                    countime = CountTime.CountDown('入库',"入库成功")
                    # messagebox.showinfo("Message", "入库成功!")
                else:
                    countime = CountTime.CountDown('入库', "入库失败!")
                    # messagebox.showinfo("Message", "入库失败!")
            else:
                messagebox.showinfo("Message", "请选择入库物料!")
        else:
            messagebox.showinfo("Message", "请输入入库数量!")


# if __name__ == '__main__':
#     run = PlantVisual()
