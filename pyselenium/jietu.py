# -*- coding: utf-8 -*-
# coding:utf-8

from selenium import webdriver
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument('--kiosk')
driver = webdriver.Chrome(chrome_options=options)
driver.get('http://p.zwjhl.com/price.aspx?url=http%3a%2f%2fitem.jd.com%2f4620979.html&bjid=853091835&ack=history')

a = driver.find_element_by_class_name("flot-overlay")
a.screenshot("test.png")
sleep(5)
driver.quit()