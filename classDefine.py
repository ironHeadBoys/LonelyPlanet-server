

#用户类，模拟
class User:
    def __init__(self, userName = '', pwd = ''):
        self.userName = userName
        self.pwd = pwd


'''
用户使用到的关于地点卡片，藏宝....的基类
其余扩展继承自该类
'''
class BaseLocationObj:
    def __init__(self, longitude, latitude, type, userId):
        self.longitude = longitude
        self.latitude = latitude
        self.type = type
        self.userId = userId

    def __init__(self, jsonString):
        print(jsonString)

    def __init__(self, paramDic):
        print(paramDic)

