#program for checking whether given String is Palindrome or not

import time;

class StrPalin:
	n = raw_input("Enter the string to test: ");
	print "Now Testing..."
	print "Please Wait"
	s=len(n)
	a = n.lower()
	str1=''
	#print a
	b=-(s)
	for c in range(-1,b-1,-1):    	                    
    				str1 = str1 + a[c] 
	#print str1
	for aa in range(1,6):
					print "."
					time.sleep(1)
					
	if (str1 == a):
		print "Entered String is Palindrome."
	else:
		print "Entered String is not a Palindrome"
	