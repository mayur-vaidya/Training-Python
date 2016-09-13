class StrMethod(object):
	a="Welcome to Python"
	b="Welcome"
	c="to"
	d="Python"
	e="welcome"

	print a.istitle()
	print a.endswith(b)		#False
	print a.count(b) 		#6
	print a.endswith(d)		#True
	print a.find(c, 0, len(a))	#8
	#print a.index(e)		#Should throw an exception
	print a.index(c)		#0
	print a.isalnum()	    #False
	print a.isalpha()		#True
	print a.isdigit()		#False
	print a.islower()		#False
	print a.isupper()		#False
	print a.isspace()		#True
	print len(a)			#17
	print a.lower()			#welcome to python
	print a.upper()			#WELCOME TO PYTHON
	print a.startswith(b)	#True
	print a.startswith(c,8,16)#True
	print a.swapcase()		#All the cases should be reversed 
	print a.lstrip()		#Welcome to Python
	print a.rstrip()		#Welcome to Python
	print e.capitalize()	#Welcome
	