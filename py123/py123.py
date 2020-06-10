from requests_html import HTMLSession
import urllib.robotparser
from urllib.parse import urlparse

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
        print(r.html.find('head title')[0].text, link)

print('共爬取 {} 个链接'.format(len(visited)))