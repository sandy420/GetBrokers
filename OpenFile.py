# -*- coding: utf-8 -*-
#!/usr/bin/env python3.4
__author__ = 'Sanddy Heng'

import os
import subprocess
import multiprocessing

#决断是否是给定的文件
def endWith(s,*endstring):
	array = map(s.endswith,endstring)
	if True in array:
		return True
	else:
		return False

#获取系统中的盘符
def getDiskName():
	vols = []
	for i in range(65,91):
		vol = chr(i)+":\\"
		#判断是否是目录
		if os.path.isdir(vol):
			vols.append(vol)
	print(vols)
	return vols

#获取指定类型的文件及程序
def getFileName():
	for volDir in getDiskName():
		s = os.sep
		root = volDir + s
		for i in os.walk(root):
			for m in i[2]:
				if len(i[1]) is not None and endWith(m,'.log'):
					command = (i[0]+'\\'+m).replace('\\\\','\\')
					try:
						pool = multiprocessing.Pool(2)
						multiprocessing.cpu_count()
						pool.apply_async(os.system(command))
					except:
						print(Exception)


if __name__ == '__main__':
	try:
		getDiskName()
	except Exception as Ex:
		print(Ex)