import random

number = random.randint(1,100)
while True :
    ui = int(input("veuillez choisir un nombre : "))
    if ui < number :
        print("It's more")
    elif number < ui :
        print("it's less")
    elif number == ui :
        print("Well done, you won! {}".format(ui))
        break