# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 13:59:07 2022

@author: conra
"""
from parametres import *
from affichage import *
from mise_a_jour import *
ans = ["oui", 'non']
def fichier_vers_liste(nom_fichier, separateur = "$"):
    """
    Entrée : une chaîne de caractères correspondante au nom d'un fichier
    Sortie : la liste des lignes du fichier, chaque ligne étant donnée sous forme de la liste de ses mots (séparés par un espace par défaut)
    """
    L = []
    try :
       with open(nom_fichier, "r") as f:    # permet d'ouvrir un fichier et de le fermer automatiquement
            for ligne in f:                 # on parcourt l'ensemble du fichier (effectué ligne par ligne)
                if (ligne[0:5] == "para:"):
                    para = eval(ligne[5:])
                else:
                    L.append(ligne.split(separateur)) # ligne.split() est une liste dont les éléments sont les mots de ligne, séparés par le caractère separateur
    except FileNotFoundError:               # au cas où le fichier n'existe pas (et dans ce cas, la liste reste vide et revient à créer un fichier vide)
        pass
    return L, para


def creer_fichier(L, para, nom_fichier, separateur = "$"):
    """
    Entrée : une liste de listes et une chaîne de caractères correspondante au nom d'un fichier
    Sortie : écriture des élements de la liste de liste L dans le fichier, ligne par ligne et élément par élément (séparés par un espace par défaut)
    """
    F = open(nom_fichier, "w")      # on ouvre le fichier en mode "w" ("w" = mode écriture qui écrase le contenu déjà existant ; "r" = mode lecture seule ; "a" : mode append, qui rajoute le texte à la fin du fichier)
    for i in range(len(L)):
        for j in range(len(L[i])):
            print(L[i][j])
            F.write(L[i][j])        # on écrit le j-ème mot de la i-ème ligne de L
            if j < len(L[i]) - 1:   # ajout du séparateur s'il ne s'agit pas du dernier élément de la ligne
                F.write(separateur)
        F.write("\n")          # pour rajouter des sauts de ligne (s'ils ne sont pas déjà gérés dans le fichier)
    F.write("para:"+ str(para))
    F.close()    
    
import random

# INSTRUCTION 3

# cette fonction permet de generer la grille, soit de generer toute les cellules

 

def generer_grille(hauteur, largeur, p0, Pdoc):

    grille = []                 # on a une liste vide qui va nous permettre de generer la grille

 

    for i in range(0, hauteur):

        l = []                  # on a une autre liste vide qui sera une liste de dictionnaire

        for j in range(0, largeur):

            # chaque liste de liste est defini par sono etat et sa valeur

            l.append({"etat": "saine", "valeur": 0})

        grille.append(l)  # on ajoute la liste l a la liste grille

    # on calcule le nombre de cellule contaminees initiales

    contaminees_initiales = int(p0 * largeur * hauteur)

 

    # cette boucle permet de choisir aleatoirement les cellules qui seront infecter initialement

    for nb_contamine in range(0, contaminees_initiales - 1):

        haut = random.randint(0, hauteur - 1)

        larg = random.randint(0, largeur - 1)

        if grille[haut][larg] == {"etat": "saine", "valeur": 0}:

            grille[haut][larg] = {"etat": "contaminee", "valeur": 0}

        else:

            nb_contamine = nb_contamine - 1

    nb_docteur = int(Pdoc * largeur * hauteur)

    for docteur in range(0, nb_docteur - 1):

        haut = random.randint(0, hauteur - 1)

        larg = random.randint(0, largeur - 1)

        if grille[haut][larg] == {"etat": "saine", "valeur": 0}:

            grille[haut][larg] = {"etat": "docteur", "valeur": 0}

        else:

            docteur = docteur - 1

 

    return grille
 




def jouer():
    fichier = ""
    while not (fichier.lower() in ans) :
        fichier = str(input("voulez-vous utiliser un fichier existant (oui ou non) :"))
    if fichier == "oui":
        nom_fichier = str(input("entrez le nom du fichier :"))
        grille, para = fichier_vers_liste(nom_fichier)
        for  nb_liste in range (0, len(grille)):
            for nb_col in range (0, len(grille[nb_liste])):
                grille[nb_liste][nb_col]= eval(grille[nb_liste][nb_col])

    else:
        para = parametre()

        hauteur = int(para[0])

        largeur = int(para[1])

        p0 = float(para[2])

        Pdoc = float(para[7])

        grille = generer_grille(hauteur, largeur, p0, Pdoc)


    tour = int(input("combien de tours voulez vous faire :"))

    for t in range(0, tour):

        grille = config_succesive(grille, para)

        print("tour:", t + 1)

        afficher_grille(grille)

        statistique(grille)


        input()
    
    enregister = ""
    while enregister.lower() not in ans :
        enregister = str(input("voulez-vous enregistrer votre progression (oui ou non) :"))

    if enregister.lower() == "oui":
        nom_fichier = str(input("entrez le nom du fichier dans lequel vous voulez l'enregistrer :"))
        for  nb_liste in range (0, len(grille)):
            for nb_col in range (0, len(grille[nb_liste])):
               grille[nb_liste][nb_col] = str(grille[nb_liste][nb_col])
        
        creer_fichier(grille,para, nom_fichier)
    else:
        continuer = ""  
        while continuer.lower() not in ans :
            continuer = str(input("voulez-vous continuer (oui ou non) :"))

        if continuer.lower() == "oui":
            while continuer.lower() == "oui":
                tour = int(input("combien de tours voulez vous faire :"))

                for t in range(0, tour):

                    print("tour:", t + 1)

                    afficher_grille(grille)

                    statistique(grille)

                    grille = config_succesive(grille, para)

                    input()
                continuer = str(input("voulez-vous continuer (oui ou non) :"))
                
        
        
            
jouer()