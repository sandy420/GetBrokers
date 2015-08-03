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
	Info = _soup.findAll("a",attrs={"class":"c_default f14 mr5"})
	jjrInfo = []
	for i in range(len(Info)):
		jjrname = str(re.findall(r'target="_blank">(.*?)</a>',str(Info[i]))[0])
		jjrInfo.append(jjrname)
	return jjrInfo

def getPhone(html):
	_soup = bs4.BeautifulSoup(html,from_encoding='utf-8')
	_Info = _soup.findAll("span",attrs={"class":"bold c_red"})
	jjrPhones = []
	for i in range(len(_Info)):
		jjrphone = str(re.findall(r'class="bold c_red">(.*?)</span>',str(_Info[i]))[0])
		jjrPhones.append(jjrphone)
	return jjrPhones

def getPagenum(html):
	_soup = bs4.BeautifulSoup(html,from_encoding='utf-8')
	_InfoNum = re.findall(r'共(.*?)页',str(_soup))[0]
	return _InfoNum

if __name__=="__main__":
	http = "http://weihai.esf.sina.com.cn/agent/n"
	jjr_file = r"D:\temp\log\weihai.sina.log"
	iplist = ['182.254.153.54:80','61.130.97.212:8099']
	headers = {
		"Host":"weihai.esf.sina.com.cn",
		"Accept-Language":"zh-CN,zh;q=0.8",
		"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36"
	}
	ip = choice(iplist)
	doc = gethtml(http)
	pagenum = getPagenum(doc)
	print(pagenum)

	for x in range(int(pagenum)):
		ip = choice(iplist)
		weburl = http+str(x)
		print("代理IP及端口：%s\t===>\t开始下载并保存：%s"%(ip,weburl))
		doc = gethtml(weburl)
		name = getName(doc)
		phone = getPhone(doc)
		for y in range(len(name)):
			jjr = str(name[y])+'\t'+str(phone[y])
			with open(jjr_file,'a') as f:
				f.write(jjr+'\r')
		# sleep(1)