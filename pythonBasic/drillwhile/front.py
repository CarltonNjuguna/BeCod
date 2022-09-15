languages = [["PHP", "Java", "C#"], ["HTML", "CSS", "Javascript"]]

for x in range(2) :
    for i in languages[x] :
        if x == 1 :
            print("{} is a backend language?".format(i))
        else :
            print("{} is a frontend language?".format(i))
            