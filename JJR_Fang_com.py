# -*- coding: utf-8 -*-
# !/usr/bin/env python
__author__ = 'Sanddy Heng'

import urllib.request as urllib2
import bs4 as BeautifulSoup
import re
from random import choice
from time import sleep

def getHtml(url,IP='221.10.102.203:82'):
	proxy_support = urllib2.ProxyHandler({'http':'http://'+IP})
	opener = urllib2.build_opener(proxy_support)
	urllib2.install_opener(opener)
	req = urllib2.Request(url)
	con = urllib2.urlopen(req)
	doc = con.read()
	return doc

#获取子页面
def  getsublst(doc):
	doc = getHtml(url,IP='221.10.102.203:82')
	soup = BeautifulSoup.BeautifulSoup(doc,fromEncoding="utf-8")
	lst = soup.findAll("dd",attrs={"class":"info rel floatr"})
	lst = re.findall(r'href="(.*?)"',lst).text
	print(lst)
	return lst

#获取下一页地址
def getNext(doc):
	doc = getHtml(url)
	soup = BeautifulSoup.BeautifulSoup(doc,fromEncoding="utf-8")
	Next = soup.findAll("a",attrs={"id":"PageControl1_hlk_next"})
	Next = re.findall(r'href="/(.*?)"',Next)
	return Next

#获取经纪人信息
def getInf(url):
	doc = getHtml(url)
	soup = BeautifulSoup.BeautifulSoup(doc,fromEncoding="utf-8")
	info = soup.findAll("div",attrs={"class":"info-phone"})
	name = re.findall(r'>"(.*?)"<').text
	phone = re.findall(r'\d{11}',info).txet
	return name,phone

if __name__ == '__main__':
	#代理ip及端口
	iplist = ['221.10.102.203:82']

	#抓取经纪人的网站地址列表
	url='http://esf.xiaogan.fang.com/esfhouse/'

	#抓取经纪人并保存
	JJR_FPATH = r"D:\temp\log\ffff.txt"
	headers = {
		"GET":'url',
		"Host":'Referer',
		"Referer":"http://esf.xiaogan.fang.com",
		"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36"
	}

	try:
		while True:
			IP = choice(iplist)
			html_doc = getHtml(url,IP)
			sub_lst_url = getsublst(html_doc)
			while True:
				try:
					url = S_URL.replace("/esfhouse",'')+sub_lst_url.pop()
					print("代理IP及端口：%s\t===>\t开始下载并保存：%s"%(IP,url))
					JJR_NAME = getInf(url)[0]
					JJR_PHONE = getInf(url)[1]
					JJR = JJR_NAME+'\t'+JJR_PHONE
					with open(JJR_FPATH,'ab') as f:
						f.write(JJR)
				except:
					print("此页获取完毕....")
			Nextpage = S_URL+getNext(html_inf)
			sleep(1)
	except:
		print("没有下一页了，获取完毕....")