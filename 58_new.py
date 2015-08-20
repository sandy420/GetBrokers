# -*- coding: utf-8 -*-
#!/usr/bin/env python3.4
__author__ = 'Sanddy Heng'

import urllib.request
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
from ghost import Ghost
from random import choice


def gethtml(HTTP,headers={}):
	try:
		ip = choice(iplist)
		# proxy_support=urllib.request.ProxyHandler({'http':'http://'+ip})
		# opener = urllib.request.build_opener(proxy_support)
		# urllib.request.install_opener(opener)
		req = urllib.request.Request(HTTP,headers=headers)
		HTML = urllib.request.urlopen(req,timeout=60)
		WebCon = HTML.read()
		HTML.close()
	except Exception as Err:
		print(Err)
	return WebCon

def getSubHtml(doc):
	try:
		soap = BeautifulSoup(doc,'html5lib')
		SubUrl = soap.findAll("a",attrs={"class":"t"})
		UrlList=[]
		for i in range(len(SubUrl)):
			_SubUrl = re.findall(r'href="(.*?)"',str(SubUrl[i]))
			UrlList.append(_SubUrl)
	except Exception as Ex:
		print(Ex)
	return UrlList

def GetNamePhone(subUrl):
	for x in range(len(subUrl)):
		try:
			u = str(subUrl[x][0]).split("?")
			print(u[0])
			_con = gethtml(u[0],headers)
			_soap = BeautifulSoup(_con,'html.parser')
			_name = _soap.findAll("li",attrs={"class":"jjreninfo_des_jjr"})
			_name = re.findall(r'_blank">(.*?)</a>',str(_name))
			print(_name)
		except Exception as e:
			print(e)


if __name__ == "__main__":
	web_Url = "http://cd.58.com/ershoufang/"
	JJR_FPATH = r"D:\temp\jjrlog\xiangyang.58.txt"
	headers = {
		"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36"
	}
	iplist = ['101.71.27.120:80']

	doc = gethtml(web_Url,headers)
	_urls = getSubHtml(doc)
	GetNamePhone(_urls)