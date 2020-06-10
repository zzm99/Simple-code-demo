import os
import re
import sqlite3
import requests
from win32.win32crypt import CryptUnprotectData


def getcookiefromchrome():
    host = '.taobao.com'
    cookies_str = ''
    cookiepath=os.environ['LOCALAPPDATA']+r"\Google\Chrome\User Data\Default\Cookies"
    sql="select host_key,name,encrypted_value from cookies where host_key='%s'" % host
    with sqlite3.connect(cookiepath) as conn:
        cu=conn.cursor()        
        cookies={name:CryptUnprotectData(encrypted_value)[1].decode() for host_key,name,encrypted_value in cu.execute(sql).fetchall()}
        for key,values in cookies.items():
                cookies_str = cookies_str + str(key)+"="+str(values)+';'
        return cookies_str

def getHTMLText(url):
    cookies = getcookiefromchrome()
    kv = {'cookie':cookies,'user-agent':'Mozilla/5.0'}
    try:
        r = requests.get(url, headers=kv, timeout=30)
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
   
def main():
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
    
main()

