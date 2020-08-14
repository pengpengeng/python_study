# -*- coding: UTF-8 -*-
from flask import Flask,request

app=Flask(__name__)

@app.route("/user")
def hello():

    return "this is dengbaolei "

def deng():
    return "这不是用构造函数"
app.add_url_rule(rule='/deng',view_func=deng)

def url_name(urlname):
    return "这是动态的url，名字是%s"%(urlname)

app.add_url_rule(rule='/deng/<urlname>',view_func=url_name)

@app.route("/login")
def get_demo():
    get_data =request.args.get('a','sdfdsf')
    #request.args,=获取传参
    return "获取的参数是%s%s"%(request.args,get_data)

@app.route("/login_post",methods=["POST"])
def post_demo():

    return ok

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
