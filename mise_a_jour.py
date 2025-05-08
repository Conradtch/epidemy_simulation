import random

#  fonction permettant de calculer le nombre de voisines contaminées de chaque cellules
def nb_voisine_contaminee(G, n, m):
    nb_voisine_contaminee = 0
    for i in range(n - 1, n + 2):
        for j in range(m - 1, m + 2):
            if i != n or j != m:
                if 0 <= i <= len(G) - 1 and 0 <= j <= len(G[i]) - 1:
                    if G[i][j]["etat"] == "contaminee":
                        nb_voisine_contaminee = nb_voisine_contaminee + 1

    return nb_voisine_contaminee


# fonction permettant de creer la generation suivante, soit le tour suivant

def config_succesive(G, parametre):
    G_next = [[{"etat": "saine", "valeur": 0}
               for j in range(len(G[i]))] for i in range(len(G))]

    for i in range(len(G)):

        for j in range(len(G[i])):

            # cette boucle permet a une cellule saine d'etre contaminee au tour suivant

            if G[i][j]["etat"] == "saine":

                if nb_voisine_contaminee(G, i, j) >= 1:

                    # si une cellule a une voisine contaminee, alors elle a une certaine probabilite de se faire contaminer

                    for voisine_contaminee in range(0, nb_voisine_contaminee(G, i, j)):

                        # on fait un tirage qui va nous permetre de la comparer a la probabilite d'infecter une cellule voisine

                        proba = random.randint(0, 10) / 10

                        # si proba est inferieur ou egale a la probabilite d'infecter une cellule voisine

                        if proba <= parametre[3]:
                            # alors la cellule saine est contqminee par le virus

                            G_next[i][j] = {"etat": "contaminee", "valeur": 0}


            # cette boucle permet a une cellule contaminee soit de mourrir soit d'etre imunnisee au tour suivant

            elif G[i][j]["etat"] == "contaminee" and G[i][j]["valeur"] == parametre[4]:

                # on fait un tirage qui va nous permettre de la comprarer avec la probabilite de mourrir ou d'etre immunise

                proba = random.randint(0, 10) / 10

                # si cette proba est inferieur ou egale a la probabilite de mourir

                if proba <= parametre[5]:

                    # alors la cellule decede

                    G_next[i][j] = {"etat": "decedee", "valeur": 0}

                else:

                    # sinon, si la proba est superieur a la probabilite de mourir, alors la cellule ne decede pas et devient immunisee

                    G_next[i][j] = {"etat": "immunisee", "valeur": 0}

                for n in range(i - 1, i + 2):

                    for m in range(j - 1, j + 2):

                        if n != i or m != j:

                            if 0 <= n <= len(G) - 1 and 0 <= m <= len(G[n]) - 1:

                                if G[n][m]["etat"] == "docteur":
                                    G_next[i][j] = {"etat": "immunisee", "valeur": 0}

            # si la cellule est imunisee et que le nombre de jour d'imunisation est depasser, alors elle perd son imunisation et redevient saine

            elif G[i][j]["etat"] == "immunisee" and G[i][j]["valeur"] == parametre[6]:

                G_next[i][j] = {"etat": "saine", "valeur": 0}


            elif G[i][j]["etat"] == "docteur":

                if nb_voisine_contaminee(G, i, j) == 8:

                    G_next[i][j] = {"etat": "contaminee", "valeur": 0}
                else:
                    G_next[i][j] = G[i][j]


            # si aucune des conditions n'a été rempli, alors elle reste dans l'etat qu'elle est.

            else:

                G_next[i][j] = G[i][j]

            # A chaque tour, la valeur augmente de 1.

            G_next[i][j]["valeur"] = G_next[i][j]["valeur"] + 1

    return G_next

