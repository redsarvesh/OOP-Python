#!/usr/bin/python


class hidden():
	__var1=987
	var2=9898998
	
	def name(self):
		self.__var=10
		a=9
		print self.__var
		print hidden.__var1
h=hidden()
h.name()
print hidden.var2
print h._hidden__var1

		
