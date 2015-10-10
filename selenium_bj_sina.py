#-*- coding: utf-8 -*-
#!/usr/bin/env /usr/local/bin/python3.4
__author__ = 'Sanddy .Heng'
__date__   = '2015-10-09'

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time


if __name__ == "__main__":

	http = "http://bj.esf.sina.com.cn/agent/m3-n"     	#网站源地址
	tkey = "hall_people_red"				#经济人电话关键字
	nkey = "hall_people_house_name_l"			#经济人姓名关键字
	filename = r"D:\temp\jjrlog\bj_sina.txt"		#存放文件地址及文件名

	#循环获取经济人信息
	for i in range(741):    				#网页页数
		url= http+str(i)
		print("开始获取%s上的经济人信息."%url)
		try:
			#调用驱动程序打开Chrome
			browser = webdriver.Chrome("chromedriver.exe")
			#设置延时30秒
			browser.implicitly_wait(30)
			#如果窗口大小设置抛异常，继续打开链接获取数据
			#也可以不设置采用默认窗体大小，提高效率
			try:
				browser.set_window_size(400,800)
				browser.get(url)
			except Exception as e:
				print("设置窗口大小错误，错误信息为:",e)
				browser.get(url)
		except NoSuchElementException as e:
			print("没有获取到：",e)

		#根据经济人姓名唯一关键字，获取经济人姓名对象
		try:
			_names = browser.find_elements_by_class_name(nkey)
		except NoSuchElementException as e:
			print("没有获取到经济人姓名：",e)

		#根据经济人电话唯一关键字，获取经济人电话对象
		try:
			_mobiles = browser.find_elements_by_class_name(tkey)
		except NoSuchElementException as e:
			print("没有获取到经济人电话：",e)

		#提取姓名到列表
		jns=[]
		for x in _names:
			jns.append(x.text)

		#提取电话到列表
		jms = []
		for y in _mobiles:
			jms.append(y.text)

		#将姓名、电话一一对应，并持久保存至文件中
		try:
			if len(jns) == len(jms):
				for num in range(len(jns)):
					nm = jns[num] + '\t' + jms[num]+'\r'
					with open(filename,'a') as f:
						f.write(nm)
						time.sleep(0.1)
			browser.quit()
		except Exception as e:
			print("姓名数和电话数不一致：",e+'\r'+jns+'\r'+jms)
