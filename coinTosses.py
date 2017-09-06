import random
# I set my program to take an input of number of tosses and had 5000 at the end to run it
def coinToss(toss):
    print "Starting the program..."
    heads = 0
    tails = 0 
    for num in range(0,toss+1):
        if random.randint(2,3) % 2 == 0:
            heads += 1 
            print "Attempt #" + str(num) + ": Throwing a coin... It's a head! ... Got " + str(heads) + " head(s) so far and " + str(tails) + " tail(s) so far"
        else:
            tails += 1 
            print "Attempt #" + str(num) + ": Throwing a coin... It's a tail! ... Got " + str(heads) + " head(s) so far and " + str(tails) + " tail(s) so far"
    print "Ending the program, thank you!"

coinToss(5000)