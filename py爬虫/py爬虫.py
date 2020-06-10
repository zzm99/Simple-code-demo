
#正常爬取
import requests
url = "https://item.jd.com/8735304.html"
try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:300])
except:
    print("爬取失败")

#伪装成浏览器来爬取
import requests
try: 
    kv = {'user-agent':'Mozillz/5.0'}
    url = "https://www.amazon.cn"
    r = requests.get(url, headers = kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[100:400])
except:
    print("爬取失败")

#搜索引擎关键字搜索爬取
import requests
keyword = "Python"
try:
    kv = {'wd' : keyword}
    r = requests.get("http://www.baidu.com/s",params = kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print("爬取失败")


#网络图片爬取和存贮
import requests
import os
url = "http://www.005.tv/uploads/allimg/181112/1425113c9-1.jpg"
root = "D://Pythonpachongpics//"
path = root + url.split('/')[-1]

try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")
except:
    print("爬取失败")
    
#ip地址查询全代码
import requests
url = "http://m.ip138.com/ip.asp?ip="
try:
    r = requests.get(url+'202.204.80.112')
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[-300:])
except:
    print("爬取失败")
    
    
















