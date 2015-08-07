# -*- coding: utf-8 -*-
# !/usr/bin/env python3.4
__author__ = 'Sanddy Heng'

import urllib.request
from ghost import Ghost
import re
from bs4 import BeautifulSoup
from os.path import exists
from os import makedirs

def gethtml(URL):
	ghost = Ghost(wait_timeout=120)
	try:
		page, resources = ghost.open(URL)
		html = BeautifulSoup(ghost.content)#,from_encoding='GB18030')
	except Exception as EX:
		print(EX)
	print(html)
	return html

def getName(html):
	_soup = BeautifulSoup(html,from_encoding='GB18030')
	Info = _soup.findAll("label",attrs={"style":"white-space:nowrap;"})
	print(Info)
	jjrInfo = []
	for i in range(len(Info)):
		jjrname = str(re.findall(r'target="_blank">(.*?)</a>',str(Info[i]))[0])
		jjrInfo.append(jjrname)
	return jjrInfo

def getName_Phone(doc):
	Info = doc.find_all("label",attrs={"style":"white-space:nowrap;"})
	for i in range(len(Info)):
		try:
			jjrInfo = str(re.findall(r'nowrap;">"(.*?)"<img',str(Info[i])))
			print(jjrInfo)
		except Exception as err:
			print(err)

def getPhone(html):
	_soup = BeautifulSoup(html,from_encoding='utf-8')
	_Info = _soup.findAll("span",attrs={"class":"mobile_number"})
	jjrPhones = []
	for i in range(len(_Info)):
		jjrphone = str(re.findall(r'mobile_number">\r\n(.*?)</span>',str(_Info[i]))[0]).replace(' ','').replace('\'','')
		jjrPhones.append(jjrphone)
	return jjrPhones

if __name__=="__main__":
	http = "http://second.xf.fccs.com/broker/"
	jjr_file = r"d:\temp\jjrlog\xiangyang.fccs.txt"

	gethtml(http)
	# print(doc)
	# name = getName(doc)
		# phone = getPhone(doc)
		# for y in range(len(name)):
		# 	jjr = str(name[y])+'\t'+str(phone[y])
		# 	with open(jjr_file,'a') as f:
		# 		f.write(jjr+'\r')