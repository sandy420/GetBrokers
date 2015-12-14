#!/usr/bin/env python3.4
# -*- coding:utf-8 -*-
__author__ = "sandy heng"

from os import makedirs
from os.path import exists

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


def GetAgent(browser,url):
    names = []
    tels = []
    try:
        browser.set_page_load_timeout(5)
        browser.implicitly_wait(30)
        browser.set_window_size(400, 200)
        print("开始下载→→→%s"% url)
        browser.get(url)
        name = browser.find_elements_by_css_selector(css_selector=conf.css_name_key)
        tel = browser.find_elements_by_css_selector(css_selector=conf.css_tel_key)
        for n in name:
            names.append(n.text)
        for t in tel:
            tels.append(t.text)
    except NoSuchElementException as err:
        print(err)
    return names,tels



if __name__ == '__main__':
    from Broker_spider import conf
    filename = input("请输入文件名：")
    browser = webdriver.Chrome("chromedriver.exe")
    if exists(conf.jjr_log_path) is False:
        makedirs(conf.jjr_log_path)
    file = conf.jjr_log_path+'/'+filename+'.txt'
    for i in range(1,conf.page_number):
        url = conf.url+'n'+str(i)
        n,t=GetAgent(browser,url)
        try:
            if len(n) == len(t):
                for num in range(len(n)):
                    Agent = n[num]+'\t'+t[num]+'\n'
                    with open(file,'a') as f:
                        f.write(Agent)
        except Exception as err:
            print(Exception)
    browser.close()