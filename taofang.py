# -*- coding: utf-8 -*-
# !/usr/bin/env python3.4
__author__ = 'Sanddy Heng'

import bs4,re
import urllib.request
from  random import choice

def gethtml(http):
	proxy_support=urllib.request.ProxyHandler({'http':'http://'+ip})
	opener = urllib.request.build_opener(proxy_support)
	urllib.request.install_opener(opener)
	req = urllib.request.Request(http)
	for key in headers:
		req.add_header(key,headers[key])
	html = urllib.request.urlopen(req).read()
	return html

def getPagenum(html):
	_soup = bs4.BeautifulSoup(html,from_encoding="utf-8")
	pagenum = _soup.findAll

def getName(html):
	_soup = bs4.BeautifulSoup(html,from_encoding="utf-8")
	Info = _soup.findAll("div",attrs={"class":"title"})
	jjrInfo = []
	for i in range(len(Info)):
		jjrname = str(re.findall(r'target="_blank">(.*?)</a>',str(Info[i]))[0])
		jjrInfo.append(jjrname)
	return jjrInfo

def getPhone(html):
	_soup = bs4.BeautifulSoup(html,from_encoding="utf-8")
	Info = _soup.findAll("div",attrs={"class":"title"})
	jjrHref = []
	for i in range(len(Info)):
		jjrUrl = str(re.findall(r'href="(.*?)" target',str(Info[i]))[0])
		jjrHref.append(jjrUrl)
	phones=[]
	for j in range(len(jjrHref)):
		_doc = gethtml(jjrHref[j])
		__soup = bs4.BeautifulSoup(_doc,from_encoding="utf-8")
		tel = re.findall(r'<span>\d{11}</span>',str(__soup.find_all("div",attrs={"class":"body profile c"})))[0]
		phone = str(tel).split("<")[1].split(">")[1]
		phones.append(phone)
	return phones



if __name__=="__main__":
	http = 'http://j.taofang.com/deyang/pn'
	jjr_file = r"D:\temp\log\deyang.taofang.txt"
	headers = {
		"GET":'url',
		"Host":'Referer',
		"Referer":"http://j.taofang.com/deyang",
		"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36"
	}

	iplist = ['218.61.39.53:55336']
	for x in range(18):
		ip = choice(iplist)
		url = http+str(x)+"0"
		print("代理IP及端口：%s\t===>\t开始下载并保存：%s" %(ip,url))
		doc = gethtml(url)
		name = getName(doc)
		phone = getPhone(doc)
		for j in range(len(name)):
			with open(jjr_file,'a') as f:
				print("姓名：%s\t电话号码：%s\r"%(name[j],phone[j]))
				f.write(name[j]+'\t'+phone[j]+'\r')