#!/usr/bin/python
class one(object):
	def __init__(self):
		pass
class two(one):
	pass

print issubclass(two,one)
print issubclass(one,two)
