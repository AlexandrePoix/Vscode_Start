from fileinput import close
import string
import sys
n = z = y = 0
e = ""
t = ["*", "//", "+", "/", "%", "-", "**"]
while e != "quit":
    while n == 0:
        print()
        a = input ("Entrez un premier nombre : ")
        if a.isnumeric() == False:
            print ("Merci de remplir avec un nombre")
        else: n = 1
    while z == 0:
        print()
        b = input ("Entrez un second nombre : ")
        if b.isnumeric() == False:
            print("Merci de remplir avec un nombre") 
        else:
            z = 1
    while y == 0:
        print()
        y = 0
        c = input ("Quelle fonction voulez vous utiliser : ")
        if (c in t) == False:
            print("Merci de remplir avec un opérateur de calcul")
        else: y = 1
    res = eval(a + c + b)
    print()
    print ("Le résultat de l'opération " + a,""  + c, "" + b, "est égal à : %s" %res)
    n = 0
    y = 0
    z = 0
    print()
    e = input("Taper \"quit\" si vous voulez quitter le programme sinon appuyer sur une autre touche : ")
    print()
else: sys.exit()
