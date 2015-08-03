# -*- coding: utf-8 -*-
# !/usr/bin/env python
__author__ = 'Sanddy Heng'

import BeautifulSoup,urllib2
print(BeautifulSoup.__version__)
url = 'http://tj.esf.sina.com.cn/agent'
req= urllib2.Request(url)
con = urllib2.urlopen(req)
doc = con.read()
doc.close

soup = BeautifulSoup.BeautifulSoup(doc)
P_NUM = soup.findAll("div",attrs={"div":"d"})
