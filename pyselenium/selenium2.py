# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://music.163.com/#/song?id=31877470")
driver.switch_to_frame("contentFrame")
time.sleep(5)
driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
driver.save_screenshot('D://代码//pyselenium//gg.png')  # 截图
b = driver.find_element_by_xpath("//a[starts-with(@class,'zbtn znxt')]")
b.click()
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//a[@data-type='reply']")))
    print(driver.page_source)
except NoSuchElementException:
    print('OMG')
finally:
        driver.quit()