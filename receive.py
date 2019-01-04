"""消息接收"""

import xml.etree.ElementTree as ET


def parse_xml(web_data):
    if len(web_data) == 0:
        return None
    xmlData = ET.fromstring(web_data)
    msg_type = xmlData.find('MsgType').text
    if msg_type == 'text':  # 文本消息
        return TextMsg(xmlData)
    elif msg_type == 'image':  # 图片消息
        return ImageMsg(xmlData)


class Msg():
    """消息基类"""

    def __init__(self, xmlData):
        """初始化消息类"""
        self.ToUserName = xmlData.find('ToUserName').text
        self.FromUserName = xmlData.find('FromUserName').text
        self.CreateTime = xmlData.find('CreateTime').text
        self.MsgType = xmlData.find('MsgType').text
        self.MsgId = xmlData.find("MsgId").text


class TextMsg(Msg):
    """文本消息类"""

    def __init__(self, xmlData):
        """初始化文本消息"""
        super().__init__(xmlData)
        self.Content = xmlData.find('Content').text.encode('utf-8')


class ImageMsg(Msg):
    """图片消息类"""

    def __init__(self, xmlData):
        super().__init__(xmlData)
        self.PicUrl = xmlData.find('PicUrl').text
        self.MediaId = xmlData.find('MediaId').text
