# Part 1 and Part 2 together
def draw_stars(list):
    for el in list: 
        star = "*"
        myString = ""
        if type(el) == str:
            star = el[0].lower()
            for num in range(0,len(el)):
                myString += star 
            print myString
        if type(el) == int:
            for num in range(0,el):
                myString += star
            print myString

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars(x)       