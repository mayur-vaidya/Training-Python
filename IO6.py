n = raw_input("Enter the name of the text file without extention: ")
name = n+".txt"
a = raw_input("If you want to overwrite press 'Y' and if you want to update press 'N' :  ")
if a is 'Y':
	mode="W+"
if a is 'N':
 	mode="a+"
obj=open(name, mode)
print "Enter the data now: "
s = raw_input()
obj.write(s)
obj.close()
obj1=open(name)
print "Updated file looks like :"
d=obj1.read()
print d
obj1.close()
print "Continue if further code available..."