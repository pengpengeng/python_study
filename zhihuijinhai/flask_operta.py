# -*- coding: UTF-8 -*=
from flask import Flask,request
from mysql_init import Operta_mysql 
import json

test=Flask(__name__)
test.config['JSON_AS_ASCII'] = False
with open("test_scripts/config.json",'r') as f:
    data=json.loads(f.read())
    
Operta=Operta_mysql(data["host"],data["port"],data["user"],data["password"],data['db'])


@test.route('/delete')
def delete_user():
    '''
        删除用户信息
    '''
    userid=request.values.get('userid')
    if userid == None or userid=="":
        return {'msg':"参数不能为空"}
    else:
        print(userid)
        sql="DELETE FROM db_user.user_user WHERE userid="+userid+";DELETE FROM db_user.user_info WHERE userid="+userid+";DELETE FROM db_user.user_kychistory WHERE userid="+userid+";DELETE FROM db_user.user_auth WHERE userid="+userid+";DELETE FROM db_user.user_app_user WHERE userid="+userid+";delete from db_user.user_bankcard  where userid = "+userid+";delete from db_user.user_history where userid = "+userid+";delete from db_user.user_invitecode where userid = "+userid+";delete from db_user.user_withdrawadress where userid = "+userid
        result=Operta.delete(sql)
        Operta.close_db()
        
        if result ==True:
            return {'msg':"清理成功"}
        else:
            return {'msg':"error"}

        
@test.route("/addphone")
def add_phone():
    ''' 
        设置手机号
    '''

    userid=request.values.get('userid')
    phone=request.values.get('phone')
    area=request.values.get('area')
    if userid==None or phone==None or area==None or userid=="" or phone=="" or area=="":
        return {'msg':"参数不可为空"}
    else:
        sql='''
        UPDATE db_user.user_user set areacode=%s,phone=%s WHERE userid=%s;
        UPDATE db_user.user_info set phone=%s,phonevalidflag=1 WHERE userid=%s;
        UPDATE db_user.user_app_user set area_code=%s,phone=%s WHERE userid=%s;
        UPDATE db_user.user_auth set phonevalidflag=1 WHERE userid=%s
        ''' %(area,phone,userid,phone,userid,area,phone,userid,userid)
        print(sql)
        result=Operta.updata(sql)
        Operta.close_db()
        if result ==True:
                return {'msg':"修改成功"}
        else:
                return {'msg':"error"}


 



if __name__ == "__main__":
    test.run(host='0.0.0.0',debug=True,port=4421)
    #delete_user()

