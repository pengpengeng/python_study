# -*- coding: UTF-8 -*=
import requests
import json
import time
import pymysql
class classname(object):
    def __init__(self,host,port,user,password,db):
        self.host=host
        self.port=port
        self.user=user
        self.password=password
        self.db=db
        self.connect=pymysql.connect(self.host,self.port,self.user,self.password,self.db,charset='utf8')



    def delete(self,sql):
      
        self.cursor=self.connect.cursor()
        try:
            self.cursor.execute(sql)
            self.connect.commit()
        except:
            self.connect.rollback()
        finally:
            self.cursor.close()

    def select(self,sql):
        self.cursor=self.connect.cursor()
        try:
            self.cursor.execute(sql)
            data=self.cursor.fetchall()
            for select_data in data:
                print(select_data)
        except:
            print("没有返回数据")
        finally:
            self.cursor.close()

    def close_db(self):
        self.connect.close()