"""
同一获取Access_Token
"""
import urllib.request
import time
import json
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


class Basic():

    def __init__(self):
        self.__accessToken = ''
        self.__leftTime = 0

    def __real_get_access_token(self):
        """获取Access_token"""
        appId = "wxc331578ee40046ba"
        appSecret = "4f7234f604b6e71207b475f9318e5d7d"
        postUrl = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential" \
                  "&appid=APPID&secret=APPSECRET".replace('APPID', appId).replace('APPSECRET', appSecret)
        urlResp = urllib.request.urlopen(postUrl)
        urlResp = json.loads(urlResp.read())
        self.__accessToken = urlResp['access_token']
        self.__leftTime = urlResp['expires_in']

    def get_access_token(self):
        if self.__leftTime < 10:
            self.__real_get_access_token()
        return self.__accessToken

    def run(self):
        while True:
            if self.__leftTime > 10:
                time.sleep(2)
                self.__leftTime -= 2
            else:
                self.__real_get_access_token()


if __name__ == '__main__':
    basic = Basic()
    token = basic.get_access_token()
    print(token)
