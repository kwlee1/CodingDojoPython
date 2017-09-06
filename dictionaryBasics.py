me = {"name": "Keith", "age": 30, "country": "The United States", "language": "Python"}
def intro(dict):
    print "My name is " + str(dict["name"])
    print "My age is " + str(dict["age"])
    print "My country of birth is " + str(dict["country"])
    print "My favorite language is " + str(dict["language"])

intro(me)