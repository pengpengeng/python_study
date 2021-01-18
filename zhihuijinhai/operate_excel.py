# -*- coding: UTF-8 -*=
import xlrd
import json
from mysql_init import Operta_mysql
import requests
data=xlrd.open_workbook("C:/Users/zhongquan/Desktop/DATA2.xls")
table=data.sheets()[0]

def opermysql():
    init_sql = "SELECT userid from db_user.user_user WHERE phone= "
    with open("test_scripts/config.json",'r') as f:
        data=json.loads(f.read())
        
    Operta=Operta_mysql(data["host"],data["port"],data["user"],data["password"],data['db'])
    string_datas=""
    for i in table.col_values(0):
        print(i)
        sql=init_sql+str(int(i))
    
        result=Operta.select(sql)
        
        for i in result:
            string_datas+="  "+str(i[0])
            #删除用户
            # userid=str(i[0])
            # sql="DELETE FROM db_user.user_user WHERE userid="+userid+";DELETE FROM db_user.user_info WHERE userid="+userid+";DELETE FROM db_user.user_kychistory WHERE userid="+userid+";DELETE FROM db_user.user_auth WHERE userid="+userid+";DELETE FROM db_user.user_app_user WHERE userid="+userid+";delete from db_user.user_bankcard  where userid = "+userid+";delete from db_user.user_history where userid = "+userid+";delete from db_user.user_invitecode where userid = "+userid+";delete from db_user.user_withdrawadress where userid = "+userid
            # print(userid,Operta.delete(sql))
    
    print(string_datas)

def get_token():
    header={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        "Accept": "application/json","AuthorizationId": "0f5cdcfc-1bbd-4c86-82bc-2ea6a56c65b5"}
    for i in table.col_values(0):
        
        data='{"password":"zhang521.","phone":"'+str(int(i))+'","function":1,"areaCode":"86"}'
        res=requests.post(url="https://test.fameex.com/userapi/user/temptoken/gettemptoken",headers=header,data=data).json()
        json.dumps(res)
        temporary_token=res['data']['token']


        header1={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        "Accept": "application/json","AuthorizationId": "0f5cdcfc-1bbd-4c86-82bc-2ea6a56c65b5","Authorization":temporary_token}

        data1='{"channel":1,"codeType":2,"loginType":1,"phone":"'+str(int(i))+'","areaCode":"86","code":"abcdef"}'
        res1=requests.post(url="https://test.fameex.com/userapi/user/login/login",headers=header1,data=data1).json()
        json.dumps(res1)
        
        if "data" in res1:
         
            gettoken=res1['data']['token']
            print(gettoken)
        else:
            
            print("接口报错",str(int(i)))

if __name__ == "__main__":
    #获取token
    #get_token()

    #查找添加用户或删除用户
    opermysql()