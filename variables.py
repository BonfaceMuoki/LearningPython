x=10
print(x)

def addTenToY():
    global x
    x=20
    print(int(x)+10)
def dataTypes():
    #declaring integer and printing it in a single line
    x=10
    #printing by concatnate method  1.Note that the comma separated print converts the objects into strings
    print("The value of",type(x), "is",str(x))
     #printing by concatnate method  1.Note that you have to  convert to a string the objects.
    print("The value of "+str(type(x))+ " is "+str(x))
dataTypes()

