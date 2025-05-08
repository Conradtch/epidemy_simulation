
# fonction permetant de definir tout les parametres
def parametre():
    ans = ["oui", "non"]

    choix0 = ""
    while choix0.lower() not in ans :
        choix0 = str(input("voulez-vous simuler une épidémie ? (oui ou non) :"))
    if choix0.lower() == "oui":
        choix1 = "0"
        while choix1.lower() != "c" and choix1.lower() != "g" and choix1.lower() != "p" :
            choix1 = str(input("quelle épidémie voulez-vous simuler ? (Covid-19 : C; grippe espagnole : G; peste noire : P) :"))
        
        if choix1.lower() == "c":
            # defini le nombre de cellule sur la hauteur
            largeur = 10
            # defini le nombre de cellule sur la largeur
            hauteur = 10
            # defini le nombre de cellule initialement contaminees
            p0 = 0.1
            # defini la probabilite, pour une cellule malade, d'infecter une cellule voisine
            R0 = 0.8
            # defini le nombre de jour apres lequel une cellule malade sera guerri
            Dm = 7
            # defini la probabilite que une cellule malade meurt
            Pm = 0.2
            # defini le nombre de jour de l'imunisation d'une cellule
            Di = 7
            Pdoc = 0.05
            parametre = [hauteur, largeur, p0, R0, Dm, Pm, Di, Pdoc]
            return parametre
        
        elif choix1.lower() == "g":
            # defini le nombre de cellule sur la hauteur
            largeur = 10
            # defini le nombre de cellule sur la largeur
            hauteur = 10
            # defini le nombre de cellule initialement contaminees
            p0 = 0.1
            # defini la probabilite, pour une cellule malade, d'infecter une cellule voisine
            R0 = 0.5
            # defini le nombre de jour apres lequel une cellule malade sera guerri
            Dm = 6
            # defini la probabilite que une cellule malade meurt
            Pm = 0.9
            # defini le nombre de jour de l'imunisation d'une cellule
            Di = 6
            Pdoc = 0.05
            parametre = [hauteur, largeur, p0, R0, Dm, Pm, Di, Pdoc]
            return parametre
  
        elif choix1.lower() == "p":
            # defini le nombre de cellule sur la hauteur
            largeur = 10
            # defini le nombre de cellule sur la largeur
            hauteur = 10
            # defini le nombre de cellule initialement contaminees
            p0 = 0.2
            # defini la probabilite, pour une cellule malade, d'infecter une cellule voisine
            R0 = 0.3
            # defini le nombre de jour apres lequel une cellule malade sera guerri
            Dm = 3
            # defini la probabilite que une cellule malade meurt
            Pm = 0.8
            # defini le nombre de jour de l'imunisation d'une cellule
            Di = 3
            Pdoc = 0.05
            parametre = [hauteur, largeur, p0, R0, Dm, Pm, Di, Pdoc]
            return parametre
         
    else:
        choix2 = ""
        while choix2.lower() not in ans :
            choix2 = str(input("voulez-vous parametrer vous-mêmes (oui ou non) :"))
        if choix2.lower() == "oui":
            # defini le nombre de cellule sur la hauteur
            hauteur = int(input("entrez la hauteur :"))
            # defini le nombre de cellule sur la largeur
            largeur = int(input("entrez la largeur :"))
            # defini le nombre de cellule initialement contaminees

            p0 = int(input(
                "entrez la densité de population initialement contaminée (entier entre 0 et 10) :"))
            # si l'utilisateur n'est pas satisfait, alors on recommence le calcule de p0
            while p0 < 0 or p0 > 10:
                p0 = int(input(
                    "entrez la densité de population initialement contaminée (entier entre 0 et 10) :"))
            p0 = p0 / 10

            # defini la probabilite d'infecter une cellule voisine
            R0 = int(input(
                "entrez la probabilité d'infecter une cellule voisine (entier entre 0 et 10) :"))
            # si l'utilisateur n'est pas satisfait, alors on recommence le calcule de p0
            while R0 < 0 or R0 > 10:
                R0 = int(input(
                    "entrez la probabilité d'infecter une cellule voisine (entier entre 0 et 10) :"))
            R0 = R0 / 10

            # on demande a l'utilisateur d'entrer le nombre de jour apres lequel une cellule malade sera guerri
            Dm = int(input("entrez le nombre de jours avant guérison: "))

            Pm = int(input("entrez la probabilité de mortalité (entier entre 0 et 10) :"))
            while Pm < 0 or Pm > 10:
                # defini la probabilite d'infecter une cellule voisine
                Pm = int(
                    input("entrez la probabilité de mortalité (entier entre 0 et 10) :"))
            Pm = Pm / 10

            # on demande a l'utilisateur d'entrer le nombre de jour de l'imunisation d'une cellule
            Di = int(input("entrez le nombre de jours immunisé :"))

            # on demande a l'utilisateur d'entrer le nombre de docteur, entre 0 et 3 docteurs
            Pdoc = int(input("entrez la densite de population docteur (entier entre 0 et 3) :"))
            while Pdoc < 0 or Pdoc > 3:
                Pdoc = int(
                    input("entrez la densite de population docteur (entier entre 0 et 3) :"))
            Pdoc = Pdoc / 10
            parametre = [hauteur, largeur, p0, R0, Dm, Pm, Di, Pdoc]
            return parametre
    
            
        # si l'utilisateur ne veut pas configurer les parametres, alors on les defini
        else:
            # defini le nombre de cellule sur la hauteur
            largeur = 10
            # defini le nombre de cellule sur la largeur
            hauteur = 10
            # defini le nombre de cellule initialement contaminees
            p0 = 0.1
            # defini la probabilite, pour une cellule malade, d'infecter une cellule voisine
            R0 = 0.5
            # defini le nombre de jour apres lequel une cellule malade sera guerri
            Dm = 3
            # defini la probabilite que une cellule malade meurt
            Pm = 0.6
            # defini le nombre de jour de l'imunisation d'une cellule
            Di = 3
            # defini le nombre de docteur dans la simsulation
            Pdoc = 0.05
            parametre = [hauteur, largeur, p0, R0, Dm, Pm, Di, Pdoc]
            return parametre


