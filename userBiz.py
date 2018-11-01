#用户登录等相关操作

from flask import Flask, request, render_template
import os
import json


def loginWithParam(param):
    return json.dumps({'status': 0})