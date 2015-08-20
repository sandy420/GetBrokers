# -*- coding: utf-8 -*-
# !/usr/bin/env python3.4
__author__ = 'Sanddy Heng'

import urllib.request
import bs4
import re
from random import choice
from time import sleep
#代理ip及端口
iplist = ['101.71.27.120:80']
ip = choice(iplist)

#抓取经纪人的网站地址列表
S_WEB_list=['http://xiangyang.ganji.com/fang/agent/o']

#抓取经纪人并保存
JJR_FPATH = r"D:\temp\jjrlog\xiangyang_ganji.txt"
headers = {
		"Referer":"http://xiangyang.ganji.com/fang/agent",
		"Host":"yc.ganji.com",
		"Accept-Language":"zh-CN,zh;q=0.8",
		"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36"
}
#####################################################################################################
#										以下为程序执行内容，无需修改									#
#####################################################################################################
web_Url = S_WEB_list.pop()

for i in range(36,51):
	Http = web_Url + str(i)
	ip = choice(iplist)
	print("代理IP及端口：%s\t ===>\t开始下载并保存：%s"%(ip,Http))
	proxy_support = urllib.request.ProxyHandler({'http':'http://'+ip})
	opener = urllib.request.build_opener(proxy_support)
	urllib.request.install_opener(opener)
	req = urllib.request.Request(Http,headers=headers)
	con = urllib.request.urlopen(req)
	doc = con.read()
	con.close
	soup = bs4.BeautifulSoup(doc,from_encoding="utf-8")
	JJR_PHONES = soup.findAll("span",attrs={"class":"broker-tel"})
	JJR_NAMES = soup.findAll("span",attrs={"class":"broker-name"})
	for j in range(len(JJR_PHONES)):
		JJR_NAMES_str = str(JJR_NAMES[j]).split(">")[2].split("<")[0]
		JJR_PHONE_NOstr = str(JJR_PHONES[j]).split(">")[3].split("<")[0]
		# JJR_INFO = JJR_NAMES_str+'\t\t'+JJR_PHONE_NOstr+'\r'
		with open(JJR_FPATH,'a')as f:
			f.write(JJR_NAMES_str+'\t'+JJR_PHONE_NOstr+'\r')
	# sleep(1)