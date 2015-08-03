# -*- coding: utf-8 -*-
# !/usr/bin/env python
__author__ = 'Sanddy Heng'

import urllib.request as urllib2
import bs4 as BeautifulSoup
import re
from random import choice
from time import sleep
#代理ip及端口
iplist = ['101.71.27.120:80']
ip = choice(iplist)

#抓取经纪人的网站地址列表
# S_WEB_list=['http://weihai.esf.sina.com.cn/agent/n']

#抓取经纪人并保存
JJR_FPATH = r"D:\temp\log\weihai.sina.txt"
headers = {
		"Referer":"http://weihai.esf.sina.com.cn/agent/",
		"Host":"weihai.esf.sina.com.cn",
		"Accept-Language":"zh-CN,zh;q=0.8",
		"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36"
}
#####################################################################################################
#										以下为程序执行内容，无需修改									#
#####################################################################################################
web_Url = 'http://weihai.esf.sina.com.cn/agent/n'
proxy_support = urllib2.ProxyHandler({'http':'http://'+ip})
opener = urllib2.build_opener(proxy_support)
urllib2.install_opener(opener)
req = urllib2.Request(web_Url,headers=headers)
con = urllib2.urlopen(req)
doc = con.read()
con.close
#匹配所需要查找的内容
soup = BeautifulSoup.BeautifulSoup(doc,from_encoding="utf-8")
P_NUM = soup.find("div",attrs={"class":"pages fr"})
P_NUM = P_NUM.findAll("span")
pagecount = re.findall(r'共(.*?)页', str(P_NUM))[0]

# for i in range(int(pagecount)):
for i in range(736,int(pagecount)):
	Http = web_Url + str(i)
	ip = choice(iplist)
	print("代理IP及端口:%s\t ===>\t开始下载并保存：%s"%(ip,Http))
	proxy_support = urllib2.ProxyHandler({'http':'http://'+ip})
	opener = urllib2.build_opener(proxy_support)
	urllib2.install_opener(opener)
	req = urllib2.Request(Http)
	con = urllib2.urlopen(req)
	doc = con.read()
	con.close
	_soup = BeautifulSoup.BeautifulSoup(doc,from_encoding="utf-8")
	JJR_PHONES = _soup.findAll("a",attrs={"class":"c_default f14 mr5"})
	JJR_NAMES = _soup.findAll("span",attrs={"class":"bold c_red"})
	for j in range(len(JJR_PHONES)):
		JJR_NAMES_str = str(JJR_NAMES[j]).split('>')[1].split('<')[0]
		JJR_PHONE_NOstr = str(JJR_PHONES[j]).split('>')[1].split('<')[0]
		JJR_INFO = JJR_PHONE_NOstr+'\t\t'+JJR_NAMES_str+'\r'
		with open(JJR_FPATH,'ab')as f:
			f.write(JJR_INFO)
	sleep(3)