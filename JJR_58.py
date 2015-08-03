# -*- coding: utf-8 -*-
# !/usr/bin/env python
__author__ = 'Sanddy Heng'

import urllib2
import BeautifulSoup
import re
from random import choice
from time import sleep

#代理ip及端口
iplist = ['218.61.39.53:55336']
ip = choice(iplist)
print ip

#抓取经纪人的网站地址列表
S_WEB_list=['http://xiaogan.58.com/ershoufang/h1/pn']

#抓取经纪人并保存
JJR_FPATH = r"D:\temp\log\xiaogan.58.txt"
headers = {
	"GET":'url',
	"Host":'Referer',
	"Referer":"http://xiaogan.58.com/ershoufang",
	"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36"
}
###################################################################
#						以下为程序执行内容，无需修改				  #
###################################################################
web_Url = S_WEB_list.pop()


# for i in range(int(pagecount)):
for i in range(10,70):
	Http = web_Url + str(i)
	ip = choice(iplist)

	print "代理IP及端口："+ip+"\t ===>\t"+"开始下载并保存："+ Http
	proxy_support = urllib2.ProxyHandler({'http':'http://'+ip})
	opener = urllib2.build_opener(proxy_support)
	urllib2.install_opener(opener)
	req = urllib2.Request(Http)
	for key in headers:
		req.add_header(key,headers[key])
	con = urllib2.urlopen(req)
	doc = con.read()
	con.close
	_soup = BeautifulSoup.BeautifulSoup(doc,fromEncoding="utf-8")
	JJR_HOME_WEBS = _soup.findAll("h1",attrs={"class":"bthead"})
	JJR_WEB_LIST = []
	for j in range(len(JJR_HOME_WEBS)):
		a = str(JJR_HOME_WEBS[j]).split("\"")[3]
		JJR_WEB_LIST.append(a)
	print JJR_WEB_LIST
	for http in JJR_WEB_LIST:
		_req = urllib2.Request(http)
		for key in headers:
			_req.add_header(key,headers[key])
		_con = urllib2.urlopen(_req)
		_doc = _con.read()
		_con.close

		j_soup = BeautifulSoup.BeautifulSoup(_doc,fromEncoding="utf-8")
		JJR_Name = j_soup.findAll("li",attrs={"class":"liv0"})
		JJR_Name = re.findall(r'>(.*?)</a>',str(JJR_Name))[0]
		print JJR_Name
		JJR_phone = j_soup.findAll("span",attrs={"id":"t_phone"})
		JJR_phone = re.findall(r'\d{3}\s\d{4}\s\d{4}',str(JJR_phone))[0].replace(' ','')
		JJR_Info = str(JJR_Name) +'\t'+str(JJR_phone)+'\r'
		print JJR_phone
		with open(JJR_FPATH,'ab') as f:
			f.write(JJR_Info)
		sleep(3)