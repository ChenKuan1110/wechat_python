"""消息接收
    从公众号后台发送过来的xml数据包
"""

import xml.etree.ElementTree as ET


def parse_xml(web_data):
    if len(web_data) == 0:
        return None
    xmlData = ET.fromstring(web_data)
    msg_type = xmlData.find('MsgType').text
    if msg_type == 'event':
        event_type = xmlData.find('Event').text
        if event_type == 'CLICK':
            return Click(xmlData)
        # elif event_type in ('subscribe', 'unsubscribe'):
        # return Subscribe(xmlData)
        # elif event_type == 'VIEW':
        # return View(xmlData)
        # elif event_type == 'LOCATION':
        # return LocationEvent(xmlData)
        elif event_type == 'scancode_waitmsg':
            return ScanCodePush(xmlData)
    elif msg_type == 'text':  # 文本消息
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


class EventMsg():
    """事件推送消息类"""

    def __init__(self, xmlData):
        self.ToUserName = xmlData.find('ToUserName').text
        self.FromUserName = xmlData.find('FromUserName').text
        self.CreateTime = xmlData.find('CreateTime').text
        self.MsgType = xmlData.find('MsgType').text
        self.Event = xmlData.find('Event').text


class Click(EventMsg):
    """Click菜单的推送消息类"""

    def __init__(self, xmlData):
        super().__init__(xmlData)
        self.EventKey = xmlData.find('EventKey').text


class ScanCodePush(EventMsg):
    """扫码等待事件的推送消息"""

    def __init__(self, xmlData):
        super().__init__(xmlData)
        self.EventKey = xmlData.find("EventKey").text
        self.ScanType = xmlData.find("ScanCodeInfo").find('ScanType').text
        self.ScanResult = xmlData.find("ScanCodeInfo").find("ScanResult").text
