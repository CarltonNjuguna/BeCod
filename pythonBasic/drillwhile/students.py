students = [
    "Merouane",
    "Baptiste",
    "Caroline",
    "Joe",
    "Sophie",
    "Nathan",
    "Raphaël",
    "Axel",
    "Mathieu",
    "Adrien",
]
def sortalpha(students) :
    print(sorted(students))

def onlym(students) :
    for i in students :
        if i[0] == 'M' :
            print(i)
