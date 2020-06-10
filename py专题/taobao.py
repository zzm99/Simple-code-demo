# -*- coding: utf-8 -*-
import re
import requests
import time
from selenium import webdriver

wd = webdriver.Chrome()
loginUrl = 'https://login.taobao.com/member/login.jhtml' 
wd.get(loginUrl) #进入登陆界面
 
time.sleep(30)#设定45秒睡眠，期间进行手动登陆。十分关键，下面有解释。
cookies = wd.get_cookies()#调出Cookies
req = requests.Session()
for cookie in cookies:
    req.cookies.set(cookie['name'],cookie['value'])
req.headers.clear() 


def getHTMLText(url):
    try:
        r = req.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
    
def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"',html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price, title])
    except:
        print("")
    
def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号","价格","商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))


goods = input('商品：')
depth = int(input('页数：'))
start_url = 'https://s.taobao.com/search?q=' + goods
infoList = []
print ("正在爬取···")
for i in range(depth):
    try:
        url = start_url + '&s=' + str(44*i)
        html = getHTMLText(url)
        parsePage(infoList, html)
    except:
        continue
printGoodsList(infoList)

