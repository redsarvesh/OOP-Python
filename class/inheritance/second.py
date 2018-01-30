#!/usr/bin/python

class parent(object):
	def fun1(self):
		self.a=10
		return self.a
	def fun2(self):
		self.b=20
		print self.b
class child(parent):
	def fun3(self):
		self.c=30
		print self.c
		parent.fun2(self)
#		self.d=self.c+self.a
#		return self.d

c=child()
c.fun3()
print c.fun1()

