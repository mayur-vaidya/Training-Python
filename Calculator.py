import Module2
print "You can perform the basic operation of Calculation here..."
x = float(raw_input("Enter the first value: "))
y = float(raw_input("Enter the second value: "))
print """Enter the choice of operation you want to perform
			1.Addition
			2.Subtraction
			3.Multiplication
			4.Division
	 	Enter Your Choice (1,2,3 or 4)"""
n=int(raw_input())
if n==1:
	Module2.add(x,y)

if n==2:
	Module2.sub(x,y)

if n==3:
	Module2.mul(x,y)

if n==4:
	Module2.div(x,y)
	
if n>4:
	print "Please Enter the genuine details/option."

