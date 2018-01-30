#!/usr/bin/python

class student:
	name='sir ashutoshh'
	
	def __init__(self,name):
		self.name=name
		
		print name
		self.branch='cse'

	def sub(self,cn,os):
		self.cn=cn
		self.os=os
		print cn
		print os
	def marks(self,name):
		print self.cn
		print self.os
		print self.branch
		print self.name
		print student.name
		print name
st=student('sarvesh')
st.sub('sub1','sub2')
st.marks('helloworld')

st1=student('rajesh')
