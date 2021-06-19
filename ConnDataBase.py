#!/usr/bin/python3
# -*- coding:utf-8 -*-
# project:
# user:哦！再见
# Author: _bggacyy
# createtime: 2020/11/27 11:22

import pymysql


class Operation:
    def __init__(self):
        """
        初始化连接
        """
        self.conn = pymysql.connect(
            host="",
            user="root",
            password="19990805",
            database="PlantMaterial",
            charset="utf8")
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def selectData(self, UserName, Password,status):
        """
        登录账号密码验证
        :param UserName:
        :param Password:
        :return:
        """
        indexSelect = False
        try:
            sql = "select * from UserTable where username = %s;"
            # 执行sql语句
            self.cur.execute(sql, [UserName])
            self.conn.commit()
            # 获取数据字典
            data = self.cur.fetchall()
            Key = 'Password'
            if data != "":
                dictData = dict(data[0])
                if Password == dictData['Password'] and status == dictData['status']:
                    indexSelect = True
            return indexSelect
        except Exception as e:
            self.conn.rollback()
            print(e)

    def SignIn(self, Name, UserName, password, Phone, Sex, Status):
        """
        注册账号
        :param Name:
        :param Status:
        :param Sex:
        :param UserName:
        :param password:
        :param Phone:
        :return:
        """
        indexInsert = False
        try:
            sql = "INSERT INTO UserTable (PName,UserName, Password,Phone,Sex,Status) VALUES (%s,%s,%s,%s,%s,%s);"
            self.cur.execute(sql, [Name, UserName, password, Phone, Sex, Status])
            self.conn.commit()
            index = self.selectData(UserName, password,Status)
            if index:
                indexInsert = True
            return indexInsert
        except Exception as e:
            self.conn.rollback()
            print(e)

    def getSql(self, tableName):
        """
        用来确定查询的数据库
        :param tableName:
        :return:
        """
        sql = ""
        if tableName == 'materialone':
            sql = "select * from MaterialOne;"
        elif tableName == 'materialtwo':
            sql = "select * from MaterialTwo;"
        elif tableName == 'materialthree':
            sql = "select * from Materialthree;"
        elif tableName == 'materialfour':
            sql = "select * from Materialfour;"
        return sql

    def selectList(self, tableName):
        """
        查询物料小类
        :param tableName:
        :return:
        """
        try:
            listData = []
            sql = self.getSql(tableName)
            # 执行sql语句
            self.cur.execute(sql)
            self.conn.commit()
            # 获取数据字典
            data = self.cur.fetchall()
            for i in data:
                listData.append(i["MatName"])
            # print(listData)
            return listData
        except Exception as e:
            self.conn.rollback()
            print(e)

    def showBoard(self, tableName):
        """
        查询库存
        :param tableName:
        :return:
        """
        try:
            listData = []
            sql = self.getSql(tableName)
            self.cur.execute(sql)
            self.conn.commit()
            data = self.cur.fetchall()
            for i in data:
                list = [i["MatName"], i["MatRepertory"], i["Price"]]
                listData.append(list)
            # print(listData)
            return listData
        except Exception as e:
            self.conn.rollback()
            print(e)

    def SelectMatRepertory(self, tableName, name):
        """
        查询指定小料的库存值
        :param tableName:
        :param name:
        :return:
        """
        try:
            sql = ""
            if tableName == 'materialone':
                sql = "select MatRepertory from MaterialOne where MatName=%s ;"
            elif tableName == 'materialtwo':
                sql = "select MatRepertory from MaterialTwo where MatName=%s;"
            elif tableName == 'materialthree':
                sql = "select MatRepertory from Materialthree where MatName=%s;"
            elif tableName == 'materialfour':
                sql = "select MatRepertory from Materialfour where MatName=%s;"
            self.cur.execute(sql, [name])
            self.conn.commit()
            valuesMatRepertory = self.cur.fetchall()
            return valuesMatRepertory[0]["MatRepertory"]
        except Exception as e:
            self.conn.rollback()
            print(e)

    def UpdateOne(self, tableName, value, name):
        """
        出库
        :param tableName:
        :param value:
        :param name:
        :return:
        """
        try:
            index = False
            valuedata = int(self.SelectMatRepertory(tableName, name))
            value = int(value)
            if (valuedata - value) >= 0:
                K = valuedata - value
                K = str(K)
                sql = ""
                if tableName == 'materialone':
                    sql = "update MaterialOne set MatRepertory = %s  where MatName = %s;"
                elif tableName == 'materialtwo':
                    sql = "update MaterialTwo  set MatRepertory = %s where MatName = %s;"
                elif tableName == 'materialthree':
                    sql = "update MaterialThree  set MatRepertory = %s where MatName = %s;"
                elif tableName == 'materialfour':
                    sql = "update MaterialFour set MatRepertory = %s  where MatName = %s;"
                self.cur.execute(sql, [K, name])
                self.conn.commit()
                index = True
            return index
        except Exception as e:
            self.conn.rollback()
            print(e)

    def UpdateTwo(self, tableName, value, name):
        """
        入库
        :param tableName:
        :param value:
        :param name:
        :return:
        """
        try:
            index = False
            valuedata1 = int(self.SelectMatRepertory(tableName, name))
            value = int(value)
            K = valuedata1 + value
            K = str(K)
            sql = ""
            if tableName == 'materialone':
                sql = "update MaterialOne set MatRepertory = %s  where MatName = %s;"
            elif tableName == 'materialtwo':
                sql = "update MaterialTwo  set MatRepertory = %s where MatName = %s;"
            elif tableName == 'materialthree':
                sql = "update MaterialThree  set MatRepertory = %s where MatName = %s;"
            elif tableName == 'materialfour':
                sql = "update MaterialFour set MatRepertory = %s  where MatName = %s;"
            self.cur.execute(sql, [K, name])
            self.conn.commit()
            valuedata2 = int(self.SelectMatRepertory(tableName, name))
            if valuedata2 == int(K):
                index = True
            return index
        except Exception as e:
            self.conn.rollback()
            print(e)
    def SelectPrice(self, tableName, name):
        """
        查询指定小料的价钱
        :param tableName:
        :param name:
        :return:
        """
        try:
            sql = ""
            if tableName == 'materialone':
                sql = "select Price from MaterialOne where MatName=%s ;"
            elif tableName == 'materialtwo':
                sql = "select Price from MaterialTwo where MatName=%s;"
            elif tableName == 'materialthree':
                sql = "select Price from Materialthree where MatName=%s;"
            elif tableName == 'materialfour':
                sql = "select Price from Materialfour where MatName=%s;"
            self.cur.execute(sql, [name])
            self.conn.commit()
            valuesPrice = self.cur.fetchall()
            return valuesPrice[0]["Price"]
        except Exception as e:
            self.conn.rollback()
            print(e)
    def updateThree(self,tableName,name,price):
        try:
            index = False
            sql = ""
            # price = int(price)
            if tableName == 'materialone':
                sql = "update MaterialOne set Price = %s  where MatName = %s;"
            elif tableName == 'materialtwo':
                sql = "update MaterialTwo  set Price= %s where MatName = %s;"
            elif tableName == 'materialthree':
                sql = "update MaterialThree  set Price = %s where MatName = %s;"
            elif tableName == 'materialfour':
                sql = "update MaterialFour set Price = %s  where MatName = %s;"
            self.cur.execute(sql, [price, name])
            self.conn.commit()
            value = self.SelectPrice(tableName,name)
            if int(value) == int(price):
                index = True
                print("改价成功")
            return index

        except Exception as e:
            self.conn.rollback()
            print(e)
    def alter(self,tableName,name,tableName2):
        global index
        try:
            sql = ""
            if tableName == 'materialone':
                sql = "select * from MaterialOne where MatName=%s ;"
            elif tableName == 'materialtwo':
                sql = "select * from MaterialTwo where MatName=%s;"
            elif tableName == 'materialthree':
                sql = "select * from Materialthree where MatName=%s;"
            elif tableName == 'materialfour':
                sql = "select * from Materialfour where MatName=%s;"
            self.cur.execute(sql, [name])
            self.conn.commit()
            data = self.cur.fetchall()
            MatName = data[0]["MatName"]
            MatRepertory = data[0]["MatRepertory"]
            Price = data[0]["Price"]
            self.alterInsert(tableName2,MatName,MatRepertory,Price)
            self.alterDelete(tableName,name)
            value = self.SelectMatRepertory(tableName2,name)
            if value!="":
                index = True
            return index
        except Exception as e:
            self.conn.rollback()
            print(e)
    def alterInsert(self,tableName,MatName,MatRepertory,Price):
        try:
            sql = ""
            if tableName == 'materialone':
                sql = "insert into  MaterialOne (MatName,MatRepertory,Price) values(%s,%s,%s);"
            elif tableName == 'materialtwo':
                sql = "insert into  MaterialTwo (MatName,MatRepertory,Price) values(%s,%s,%s);"
            elif tableName == 'materialthree':
                sql = "insert into  Materialthree (MatName,MatRepertory,Price) values(%s,%s,%s);"
            elif tableName == 'materialfour':
                sql = "insert into  Materialfour (MatName,MatRepertory,Price) values(%s,%s,%s); "
            self.cur.execute(sql,[MatName,MatRepertory,Price])
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(e)
    def alterDelete(self,tableName,name):

        try:
            sql = ""
            if tableName == 'materialone':
                sql = "delete from MaterialOne where MatName = %s;"
            elif tableName == 'materialtwo':
                sql = "delete from MaterialTwo where MatName = %s;"
            elif tableName == 'materialthree':
                sql = "delete from Materialthree where MatName = %s;"
            elif tableName == 'materialfour':
                sql = "delete from Materialfour where MatName = %s;"
            self.cur.execute(sql, [name])
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(e)




#
# if __name__ == '__main__':
#     test = Operation()
#     # test.SelectMatRepertory("materialone","通用塑料")
#     # test.updateThree("materialone","通用塑料",100)
#     test.alter("materialone","热固胶","materialtwo")
