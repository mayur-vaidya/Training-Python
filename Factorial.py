# Program for factorial

class Factorial:

	print "********** Program for factorial **********"
	a=int(raw_input("Enter the number: "))
	c=1
	for b in range (1, (a+1)):
					c=c*b
	print "The factorial of the given value is: ", c