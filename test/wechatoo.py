# -*- coding: utf-8 -*-

"""
import itchat

itchat.login()

itchat.send(u'你好','filehelper')

"""

"""
#-*- coding:utf-8 -*-
import itchat
 
# 先登录
itchat.login()
 
# 获取好友列表
friends = itchat.get_friends(update=True)[0:]
print (u"昵称", u"性别", u"省份", u"城市")
for i in friends[0:]:
    print (i["NickName"], i["Sex"], i["Province"], i["City"])
"""

"""
#-*- coding:utf-8 -*-
import itchat
 
#获取好友列表
itchat.login() #登录
friends = itchat.get_friends(update=True)[0:]
 
#初始化计数器
male = 0
female = 0
other = 0
 
#1男性,2女性,3未设定性别
for i in friends[1:]: #列表里第一位是自己，所以从"自己"之后开始计算
    sex = i["Sex"]
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other += 1
#计算比例
total = len(friends[1:])
print (u"男性人数：", male)
print (u"女性人数：", female)
print (u"总人数：", total)
a = (float(male) / total * 100)
b = (float(female) / total * 100)
c = (float(other) / total * 100)
print (u"男性朋友：%.2f%%" % a)
print (u"女性朋友：%.2f%%" % b)
print (u"其他朋友：%.2f%%" % c)
 
#绘制图形
import matplotlib.pyplot as plt
labels = ['Male','Female','Unkown']
colors = ['red','yellowgreen','lightskyblue']
counts = [a, b, c]
plt.figure(figsize=(8,5), dpi=80)
plt.axes(aspect=1) 
plt.pie(counts, #性别统计结果
        labels=labels, #性别展示标签
        colors=colors, #饼图区域配色
        labeldistance = 1.1, #标签距离圆点距离
        autopct = '%3.1f%%', #饼图区域文本格式
        shadow = False, #饼图是否显示阴影
        startangle = 90, #饼图起始角度
        pctdistance = 0.6 #饼图区域文本距离圆点距离
)
plt.legend(loc='upper right',)
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.title(u'微信好友性别组成')
plt.show()
"""


 #-*-coding:utf-8 -*-
import urllib.request  
from time import ctime
from bs4 import BeautifulSoup
import itchat
def getPM25(cityname):
    site = 'http://www.pm25.com/' + cityname + '.html'
    page = urllib.request.urlopen(site)
    html = page.read();
    soup = BeautifulSoup(html.decode("utf-8"),"html.parser")
    city = soup.find(class_='bi_loaction_city')  # 城市名称
    aqi = soup.find("a", {"class", "bi_aqiarea_num"})  # AQI指数
    quality = soup.select(".bi_aqiarea_right span")  # 空气质量等级
    result = soup.find("div", class_='bi_aqiarea_bottom')  # 空气质量描述
    output=city.text + u'AQI指数：' + aqi.text + u'\n空气质量：' + quality[0].text + result.text
    print(output)
    print('*' * 20 + ctime() + '*' * 20)
    return output
itchat.auto_login(hotReload=True)
Help="Hello!友情提示：请输入城市拼音获取天气结果，如果无法识别，自动返回首都记录"
users = itchat.search_chatrooms(name='test')
#users = itchat.search_friends(name='-whisky')
userName = users[0]['UserName']
#userName = "filehelper"
itchat.send(Help,toUserName=userName)
@itchat.msg_register(itchat.content.TEXT, isFriendChat=True, isGroupChat=True, isMpChat=True)
def getcity(msg):
    cityname=msg['Text']
    result=getPM25(cityname)
    itchat.send(result,userName)

if __name__ == '__main__':
    itchat.run()



"""
#coding=utf8
import requests
import itchat

KEY = '1026c36a7b5649dfa52d2df424bb7e82'

def get_response(msg):
    # 这里我们就像在“3. 实现最简单的与图灵机器人的交互”中做的一样
    # 构造了要发送给服务器的数据
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : KEY,
        'info'   : msg,
        'userid' : 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        # 字典的get方法在字典没有'text'值的时候会返回None而不会抛出异常
        return r.get('text')
    # 为了防止服务器没有正常响应导致程序异常退出，这里用try-except捕获了异常
    # 如果服务器没能正常交互（返回非json或无法连接），那么就会进入下面的return
    except:
        # 将会返回一个None
        return

# 这里是我们在“1. 实现微信消息的获取”中已经用到过的同样的注册方法
@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    # 为了保证在图灵Key出现问题的时候仍旧可以回复，这里设置一个默认回复
    defaultReply = 'I received: ' + msg['Text']
    # 如果图灵Key出现问题，那么reply将会是None
    reply = get_response(msg['Text'])
    # a or b的意思是，如果a有内容，那么返回a，否则返回b
    # 有内容一般就是指非空或者非None，你可以用`if a: print('True')`来测试
    return reply or defaultReply

# 为了让实验过程更加方便（修改程序不用多次扫码），我们使用热启动
itchat.auto_login(hotReload=True)
itchat.run()

"""











