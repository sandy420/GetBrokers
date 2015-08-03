# -*- coding: utf-8 -*-
# !/usr/bin/env python
__author__ = 'Sanddy Heng'

import re
import bs4
import urllib.request as rq

URLS=[]
try:
	for i in range(3):
		URL = 'http://qhd.esf.focus.cn/agent/p'+str(i)
		URLS.append(URL)
		for p in URLS:
			req = rq.Request(p)
			con = rq.urlopen(req)
			doc = con.read()
			con.close

			soup = bs4.BeautifulSoup(doc)
			JJR_PHONES = soup.findAll("span",attrs={"class":"items_r"})
			JJR_NAMES = soup.findAll("a",attrs={"class":"link"})
			# JJR_PHONE_NO=re.compile(r'1\d{10}')
			for j in range(len(JJR_PHONES)):
				print("开始下载:%s "%p)
				JJR_NAMES_str = str(JJR_NAMES[j]).decode('utf-8').encode('utf-8')
				JJR_PHONE_NOstr = str(JJR_PHONES[j])
				JJR_INFO = JJR_NAMES_str+JJR_PHONE_NOstr+'\r'
				with open(r'D:\Python Project\PPD\log\qinhuangdao.txt','ab')as f:
					f.write(JJR_INFO)
except:
	pass
else:
	pass