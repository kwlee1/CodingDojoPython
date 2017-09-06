# Part 1
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def names(dict):
    for el in dict:
        print el['first_name'] + " " + el['last_name']

names(students)

# Part 2
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def namesLength(users):
    for key, data in users.items():
        print key
        index = 1
        for value in data: 
            fullname = value['first_name'] + " " + value['last_name']
            print str(index) + " - " + fullname + " - " + str(len(fullname) - 1)
            index += 1

    
namesLength(users)