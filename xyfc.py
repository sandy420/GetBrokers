# -*- coding: utf-8 -*-
# !/usr/bin/env python3.4
__author__ = 'Sanddy Heng'

import re,bs4
import urllib.request
from random import choice
from os.path import exists
from os import makedirs

def gethtml(http):
	proxy_support=urllib.request.ProxyHandler({'http':'http://'+ip})
	opener = urllib.request.build_opener(proxy_support)
	urllib.request.install_opener(opener)
	req = urllib.request.Request(http,headers=headers)
	html = urllib.request.urlopen(req).read()
	return html

def getName(html):
	_soup = bs4.BeautifulSoup(html,from_encoding='utf-8')
	Info = _soup.findAll("a",attrs={"class":"img"})
	jjrInfo = []
	for i in range(len(Info)):
		jjrname = str(re.findall(r'<strong>(.*?)</strong>',str(Info[i]))[0])
		jjrInfo.append(jjrname)
	return jjrInfo

def getPhone(html):
	_soup = bs4.BeautifulSoup(html,from_encoding='utf-8')
	_Info = _soup.findAll("div",attrs={"class":"Contact"})
	jjrPhones = []
	for i in range(len(_Info)):
		jjrphone = str(re.findall(r'</i>(.*?)</span>',str(_Info[i]))[0]).replace(' ','')
		if jjrphone == u'暂无':
			jjrphone = None
		jjrPhones.append(jjrphone)
	return jjrPhones

def getNextPage(doc):
	_Info = bs4.BeautifulSoup(doc,from_encoding="utf-8")#(doc.find_all("a",attrs={"id":"hlk_next"})[0]).split("\"")[1]
	_NextPageUrl = _Info.findAll("div",attrs={"class":"p_bar"})
	_url=re.findall(r'href="(.*?)"',str(_NextPageUrl))
	return _url[-2]

if __name__=="__main__":
	URL = "http://www.xyfc.com/member/mcnid_14/index1.html"
	iplist = ['61.130.97.212:8099']
	ip = choice(iplist)
	headers = {
		"Host":"weihai.esf.sina.com.cn",
		"Accept-Language":"zh-CN,zh;q=0.8",
		"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36"
	}
	jjr_dir = r"d:\temp\jjrlog"
	filename = str(input("保存的文件名：")+".txt")
	if exists(jjr_dir) is False:
		makedirs(jjr_dir)
	jjr_file = jjr_dir+'\\'+filename
	doc = gethtml(URL)
	names=getName(doc)
	phones=getPhone(doc)
	for x in range(len(names)):
		jjr_nf = str(names[x])+'\t'+str(phones[x])
		if phones[x] is not None:
			with open(jjr_file,'a') as f:
				f.write(jjr_nf+'\r')
	NextPageUrl = str(getNextPage(doc))
	while True:
		try:
			print("开始下载并保存：%s" % NextPageUrl)
			_doc = gethtml(NextPageUrl)
			_names = getName(_doc)
			_phones = getPhone(_doc)
			for m in range(len(names)):
				_jjr_nf = str(_names[m])+'\t'+str(_phones[m])
				if _phones[m] is not None:
					with open(jjr_file,'a') as f:
						f.write(_jjr_nf+'\r')
			NextPageUrl = str(getNextPage(_doc))
		except:
			print("没有下一页了！")
			exit()