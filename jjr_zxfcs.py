# -*- coding: utf-8 -*-
# !/usr/bin/env /usr/local/bin/python3.4
# Python Version 3.4
__author__ = 'Sanddy Heng'

import urllib.request
from random import choice
import bs4,re


def gethtml(http):
	proxy_support=urllib.request.ProxyHandler({'http':'http://'+ip})
	opener = urllib.request.build_opener(proxy_support)
	urllib.request.install_opener(opener)
	req = urllib.request.Request(http)
	for key in headers:
		req.add_header(key,headers[key])
	html = urllib.request.urlopen(req).read()
	return html

def getInfo(html):
	_soup = bs4.BeautifulSoup(html,from_encoding="utf-8")
	Info = _soup.findAll("div",attrs={"class":"w60 fl paddt1 paddl0 paddl15  "})
	jjrInfo = []
	for i in range(len(Info)):
		jjrname = re.findall(r'<strong>(.*?)</strong>',str(Info[i]))[0]
		jjrphone = re.findall(r'\d{11}',str(Info[i]))
		if len(jjrphone):
			jjrphone = jjrphone[0]
		else:
			jjrphone = '13800000000'
			print(jjrname+'\t'+"此经纪人没有登记电话号码!")
		jjrnp = str(jjrname)+'	'+str(jjrphone)
		jjrInfo.append(jjrnp)
	return jjrInfo

if __name__=="__main__":
	http = ['http://sx.zxfcs.cn/frontpage/mxjj?page=1&size=10000']
	jjr_file = r"D:\temp\log\dddddd.zxfcs.txt"
	headers = {
		"GET":'url',
		"Host":'Referer',
		"Referer":"http://sx.zxfcs.cn/frontpage/mxjj",
		"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36"
	}

	iplist = ['218.61.39.53:55336']
	ip = choice(iplist)

	doc = gethtml(http.pop())
	jjrInfo = getInfo(doc)
	for x in range(len(jjrInfo)):
		with open(jjr_file,'a') as f:
			f.write(jjrInfo[x]+'\r')