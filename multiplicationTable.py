print "x 1 2 3 4 5 6 7 8 9 10 11 12"
for mult in range(1,13,1):
    mystring = str(mult) 
    for num in range(1,13,1): 
        mystring = mystring + " " + str(num * mult)
    print mystring

