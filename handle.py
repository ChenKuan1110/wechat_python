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

    def POST(self):
        """处理POST请求，接收消息"""
        try:
            webData = web.data()
            print("收到的消息是：\n" + webData.decode())
            recMsg = receive.parse_xml(webData)
            # 判断xml是否是消息类型
            if isinstance(recMsg, receive.Msg):
                toUser = recMsg.FromUserName  # 获取发送发
                fromUser = recMsg.ToUserName  # 获取消息接收方
                # 判断消息类型，回复消息
                if recMsg.MsgType == 'text':  # 文本消息
                    content = "文本内容"
                    replyMsg = reply.TextMsg(toUser, fromUser, content)
                    return replyMsg.send()
                if recMsg.MsgType == 'image':
                    mediaId = recMsg.MsgId  # 获取图片的mediaId
                    print("MediaId:" + mediaId)
                    replyMsg = reply.ImageMsg(toUser, fromUser, mediaId)
                    return replyMsg.send()
                else:  # 其他消息，暂不处理
                    return reply.Msg.send()

            else:
                print("暂不处理该消息")
                return reply.Msg.send()
        except Exception as e:
            print(e)
