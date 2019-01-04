"""
    处理服务器接入和消息管理
"""

import hashlib
import web
import receive
import reply


class Handle():
    """
        处理服务器接入和消息管理类
    """

    def GET(self):
        """处理Get请求，接入微信微信服务器"""
        try:
            data = web.input()
            if len(data) == 0:
                return "<h1>Hello,this is handle view</h1>"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = "kuange"

            s = sorted([timestamp, nonce, token])
            # 字典排序
            s = ''.join(s)
            hashcode = hashlib.sha1(s.encode('utf-8')).hexdigest()
            print('handle: GET hashcode: {} signature: {}'.format(hashcode, signature))
            if hashcode == signature:
                return echostr
            else:
                return ""
        except Exception as e:
            return e
