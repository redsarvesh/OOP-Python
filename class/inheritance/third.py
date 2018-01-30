#!/usr/bin/python

class parent(object):
	def __init__(self):
		self.x=10
	def fun(self):
		self.z=90
class child(parent):
	def fun2(self):
		self.y=20
		self.d=self.x+self.y
		print self.d
		parent.fun(self)
		print self.z

c=child()
c.fun2()

