import requests
import re
import traceback
from bs4 import BeautifulSoup
import bs4
def getHTMLText(url):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
         return""
fpath = 'D://gupiao.txt'
html = getHTMLText('https://hq.gucheng.com/gpdmylb.html')
soup = BeautifulSoup(html,'html.parser')
a = soup.find_all('a')
lst=[]
for i in a:
    try:
        href = i.attrs['href']
        lst.append(re.findall(r"[S][HZ]\d{6}", href)[0])
    except:
        continue
lst = [item.lower() for item in lst] #将爬取信息转换小写
count = 0
for stock in lst:
    url = 'https://gupiao.baidu.com/stock/' + stock + ".html"
    html = getHTMLText(url)
    try:
        if html =="":
            continue
        infoDict = {}
        soup = BeautifulSoup(html,'html.parser')
        stockInfo = soup.find('div',attrs={'class':'stock-bets'})
             
        if isinstance(stockInfo,bs4.element.Tag):    #判断类型
            name = stockInfo.find_all(attrs={'class':'bets-name'})[0]
            infoDict.update({'股票名称':name.text.split()[0]})            
            keylist = stockInfo.find_all('dt')
            valuelist = stockInfo.find_all('dd')
            for i in range(len(keylist)):
                key = keylist[i].text
                val = valuelist[i].text
                infoDict[key] = val
                 
        with open(fpath,'a',encoding='utf-8') as f:
            f.write( str(infoDict) + '\n')
            count = count + 1
            print("\r当前速度：{:.2f}%".format(count*100/len(lst)),end="")
    except:
        count = count + 1
        print("\r当前速度：{:.2f}%".format(count*100/len(lst)),end="")
        traceback.print_exc()
        continue