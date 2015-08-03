# -*- coding: utf-8 -*-
# !/usr/bin/env python3.4
__author__ = 'Sanddy Heng'

import re,bs4
import urllib.request
from random import choice
from time import sleep

def gethtml(http):
	proxy_support=urllib.request.ProxyHandler({'http':'http://'+ip})
	opener = urllib.request.build_opener(proxy_support)
	urllib.request.install_opener(opener)
	req = urllib.request.Request(http,headers=headers)
	html = urllib.request.urlopen(req).read()
	return html

def getName(html):
	_soup = bs4.BeautifulSoup(html,from_encoding='utf-8')
	Info = _soup.findAll("a",attrs={"class":"name"})
	jjrInfo = []
	for i in range(len(Info)):
		jjrname = str(re.findall(r'target="_blank">(.*?)</a>',str(Info[i]))[0])
		jjrInfo.append(jjrname)
	return jjrInfo

def getPhone(html):
	_soup = bs4.BeautifulSoup(html,from_encoding='utf-8')
	_Info = _soup.findAll("span",attrs={"class":"mobile_number"})
	# print(_Info)
	jjrPhones = []
	for i in range(len(_Info)):
		jjrphone = str(re.findall(r'mobile_number">\r\n(.*?)</span>',str(_Info[i]))[0]).replace(' ','').replace('\'','')
		jjrPhones.append(jjrphone)
	return jjrPhones

if __name__=="__main__":
	http = "http://hf.anjuke.com/tycoon/p"
	jjr_file = r"D:\temp\log\hf.anjuke.log"
	iplist = ['61.130.97.212:8099']
	headers = {
		"Host":"weihai.esf.sina.com.cn",
		"Accept-Language":"zh-CN,zh;q=0.8",
		"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36"
	}
	ip = choice(iplist)

	for x in range(1,51):
		ip = choice(iplist)
		weburl = http+str(x)+"-st1"
		print("代理IP及端口：%s\t===>\t开始下载并保存：%s"%(ip,weburl))
		doc = gethtml(weburl)
		name = getName(doc)
		phone = getPhone(doc)
		for y in range(len(name)):
			jjr = str(name[y])+'\t'+str(phone[y])
			with open(jjr_file,'a') as f:
				f.write(jjr+'\r')
		# sleep(1)