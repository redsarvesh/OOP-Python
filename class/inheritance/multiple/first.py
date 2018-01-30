#!/usr/bin/python
class one(object):
	a=10
class two(object):
	b=10

class child(one,two):
	def fun(self):
		x=one.a+two.b
		print x

c=child()
c.fun()
