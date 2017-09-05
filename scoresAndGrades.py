import random 
def scores():
    print "Scores and Grades"
    for num in range(0,11):
        num = random.randint(60,100)
        if num >= 90:
            print "Score: " + str(num) + "; Your grade is A"
        elif num >= 80:
            print "Score: " + str(num) + "; Your grade is B"
        elif num >= 70: 
            print "Score: " + str(num) + "; Your grade is C"
        else: 
            print "Score: " + str(num) + "; Your grade is D"
    print "End of the program. Bye!"

scores()