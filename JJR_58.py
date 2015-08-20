# -*- coding: utf-8 -*-
# !/usr/bin/env python
__author__ = 'Sanddy Heng'

import urllib.request
import bs4
import re
from random import choice
from time import sleep

#代理ip及端口
iplist = ['183.207.128.47:80']
ip = choice(iplist)

#抓取经纪人并保存
JJR_FPATH = r"D:\temp\jjrlog\cdddddd.txt"
headers = {
	"GET":'url',
	"Host":'Referer',
	"Referer":"http://cd.58.com/ershoufang",
	"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36"
}
###################################################################
#						以下为程序执行内容，无需修改				  #
###################################################################
web_Url = "http://cd.58.com/ershoufang/pn"

for i in range(2,71):
	Http = web_Url + str(i)
	ip = choice(iplist)
	headers = {
		"Accept-Language":"zh-CN,zh;q=0.8",
		"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36"
	}

	print("代理IP及端口：%s\t===>\t开始下载并保存：%s"%(ip,Http))
	proxy_support = urllib.request.ProxyHandler({'http':'http://'+ip})
	opener = urllib.request.build_opener(proxy_support)
	urllib.request.install_opener(opener)
	req = urllib.request.Request(Http,headers=headers)
	con = urllib.request.urlopen(req)
	doc = con.read()
	con.close
	_soup = bs4.BeautifulSoup(doc,fromEncoding="utf-8")
	JJR_HOME_WEBS = _soup.findAll("h1",attrs={"class":"bthead"})
	JJR_WEB_LIST = []

	for j in range(len(JJR_HOME_WEBS)):
		a = re.findall(r'href="(.*?)"',str(JJR_HOME_WEBS[j]))
		a = str(a).split('?')[0].split('\'')[1]
		JJR_WEB_LIST.append(a)

	for http in JJR_WEB_LIST:
		print("代理IP及端口：%s\t===>\t开始下载并保存：%s"%(ip,http))
		try:
			# http="http://xf.58.com/ershoufang/22679928808483x.shtml"
			_req = urllib.request.Request(http,headers=headers)
			_con = urllib.request.urlopen(_req)
			_doc = _con.read()
			_con.close
			j_soup = bs4.BeautifulSoup(_doc,fromEncoding="utf-8")
			print(j_soup)
			JJR_Name = j_soup.findAll("div",attrs={"class":"su_con"})#("a",attrs={"onclick":"clickLog('from=fc_detail_pxjjr3_ershoufang_xf');"})
			print(JJR_Name)
			JJR_Name = str(JJR_Name).split(">")[1].split("<")[0].replace('\n','')
			# if JJR_Name is None:
			# 	JJR_Name = j_soup.findAll("span",attrs={"style":"float:left;margin-right:10px;"})
			# 	print(JJR_Name)
			# 	JJR_Name = str(JJR_Name).split(">")[1].split("<")[0].replace('\n','')
			# else:
			# 	JJR_Name = str(JJR_Name).split(">")[1].split("<")[0].replace('\n','')
			JJR_phone = j_soup.findAll("span",attrs={"class":"t_phone arial c_e22"})
			JJR_phone = re.findall(r'\d{3}\s\d{4}\s\d{4}',str(JJR_phone))[0].replace(' ','')
			JJR_Info = JJR_Name+'\t'+JJR_phone
			# print(JJR_Info)
			with open(JJR_FPATH,'a') as f:
				f.write(str(JJR_Info)+'\r')
			# sleep(3)
		except Exception as EX:
			print(EX)