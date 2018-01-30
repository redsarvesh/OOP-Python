#!/usr/bin/python

class student:
	name='sarvesh_kumar'
	print name

	def __init__(self,na):
		self.con=na
		print 'constructor'
		print na

	def fun(self,rupee):
		print self.con
		self.rupee=rupee
		#output=rupee
		#print output
		#print 'hello'
		#print rupee
		#var=800
		#print var
		#print student.name
	
	def fun2(self):
		print self.con
		print self.name
		print self.rupee
		
st=student('ashu')
st.fun('9000')
st.fun2()
