from flask import Flask, request, render_template
import os

server = Flask(__name__)

@server.route('/', methods = ['GET'])
def home():
    return 'home'

@server.route('/login', methods = ['POST'])
def login():
    userName = request.form['userName']
    pwd = request.form['passWord']
    #数据库读取账号密码，验证，将采取微信登录，需要验证微信




if __name__ == '__main__':
    server.run()

