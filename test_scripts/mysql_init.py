# -*- coding: UTF-8 -*=
import requests
import json
import time
import pymysql
class Operta_mysql(object):
    def __init__(self,host,port,user,password,db):
        
        self.host=host
        self.port=port
        self.user=user
        self.password=password
        self.db=db
        self.connect=pymysql.connect(self.host,self.user,self.password,self.db,self.port,charset='utf8')
        


    def delete(self,sql):
        self.connect.ping(reconnect=True)
        self.cursor=self.connect.cursor()
        
        try:
            for i in sql.split(";"):
               
                self.cursor.execute(i)
                self.connect.commit()
            print("删除成功")
            return True
        except:
            self.connect.rollback()
            return False
        finally:
            self.cursor.close()



    def select(self,sql):
        self.connect.ping(reconnect=True)
        self.cursor=self.connect.cursor()
        try:
           
            self.cursor.execute(sql)
            data=self.cursor.fetchall()
            
            # for select_data in data:
            #      print(select_data)
            return data
        except:
            print("没有返回数据")
        finally:
            self.cursor.close()
        

    def updata(self,sql):
        self.connect.ping(reconnect=True)
        self.cursor=self.connect.cursor()
        try:
            for i in sql.split(";"):
                self.cursor.execute(i)
                self.connect.commit()
            return True
        except:
            self.connect.rollback()
            return False
      

    def close_db(self):
        self.connect.close()

if __name__ == "__main__":
    Operta=Operta_mysql('10.32.1.2',3306,'root','8YBibPmekK9LXcWsFnHw','db_user')
    sql="select userid from user_user where phone = 36552518 or userid =23540197"
    Operta.select(sql)
        