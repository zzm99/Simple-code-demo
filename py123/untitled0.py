# -*- coding: utf-8 -*-

'''
import urllib.robotparser

url = 'https://ai.baidu.com'
rp = urllib.robotparser.RobotFileParser()
rp.set_url(url + '/robots.txt')
rp.read()
info = rp.can_fetch("*", 'https://ai.baidu.com/tech/s peech/asr')
print(info)
'''

'''
from urllib.parse import urlparse
from requests_html import HTMLSession
session = HTMLSession()
origin = 'https://ai.baidu.com'
r = session.get(origin)
print(r.html.links)

domain = 'ai.baidu.com'

def is_inner_link(link):
    netloc = urlparse(link).netloc
    return (not netloc) or (netloc == domain)
	
for link in r.html.links:
    print(is_inner_link(link), link)
'''


from requests_html import HTMLSession
import urllib.robotparser
from urllib.parse import urlparse
import csv

file = open('link.csv', 'w', newline='')
csvwriter = csv.writer(file)
csvwriter.writerow(['标题', '链接'])

session = HTMLSession()
origin = 'https://ai.baidu.com'
domain = urlparse(origin).netloc

def is_inner_link(link):
    netloc = urlparse(link).netloc
    return (not netloc) or (netloc == domain)

visited = []         # 已访问链接列表
unvisited = [origin] # 待访问链接列表

# 解析爬虫协议
rp = urllib.robotparser.RobotFileParser()
rp.set_url(origin + '/robots.txt')
rp.read()

def add_unvisited(link):
    # 过滤1：判断爬虫协议是否允许
    allow = rp.can_fetch('*', link)
    if not allow:
        return
    
    # 过滤2：判断是否为内链
    if not is_inner_link(link):
        return

    # 过滤3：去掉非法链接
    path = urlparse(link).path
    if not path.startswith('/'):
        return
    
    # 过滤4：自定义过滤
    if urlparse(link).path.startswith(('/file', '/docs', '/support', '/forum', '/broad', '/paddlepaddle', '/market', '/download', '/facekit', '/sdk', '/customer', '/easydl', '//')):
        return

    # 将 /tech/123 转换为 https://ai.baidu.com/tech/123 的形式
    if link.startswith('/'):
        link = origin + link
    
    # 过滤5：判断是否访问过，或已经添加到待访问列表
    if (link in visited) or (link in unvisited):
        return

    unvisited.append(link)

while len(unvisited):
    link = unvisited.pop()
    r = session.get(link)
    visited.append(link)
    if r.html and r.html.links and len(r.html.links):
        for url in r.html.links:
            add_unvisited(url)

    if r.html.find('head title')[0]:
        #print(r.html.find('head title')[0].text, link)
        csvwriter.writerow([r.html.find('head title')[0].text, link])

file.close()
# print('共爬取 {} 个链接'.format(len(visited)))



'''
import csv

page_url = []
page_title = []
file = open('link.csv', 'r')
infos = csv.reader(file)
for info in infos:
    page_title.append(info[0])
    page_url.append(info[1])

while True:
    keyword = input('请输入查询关键字，输入 quit 结束：')
    if keyword == 'quit':
        break
    for i in range(len(page_title)):
        if str(page_title[i]).find(keyword) >= 0:
            print(page_url[i], page_title[i])

file.close()
'''