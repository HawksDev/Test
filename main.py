import time

print("""Acces Au Systeme de la DGRI
||||||||||||     ||||||||||||||   ||||||||||||||   ||||||||||||||
||          ||   ||               ||          ||         ||
||          ||   ||               ||          ||         ||
||          ||   ||               ||          ||         ||
||          ||   ||    ||||||||   ||||||||||||||         ||
||          ||   ||          ||   ||    ||               ||
||          ||   ||          ||   ||      ||             ||
||          ||   ||          ||   ||        ||           ||
||||||||||||     ||||||||||||||   ||          ||   ||||||||||||||""")

IIIIIIDIIIIII = str(input("ID : "))
MMMMMMMMDMMMMMMMP = str(input("MDP : "))



if IIIIIIDIIIIII == "admin" and MMMMMMMMDMMMMMMMP == "test":
    print("Acces Autoriser")
    print("Dossier Ecrit : \n 1. AC\n 2. \n 3.")
    docchoisi = input("Choisie le dossier que tu veux afficher : ")
    if docchoisi == "1":
        verifdoc1 = input("MDP du dossier : ")
        if verifdoc1 == "test":
            print("Acces Autoriser")
            print("Chargement des info ...")
            time.sleep(5)
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print("Info trouver sur antoine chabanne !")
            print("Default : Education \n Autre realiter \n Sans Gene \n Jaloux")
            print(" ")
            print(" ")
            print("Recherche de video de preuve ...")
            time.sleep(5)
            print("video trouver sur le telephone et l'ipad de Martin ")
            print(" ")
            print(" ")
            print("Chargement d'autre Info ...")
            time.sleep(10)
            print("MDP PC : 122008")
            time.sleep(300)
            print("Temps Ecoulé")
        else:
            print("Acces Refuser")
    else:
        print("Acces Refuser")
else:
    print("Acces Refuser")
    



