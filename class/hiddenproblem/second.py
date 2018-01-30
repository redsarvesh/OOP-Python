#!/usr/bin/python


class hidden():
	__var1=987
	var2=9898998
	
	def name(self):
		self.__var=10
		a=9
		self.z=self.__var1+a
		print self.z
		print self.__var1
		print self.__var
		print hidden.__var1
	def ano(self):
		print self.z
h=hidden()
h.name()
h.ano()


		
