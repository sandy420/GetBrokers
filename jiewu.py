# -*- coding: utf-8 -*-
# !/usr/bin/env python3.4
__author__ = 'Sanddy Heng'

from ghost import Ghost
from bs4 import BeautifulSoup
import urllib.request
import re
from os.path import exists
from os import makedirs

def Gethtml(URL):
	try:
		headers = {
		"Accept-Language":"zh-CN,zh;q=0.8",
		"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36"
	}
		req = urllib.request.Request(URL,headers=headers)
		html = urllib.request.urlopen(req).read()
		return html
	except Exception as EX:
		print(EX)

def FormatHtml(html):
	try:
		_soup = BeautifulSoup(html,"html5lib",from_encoding='utf-8')
		return _soup
	except Exception as e:
		print("FormatHtml Error:",e)

def GetNextPage(doc):
	try:
		_soup = FormatHtml(doc)
		_Info = _soup.find_all("a",attrs={"class":"tg-rownum-next index-icon"})
		NextPage = (str(_Info[0]).split('\"'))[3]
		return NextPage
	except Exception as e:
		print("GetNextPage Error:",e)


def GetName_Phone(doc):
	try:
		_soup = FormatHtml(doc)
	except Exception as es:
		print("_soup match Error:",es)
	#匹配经济人姓名及电话
	try:
		JjrName = _soup.find_all("a",attrs={"class":"black_4c"})
	except Exception as en:
		print("JJRName List matched Error",JjrName)
	try:
		JjrTel = _soup.find_all("p",attrs={"class":"jjr-detail-num icon-bg"})
	except Exception as et:
		print("JJRTel List matched Error:",et)
	try:
		for x in range(len(JjrName)):
			 name = re.findall(r'>\s*(.*?)\s*</a>',str(JjrName[x]))
			 JjrName[x] = name[0]
	except Exception as en1:
		print("Personal matched Error:",en1)
	try:
		for y in range(len(JjrTel)):
			TelNo = re.findall(r'>\s*(.*?)\s*</p>',str(JjrTel[y]))
			JjrTel[y] = TelNo[0].replace('-','')
	except Exception as et1:
		print("Personal mobile Error:",et1)
	try:
		for m in range(len(JjrName)):
			JjrNamePhone = JjrName[m]+'\t'+JjrTel[m]+'\n'
			with open(jjr_file,'a') as file:
				file.write(JjrNamePhone)
	except Exception as nt:
		print("Write Into File Error:",nt)

if __name__=="__main__":
	Uri = 'http://hz.jiwu.com/jjr/list-page1.html'
	jjr_dir = r"d:\temp\jjrlog"
	filename = str(input("保存的文件名：")+".txt")
	if exists(jjr_dir) is False:
		makedirs(jjr_dir)
	jjr_file = jjr_dir+'\\'+filename
	print("开始下载并保存：%s" % Uri)
	Html = Gethtml(Uri)
	GetName_Phone(Html)
	NextUri = GetNextPage(Html)
	while True:
		try:

			print("开始下载并保存：%s" % NextUri)
			_Html = Gethtml(NextUri)
			NextUri = GetNextPage(_Html)
			GetName_Phone(_Html)
		except Exception as e:
			print("没有下一页了！")
			exit()