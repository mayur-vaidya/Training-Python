obj1=open("test.txt","w")
n=raw_input("Enter the text you want to write in the file: ")
obj1.write(n)
obj1.close()
obj2=open("test.txt","r")
s=obj2.read()
print "The updated file now is: "
print s
#t=s.trim()
#print t
obj2.close()