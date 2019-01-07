"""创建菜单界面"""

import urllib.request
from basic import Basic


class Menu():
    """菜单类"""

    def __init__(self):
        pass

    def create(self, postData, accessToken):
        """
            创建菜单的方法
        :param postData:   json格式的菜单字符串
        :param accessToken:  Access_Token
        :return:    创建菜单
        """
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/create?" \
                  "access_token=ACCESS_TOKEN".replace('ACCESS_TOKEN', accessToken)
        urlResp = urllib.request.urlopen(url=postUrl, data=postData.encode('utf-8'))
        print(urlResp.read())

    def query(self, accessToken):
        """
            查询菜单方法
        :param accessToken:
        :return: 菜单的json格式字符串
        """
        url = "https://api.weixin.qq.com/cgi-bin/menu/get?" \
              "access_token=ACCESS_TOKEN".replace("ACCESS_TOKEN", accessToken)
        urlResp = urllib.request.urlopen(url=url)
        print(urlResp.read())

    def delete(self, accessToken):
        """删除菜单方法"""
        url = "https://api.weixin.qq.com/cgi-bin/menu/delete?" \
              "access_token=ACCESS_TOKEN".replace("ACCESS_TOKEN", accessToken)
        urlResp = urllib.request.urlopen(url=url)
        print(urlResp.read())


if __name__ == '__main__':
    myMenu = Menu()
    postJson = """
    {
        "button":
        [
            {
                "type": "click",
                "name": "点击菜单",
                "key":  "click"
            },
            {
                "name": "视图菜单",
                "type": "view",
                "url": "https://www.baidu.com"
            },
            {
                "name": "扫描",
                "sub_button": 
                [
                    {
                        "name": "扫描1",
                        "type": "scancode_push",
                        "key": "scancode1"
                    },
                    {
                        "name": "扫描2",
                        "type": "scancode_waitmsg",
                        "key": "scancode2"
                    }
                ]
            }
          ]
    }
    """
    basic = Basic()
    token = basic.get_access_token()
    # myMenu.delete(token)
    myMenu.create(postData=postJson, accessToken=token)
