#卡片的获取上传等逻辑

from flask import Flask, request, render_template
import os
import json


#根据参数返回卡片，返回值为httpResponse
def getCardWithParam(param):
    responseData = {'test': 'haha'}
    return json.dumps(responseData)


#根据参数保存，返回值为httpResponse
def upLoadCardWithParam(param):

#后续接入鉴黄api

    return  ""