# -*- coding: utf-8 -*-
from weibopy import WeiboOauth2, WeiboClient
import webbrowser

client_key = '4255203274' # 你的 app key
client_secret = '75589625cde7902ab73fab1df7844dfe' # 你的 app secret
redirect_url = 'https://api.weibo.com/oauth2/default.html'

auth = WeiboOauth2(client_key, client_secret, redirect_url)

# 获取认证 code
webbrowser.open_new(auth.authorize_url)

# 在打开的浏览器中完成操作
# 最终会跳转到一个显示 「微博 OAuth2.0」字样的页面
# 从这个页面的 URL 中复制 code= 后的字符串
# URL 类似这样 https://api.weibo.com/oauth2/default.html?code=9c88ff5051d273522700a6b0261f21e6

code = input('输入 code:')

# 使用 code 获取 token
token = auth.auth_access(code)

# token 是刚刚获得的 token，可以一直使用
client = WeiboClient(token['access_token'])

# suffix 指定 API 的名称，parmas 是参数，在文档中有详细描述
result = client.get(suffix='comments/show.json', params={'id': 4318237070487349, 'count': 200, 'page': 1})

from collections import defaultdict
import time
import re
province_list = defaultdict(list) # 保存按省划分的评论正文
comment_text_list = [] # 保存所有评论正文

# 获取「自杀式单身」评论列表
# 共获取 10 页 * 每页最多 200 条评论
for i in range(1, 11):
    result = client.get(suffix='comments/show.json', params={'id': 4322140368509204, 'count': 200, 'page': i})

    comments = result['comments']
    if not len(comments):
        break

    for comment in comments:
        text = re.sub('回复.*?:', '', str(comment['text']))
        province = comment['user']['province']
        province_list[province].append(text)
        comment_text_list.append(text)

    print('已抓取评论 {} 条'.format(len(comment_text_list)))
    time.sleep(1)