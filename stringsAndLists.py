words = "It's thanksgiving day. It's my birthday,too!"
# Find and Replace
words.find("day")
# returns index for "d" in first instance of "day"
words2 = words.replace("day","month")
# Min and Max
x = [2,54,-2,7,12,98]
minmaxx = [min(x),max(x)]
print minmaxx 
# new list with min and max values of initial list
# First and Last
x2 = ["hello",2,54,-2,7,12,98,"world"]
firstlast = [x2[0],x2[1]]
print firstlast
# New List
x3 = [19,2,54,-2,7,12,98,32,10,-3,6]
x3.sort()
print x3
x4 = [0]
x4[0] = x3[0:len(x3)/2]
x4 = x4 + x3[len(x3)/2:]
print x4