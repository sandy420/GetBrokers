
# !/usr/bin/env python3.4
__author__ = 'Sanddy Heng'

import re,bs4,sys
import urllib.request
from random import choice
from time import sleep

def gethtml(http):
	proxy_support=urllib.request.ProxyHandler({'http':'http://'+ip})
	opener = urllib.request.build_opener(proxy_support)
	urllib.request.install_opener(opener)
	req = urllib.request.Request(http,headers=headers)
	html = urllib.request.urlopen(req).read()
	print(html)
	return html
def getName(html):
	_soup = bs4.BeautifulSoup(html)
	Info = _soup.findAll("div",attrs={"id":"houseRow_0_43474169"})
	print(Info)
	# jjrInfo = []
	# for i in range(len(Info)):
	# 	jjrname = str(re.findall(r'target="_blank">(.*?)</a>',str(Info[i]))[0])
	# 	jjrInfo.append(jjrname)
	# 	print(jjrname)
	return Info
if __name__=="__main__":
	http = "http://esf.taiyuan.fang.com/agenthome/-i3100-j310/"
	jjr_file = r"D:\temp\log\taiyuan.fang.txt"
	headers = {
		"Referer":"http://esf.taiyuan.fang.com/agenthome",
		"Host":"esf.taiyuan.fang.com",
		"Accept-Language":"zh-CN,zh;q=0.8",
		"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36"
	}

	iplist = ['101.71.27.120:80','221.10.102.203:82']
	ip = choice(iplist)
	doc = gethtml(http)