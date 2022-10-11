from random import random, randrange
from tokenize import String
print("Bienvenue dans le jeu du nombre mystère \n")
a = int(randrange(1, 100))
e = None
while e != "quit":
    b = 0
    n = 5
    while (n > 0) and (str(b) != str(a)):
        print(f"Il vous reste {n} essais \n")
        b = (input("Devinez le nombre : "))
        if not b.isdigit():
            print("Merci de rentrer un nombre valide")
            continue
        if str(b) < str(a):
            print(f"Le nombre mystère est plus grand que {b}\n")
        elif str(b) > str(a): print(f"Le nombre mystère est plus petit que {b}\n")
        else: print("")
        n = n-1
    if str(a) == str(b): print("Félicitations vous avez trouvez le nombre mystère !!!\n")
    else: print(f"Vous n'avez plus d'essais, le nombre mystère était {a} \n") 
    e = input("Taper \"quit\" si vous voulez quitter le jeu sinon appuyer sur une autre touche pour réessayer:\n")
    a = int(randrange(1, 100))
else: print("Merci d'avoir joué au jeu du nombre mystère !")
