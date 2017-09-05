def findChars(mylist,mychar):
    new_list = []
    for el in mylist:
        if mychar in el: 
            new_list.append(el)
    print new_list

word_list = ['hello','world','my','name','is','Anna','boo']
char = "o"

findChars(word_list,char)