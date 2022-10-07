from fileinput import close
import string
import sys
n = 0
e = ""
t = ["*", "//", "+", "/", "%", "-", "**"]
while e != "quit":
    a = input ("Entrez un premier nombre : ")
    b = input ("Entrez un second nombre : ")
    c = input ("Quelle fonction voulez vous utiliser : ")
    if ((isinstance(a, int) == "False") or ((isinstance(b,int)) == "False")) or (c in t) == "False":
        print("Merci de respecter les consignes d'utilisation")
    else: n = 1
    res = eval(a + c + b)
    print ("Le résultat de l'opération " + a,""  + c, "" + b, "est égal à : %s" %res)
    e = input("Taper \"quit\" si vous voulez quitter le programme sinon appuyer sur une autre touche : ")
else: sys.exit()
