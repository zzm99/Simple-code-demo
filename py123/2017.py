# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from requests_html import HTMLSession
import csv

session = HTMLSession()

file = open('2016.csv', 'a+', newline='')
csvwriter = csv.writer(file)
#csvwriter.writerow(['科类','院系', '专业', '最高分', '最低分', '平均分', '省份', '年份'])

links = [#'http://admission.sysu.edu.cn/zs01/zs01c/henan/2018n.htm',
         #'http://admission.sysu.edu.cn/zs01/zs01c/fujian/2018n.htm',
         #'http://admission.sysu.edu.cn/zs01/zs01c/guangxi/2018n.htm',
         #'http://admission.sysu.edu.cn/zs01/zs01c/yunnan/2018n.htm',
         #'http://admission.sysu.edu.cn/zs01/zs01c/anhui/2018n.htm',
         #'http://admission.sysu.edu.cn/zs01/zs01c/hainan/2018n.htm',
         #'http://admission.sysu.edu.cn/zs01/zs01c/heilongjiang/2018n.htm',
         #'http://admission.sysu.edu.cn/zs01/zs01c/beijing/2018n.htm',
         #'http://admission.sysu.edu.cn/zs01/zs01c/zhejiang/2017n.htm',
         'http://admission.sysu.edu.cn/zs01/zs01c/shanghai/2017n.htm',
         ]

for link in links:
    r = session.get(link)
    for i in range(50):
        shengfen = r.html.find('#cont > h1', first = True)
        kelei = r.html.find('#cont > table > tbody > tr:nth-child('+ str(i+9)+') > td:nth-child(3)', first=True)
        yuanxi = r.html.find('#cont > table > tbody > tr:nth-child('+ str(i+9)+') > td:nth-child(2)', first=True)
        zhuanye = r.html.find('#cont > table > tbody > tr:nth-child('+ str(i+9)+') > td:nth-child(1)', first=True)
        high = r.html.find('#cont > table > tbody > tr:nth-child('+ str(i+9)+') > td:nth-child(4)', first=True)
        low = r.html.find('#cont > table > tbody > tr:nth-child('+ str(i+9)+') > td:nth-child(5)', first=True)
        avg = r.html.find('#cont > table > tbody > tr:nth-child('+ str(i+9)+') > td:nth-child(6)', first=True)
        if kelei and yuanxi and zhuanye and high and low and avg:
            csvwriter.writerow([kelei.text, yuanxi.text, zhuanye.text, high.text, low.text, avg.text, shengfen.text.split('(')[1].split(')')[0], '2016'])
            print( shengfen.text.split('(')[1].split(')')[0])
        elif kelei and yuanxi and zhuanye and high and low:
            csvwriter.writerow([' ',kelei.text, yuanxi.text, zhuanye.text, high.text, low.text,shengfen.text.split('(')[1].split(')')[0], '2016'])
            print( shengfen.text.split('(')[1].split(')')[0])
        else:
            pass

file.close()


#cont > table > tbody > tr:nth-child(9) > td:nth-child(1) > font
















