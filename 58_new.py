# -*- coding: utf-8 -*-
# !/usr/bin/env python3.4
__author__ = 'Sanddy Heng'

import urllib.request
from bs4 import BeautifulSoup
import re
from ghost import Ghost
from random import choice


# def gethtml(HTTP):
# 	# ip = choice(iplist)
# 	# proxy_support=urllib.request.ProxyHandler({'http':'http://'+ip})
# 	# opener = urllib.request.build_opener(proxy_support)
# 	# urllib.request.install_opener(opener)
# 	req = urllib.request.Request(HTTP,headers=headers)
# 	HTML = urllib.request.urlopen(req).read()
# 	return HTML

def gethtml(URL):
	ghost = Ghost(wait_timeout=120)
	page, resources = ghost.open(URL)
	html = BeautifulSoup(ghost.content)
	print(html)

if __name__ == "__main__":
	web_Url = "http://cd.58.com/ershoufang/"
	JJR_FPATH = r"D:\temp\jjrlog\xiangyang.58.txt"
	print(web_Url)
	gethtml(web_Url)