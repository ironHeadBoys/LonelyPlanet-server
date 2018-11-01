from flask import Flask, request, render_template
import os
import json

import cardBiz
import userBiz

server = Flask(__name__)

@server.route('/', methods = ['GET'])
def home():
    return 'home'

@server.route('/login', methods = ['POST'])
def login():
    param = request.form.to_dict()
    return userBiz.loginWithParam(param)
    #数据库读取账号密码，验证，将采取微信登录，需要验证微信


#上传一张卡片
@server.route('/uploadCard', methods = ['POST'])
def uploadCard():
    param = request.form.to_dict()
    return cardBiz.getCardWithParam(param)

#根据定位获取附近的卡片 参数：经纬度，用户id, 获取卡片范围(可空，为空时由服务器控制下发逻辑)
@server.route('/getCard', methods = ['POST'])
def getCard():
    param = request.form.to_dict()
    return cardBiz.getCardWithParam(param)

if __name__ == '__main__':
    server.run()

