# -*- coding: UTF-8 -*-
from flask import Flask
app=Flask(__name__)

@app.route("/user")
def hello():

    return "this is dengbaolei "

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)

