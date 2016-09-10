name = raw_input("Enter the name of the file here: ")
obj=open(name, "r")
s=obj.read()
print "Data in file right now is: "
print s
print "Name of the file is ", obj.name
print "Current Mode of the file is", obj.mode
print "Status of file closing event(true/false): ", obj.closed
obj.close()
print "close() method executed therefore now the status of closing event: ", obj.closed