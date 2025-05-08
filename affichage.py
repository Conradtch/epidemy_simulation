import random
# cette fonction nous permet d'afficher la grille avec les carres de couleur representant l'etat des cellules

def afficher_grille(T):
    for i in range(len(T)):
        for j in range(len(T[i])):
            if T[i][j]["etat"] == "saine":  # si la cellule est saine, alors le carre sera vert
                print("\033[32m◯", end=" ")

            elif T[i][j]["etat"] == "contaminee":
                # si la cellule est contaminee, alors le carre sera rouge
                print("\033[31m◯", end=" ")

            elif T[i][j]["etat"] == "decedee":
                # si la cellule est decede, alors le carre sera noir
                print("\033[30m◯", end=" ")


            elif T[i][j]["etat"] == "immunisee":
                # si la cellule est imunise, alors le carre sera bleu
                print("\033[36m◯", end=" ")

            elif T[i][j]["etat"] == "docteur":
                print("\033[35m◯", end=" ")

        print("\033[0m")


# cette fonction cacule et affiche le nombre de cellules saines, contaminees, immunisees, mortes

def statistique(G):
    nombre_saines = 0
    nombre_contaminees = 0
    nombre_immunisees = 0
    nombre_mortes = 0
    nombre_docteur = 0

    for i in range(len(G)):

        for j in range(len(G[i])):

            # si une cellule est saine, alors la fonction ajoute 1 au compteur nombre_saines

            if G[i][j]["etat"] == "saine":

                nombre_saines = nombre_saines + 1


            # si une cellule est contaminees, alors la fonction ajoute 1 au compteur nombre_contaminees

            elif G[i][j]["etat"] == "contaminee":

                nombre_contaminees = nombre_contaminees + 1


            # si une cellule est immunisees, alors la fonction ajoute 1 au compteur nombre_immunisees

            elif G[i][j]["etat"] == "immunisee":

                nombre_immunisees = nombre_immunisees + 1

            elif G[i][j]["etat"] == "docteur":

                nombre_docteur = nombre_docteur + 1

            # si une cellule est morte, alors la fonction ajoute 1 au compteur nombre_mortes

            else:

                nombre_mortes = nombre_mortes + 1

                # on affiche la valeur de chaque compteur

    print("Le nombre de cellules saines est :",

          nombre_saines, ": \033[42m  \033[0m")

    print("Le nombre de cellules contaminées est :",

          nombre_contaminees, ": \033[41m  \033[0m")

    print("Le nombre de cellules immunisées est :",

          nombre_immunisees, ": \033[46m  \033[0m")

    print("Le nombre de cellules mortes est :",

          nombre_mortes, ": \033[40m  \033[0m")

    print("Le nombre de cellules docteurs est :",

          nombre_docteur, ": \033[45m  \033[0m")
