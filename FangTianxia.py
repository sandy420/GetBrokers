# -*- coding: utf-8 -*-
# !/usr/bin/env /usr/local/bin/python3.4
__author__ = 'Sanddy .Heng'


from ghost import Ghost
from bs4 import BeautifulSoup
import urllib.request
import re
from os.path import exists
from os import makedirs

def gethtml(URL):
	ghost = Ghost(wait_timeout=120)
	try:
		page, resources = ghost.open(URL)
		html = BeautifulSoup(ghost.content)
	except Exception as EX:
		print(EX)
	return html

def getName_Phone(doc):
	Info = doc.find_all("a",attrs={"class":"comBtn"})
	for i in range(len(Info)):
		try:
			jjrInfo = str(re.findall(r'onclick=(.*?)return',str(Info[i])))
			jjrname=jjrInfo.split(',')[1].replace('\\\'','')
			jjrPhone=jjrInfo.split(',')[2].replace('\\\'','')
			print(jjrname+'\t'+jjrPhone)
			with open(jjr_file,'a') as f:
				f.write(jjrname+'\t'+jjrPhone+'\r')
		except Exception as err:
			print(err)
			jjrname=u' 经纪人'
			with open(jjr_file,'a') as file:
				file.write(jjrname+'\t'+jjrPhone+'\r')

def getNextPage(doc):
	_Info = str(doc.find_all("a",attrs={"id":"hlk_next"})[0]).split("\"")[1]
	return _Info

if __name__=="__main__":
	URL = str(input("输入房天下经纪人网站地址："))
	jjr_dir = r"d:\temp\jjrlog"
	filename = str(input("保存的文件名：")+".txt")
	if exists(jjr_dir) is False:
		makedirs(jjr_dir)
	jjr_file = jjr_dir+'\\'+filename
	doc = gethtml(URL)
	getName_Phone(doc)
	NextPageUrl = str(getNextPage(doc))
	while True:
		try:
			_Url = "http://esf.hf.fang.com"+NextPageUrl
			print("开始下载并保存：%s" % _Url)
			_doc = gethtml(_Url)
			getName_Phone(_doc)
			NextPageUrl = str(getNextPage(_doc))
		except:
			print("没有下一页了！")
			exit()