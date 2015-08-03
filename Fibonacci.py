# -*- coding: utf-8 -*-
# !/usr/bin/env python
__author__ = 'Sanddy Heng'

def fibs(num):
    result=[0,1]
    for i in range(num-2):
        result.append(result[-2]+result[-1])
    return result[i+2]

def fib1(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib1(n-1)+fib1(n-2)

def fib2(n):
	a,b=0,1
	for i in range(n):
		a,b=b,a+b
		return b

if __name__ == '__main__':
	print fib1(3)
	print fib1(7)
	print fibs(33)
	print fib2(33)