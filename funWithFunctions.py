# Odd/Even Function
def odd_even():
    for num in range(1,2001):
        if num % 2 == 0:
            print "Number is " + str(num) + ". This is an even number."
        else:
            print "Number is " + str(num) + ". This is an odd number."

# odd_even()

# Multiply Function
def multiply(list1,num):
    for ind in range(0,len(list1)):
        list1[ind] *= num
    return list1

# a = [2,4,10,16]
# b = multiply(a,5)
# print b

# Hacker Challenge
def layered_multiples(arr): 
    for ind in range(0,len(arr)):
        newarr = []
        for count in range(0,arr[ind]):
            newarr.append(1)
        arr[ind] = newarr 
    return arr 

# x = layered_multiples(multiply([2,4,5],3))
# print x