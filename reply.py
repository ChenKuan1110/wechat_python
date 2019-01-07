"""消息发送"""

import time


class Msg():
    """发送消息基类"""

    def __init__(self):
        pass

    def send(self):
        return 'success'


class TextMsg(Msg):
    """发送的文本消息类"""

    def __init__(self, toUserName, fromUserName, content):
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['ToUserName'] = toUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['Content'] = content

    def send(self):
        """
            消息方法方法
        :return:  包含文本消息符合微信官方格式的xml数据包
        """
        xml_form = """
            <xml>
            <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
            <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
            <CreateTime>{CreateTime}</CreateTime>
            <MsgType><![CDATA[text]]></MsgType>
            <Content><![CDATA[{Content}]]></Content>
            </xml>
        """
        message = xml_form.format(**self.__dict)
        print("发送给公众号的消息是：" + message)
        return message


class ImageMsg(Msg):
    def __init__(self, toUserName, fromUserName, mediaId):
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['MediaId'] = mediaId

    def send(self):
        xml_form = """
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[image]]></MsgType>
        <Image>
        <MediaId><![CDATA[{MediaId}]]></MediaId>
        </Image>
        </xml>
        """
        message = xml_form.format(**self.__dict)
        print("发送给公众号的消息是：" + message)
        return message
