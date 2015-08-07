# -*- coding: utf-8 -*-
# !/usr/bin/env python3.4
__author__ = 'Sanddy Heng'

from bs4 import BeautifulSoup
import urllib.request
import re
from os.path import exists
from os import makedirs

def gethtml(URL):
	try:
		req=urllib.request.Request(URL)
		html=urllib.request.urlopen(req).read()
	except Exception as EX:
		print(EX)
	return html

def getName_Phone(doc):
	soup = BeautifulSoup(doc,'html.parser',from_encoding='utf8')
	jjrNames = soup.find_all("span","colour_o")[0::3]
	jjrPhones = soup.find_all("em")
	for i in range(1,len(jjrNames)):
		try:
			jjrname = re.findall(r'>(.*?)</span>',str(jjrNames[i]).replace(r'\s',''))[0]
			jjrPhone = re.findall(r'>(.*?)</em>',str(jjrPhones[i]).replace(r'\s*',''))[0]
			print(jjrname+'\t'+jjrPhone)
			with open(jjr_file,'a') as f:
				f.write(jjrname+'\t'+jjrPhone+'\r')
		except Exception as err:
			print(err)
			jjrname=u'经纪人'
			with open(jjr_file,'a') as file:
				print(jjrname+'\t'+jjrPhone)
				file.write(jjrname+'\t'+jjrPhone+'\r')



if __name__=="__main__":
	URL = "http://2sf.xffcol.com/list_jjr.php"
	jjr_dir = r"d:\temp\jjrlog"
	filename = str("ggg"+".txt")

	if exists(jjr_dir) is False:
		makedirs(jjr_dir)
	jjr_file = jjr_dir+'\\'+filename

	for x in range(1,6):
		try:
			_Url = "http://2sf.xffcol.com/list_jjr.php?p="+str(x)
			print("开始下载并保存：%s" % _Url)
			_doc = gethtml(_Url)
			getName_Phone(_doc)
		except:
			print("没有下一页了！")
			exit()