# -*- coding: utf-8 -*-
from requests_html import HTMLSession
import csv

session = HTMLSession()

file = open('2016.csv', 'w', newline='')
csvwriter = csv.writer(file)
csvwriter.writerow(['科类','院系', '专业', '最高分', '最低分', '平均分', '省份', '年份'])

links = ['http://admission.sysu.edu.cn/zs01/zs01c/chongqing/2018n.htm',
         'http://admission.sysu.edu.cn/zs01/zs01c/guangdong/2018n.htm',
         'http://admission.sysu.edu.cn/zs01/zs01c/shandong/2018n.htm',
         'http://admission.sysu.edu.cn/zs01/zs01c/jiangsu/2018n.htm',
         'http://admission.sysu.edu.cn/zs01/zs01c/sichuan/2018n.htm',
         'http://admission.sysu.edu.cn/zs01/zs01c/henan/2018n.htm',
         'http://admission.sysu.edu.cn/zs01/zs01c/sichuan/2018n.htm',
         'http://admission.sysu.edu.cn/zs01/zs01c/hebei/2018n.htm',
         'http://admission.sysu.edu.cn/zs01/zs01c/shanxi/2018n.htm',
         'http://admission.sysu.edu.cn/zs01/zs01c/shanx/2018n.htm',
         'http://admission.sysu.edu.cn/zs01/zs01c/liaoning/2018n.htm',
         'http://admission.sysu.edu.cn/zs01/zs01c/qinghai/2018n.htm',
         'http://admission.sysu.edu.cn/zs01/zs01c/ningxia/2018n.htm',
         'http://admission.sysu.edu.cn/zs01/zs01c/neimenggu/2018n.htm',
         'http://admission.sysu.edu.cn/zs01/zs01c/jiangxi/2018n.htm',
         'http://admission.sysu.edu.cn/zs01/zs01c/jilin/2018n.htm',
         'http://admission.sysu.edu.cn/zs01/zs01c/hunan/2018n.htm',
         'http://admission.sysu.edu.cn/zs01/zs01c/hubei/2018n.htm',
         'http://admission.sysu.edu.cn/zs01/zs01c/yunnan/2018n.htm',
         'http://admission.sysu.edu.cn/zs01/zs01c/guizhou/2018n.htm',
         'http://admission.sysu.edu.cn/zs01/zs01c/xinjiang/2018n.htm',
         'http://admission.sysu.edu.cn/zs01/zs01c/gansu/2018n.htm',
         'http://admission.sysu.edu.cn/zs01/zs01c/xizang/2018n.htm',
         ]

for link in links:
    r = session.get(link)
    for i in range(50):
        shengfen = r.html.find('#cont > h1', first = True)
        kelei = r.html.find('#cont > table > tbody > tr:nth-child('+ str(i+9)+') > td:nth-child(3)', first=True)
        yuanxi = r.html.find('#cont > table > tbody > tr:nth-child('+ str(i+9)+') > td:nth-child(2)', first=True)
        zhuanye = r.html.find('#cont > table > tbody > tr:nth-child('+ str(i+9)+') > td:nth-child(1)', first=True)
        high = r.html.find('#cont > table > tbody > tr:nth-child('+ str(i+9)+') > td:nth-child(7)', first=True)
        low = r.html.find('#cont > table > tbody > tr:nth-child('+ str(i+9)+') > td:nth-child(8)', first=True)
        avg = r.html.find('#cont > table > tbody > tr:nth-child('+ str(i+9)+') > td:nth-child(9)', first=True)
        if kelei and yuanxi and zhuanye and high and low and avg:
            csvwriter.writerow([kelei.text, yuanxi.text, zhuanye.text, high.text, low.text, avg.text, shengfen.text.split('（')[1].split('）')[0], '2016'])
        elif kelei and yuanxi and zhuanye and high and low:
            csvwriter.writerow([' ',kelei.text, yuanxi.text, zhuanye.text, high.text, low.text,shengfen.text.split('（')[1].split('）')[0], '2016'])
        else:
            pass

file.close()

