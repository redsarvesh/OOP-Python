#!/usr/bin/python

class student:
	name='sir ashutoshh'
	
	def __init__(self,name):
		
		print name
		self.branch='cse'

	def sub(self,cn,os):
		self.cn=cn
		self.os=os
		print cn
		print os
	def marks(self):
		print self.cn
		print self.os
		print self.branch
		print student.name
st=student('sarvesh')
st.sub('sub1','sub2')
st.marks()
