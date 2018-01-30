#!/usr/bin/python


class hidden():
	def __init__(self,a,b):
		self.a=a
		self.b=b

	def __str__(self):
		print 'oh this is:%r and %r'%(self.a,self.b)

h=hidden(1,2)


