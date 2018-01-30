#!/usr/bin/python
	

class Person(object):
    def __init__(self):
        self.name = "{} {}".format("First","Last")
    def f(self):
	self.x=10

class Employee(Person):
    def introduce(self):
        print("Hi! My name is {}".format(self.name))
	print self.x
e = Employee()
e.introduce()
