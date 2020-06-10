# -*- coding: utf-8 -*-
import base64  
from selenium import webdriver

#其他浏览器把Chrome换名就行
#option = webdriver.ChromeOptions()
#option.set_headless() 设置无头浏览器，就是隐藏界面后台运行

driver = webdriver.Chrome() #创建driver实例
#driver = webdriver.Chrome(chrome_options=option)  创建实例并载入option

url = 'http://p.zwjhl.com/price.aspx?url=http%3a%2f%2fitem.jd.com%2f4620979.html&bjid=853091835&ack=history'
driver.get(url)
#driver.maximize_window() 最大化窗口
#driver.set_window_size(width,height) 设置窗口大小


# 通过 toDataURL() 方法获取图片 base64 数据，并 return
getImgJS = 'return document.querySelector("#container > canvas.flot-overlay").toDataURL("image/png");'
# 执行 JS 代码并拿到图片 base64 数据
bg_img = driver.execute_script(getImgJS)
# 去除类型，只要数据部分
bg_img = bg_img[bg_img.find(',') + 1:]

img_data = base64.b64decode(bg_img)
file = open('bg.png', 'wb')
file.write(img_data)
file.close()
   
#print(driver.page_source) #打印网页源码
driver.quit() # 关闭浏览器