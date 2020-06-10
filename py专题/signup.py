# -*- coding: utf-8 -*-
'''
import requests
from selenium import webdriver
import time

wd = webdriver.Chrome() #构建浏览器
loginUrl = 'http://www.weibo.com/login.php' 
wd.get(loginUrl) #进入登陆界面

time.sleep(2)
wd.find_element_by_xpath('//*[@id="loginname"]').send_keys('13724661953') #输入用户名
wd.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[2]/div/input').send_keys('ZHENGZHUOMIN') #输入密码
wd.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a/span').click() #点击登陆
#wd.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[3]/div/input').send_keys(input("输入验证码： "))
#wd.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a').click()#再次点击登陆

req = requests.Session() #构建Session
cookies = wd.get_cookies() #导出cookie
for cookie in cookies:
    req.cookies.set(cookie['name'],cookie['value']) #转换cookies

print (req.cookies)
#test = req.get('待测试的链接')
'''

import time
import requests
from selenium import webdriver

wd = webdriver.Chrome()
loginUrl = 'http://www.weibo.com/login.php' 
wd.get(loginUrl) #进入登陆界面
 
time.sleep(45)#设定45秒睡眠，期间进行手动登陆。十分关键，下面有解释。
cookies = wd.get_cookies()#调出Cookies
req = requests.Session()
for cookie in cookies:
    req.cookies.set(cookie['name'],cookie['value'])
req.headers.clear() 
#test = req.get('待测试的链接') 
print(req.cookies)