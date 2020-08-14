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

        
    

if __name__ == "__main__":
    test.run(host='0.0.0.0',debug=True,port=4421)
    #delete_user()

