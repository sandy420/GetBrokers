# -*- coding: utf-8 -*-
# !/usr/bin/env python3.4
__author__ = 'Sanddy Heng'

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time,os

browser = webdriver.Firefox()
browser.get("http://esf.hf.fang.com/agenthome/")
assert "合肥搜房帮，中国最大的房地产经纪人网络平台-搜房网" in browser.title
elem = browser.find_element_by_xpath("/html/body/div[4]/div[5]/div[4]/div[1]/div[2]/div/div[3]/dl/dt/p[1]/a").is_displayed()
a= elem
print(a)
# elem.send_keys(Keys.RETURN)
# time.sleep(0.2)
# try:
# 	browser.find_elements_by_xpath("//div[dl/dt/p(@class,'black')]")
# except NoSuchElementException:
# 	assert 0,"没有发现相应内容。"
# browser.close()
