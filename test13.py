#!/usr/bin/python

class pycho():
	var=8
	def __init__(self):
		self.var=98
		print self.var
		print pycho.var
	def fun(self):
		print self.var
		print pycho.var

p=pycho()
p.fun()
