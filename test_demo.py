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

    