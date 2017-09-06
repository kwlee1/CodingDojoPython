def isPrime(x):
    for i in range(2,x):
        if x % i == 0:
            return False
    return True 

def isSquare(x):
    for i in range(2,x):
        if x % i == 0:
            if i * i == x:
                return True 
    return False 

def fooBar(end):
    result = {}
    for num in range (100,end): 
        if isPrime(num):
            result[num] = "Foo"
        elif isSquare(num):
            result[num] = "Bar"
        else:
            result[num] = "FooBar"
    print result 

fooBar(300)
# fooBar(100000)
# This would check the assignment but I commented it out so as not to overload the computer         