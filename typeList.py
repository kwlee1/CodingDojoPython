def typelist(list):
    mytype = ""
    mystring = ""
    mysum = 0
    if type(list[0]) == str: 
        mytype = "string" 
    if type(list[0]) == int:
        mytype = "integer"
    if type(list[0]) == float:
        mytype = "float"
    for num in range(0,len(list)):
        if type(list[0]) != type(list[num]):
            mytype = "mixed"
    for el in list: 
        if type(el) == str:
            mystring = mystring + " " + el 
        if type(el) == int: 
            mysum = mysum + el 
        if type(el) == float: 
            mysum = mysum + el 

    print "The list you entered is of " + mytype + " type"
    if len(mystring) > 0:
        print "String:" + mystring 
    if mysum != 0: 
        print "Sum:", mysum 

input1 = ['magical unicorns',19,'hello',98.98,'world']
input2 = [2,3,1,7,4,12]
input3 = ['magical','unicorns']

typelist(input1)
typelist(input2)
typelist(input3)
