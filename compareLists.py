def compare(list1,list2):
    if len(list1) == len(list2):
        for ind in range(0,len(list1)):
            if list1[ind] != list2[ind]:
                print "The lists are not the same."
                break 
        print "The lists are identical."
    else: 
        print "The lists are not the same. "

list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']

compare(list_one,list_two)