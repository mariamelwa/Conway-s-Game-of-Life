# Auteurs: Mariam Elwa et Thanh Liem Huynh
# Date: 9 juillet 2023



# La fonction creerGrille prend un paramètre, tailleGrille, qui est un
# enregistrement possédant 3 champs : nx le nombre de cases sur l'axe x, ny le
# nombre de cases sur l'axe y et largeur qui est la largeur d'une case.
# La fonction crée un modèle de la grille de jeu et retourne la variable modèle
# de taille spécifiée, qui est dans ce cas un tableau 1D.

def creerGrille(tailleGrille):

    nx = tailleGrille.nx  # nombre des cases sur l’axe x
    ny = tailleGrille.ny  # nombre des cases sur l’axe y

    tab = [0]*nx*ny       # création du tableau de grille initialisé avec des 0
    return tab            # retourner tableau de grille




# La procédure init(grille) prend un paramètre, grille, une variable modèle du
# jeu de grille representée sous forme d'un tableau (1D). Elle génére
# aléatoirement les indexes des cellules vivantes sur la grille.

def init (grille):

    n = len(grille) # obtenir la taille de la grille

    # Génération du pourcentage des cellules vivantes aléatoirement entre 10%
    # et 50%
    pourcent = 0.4*random()+0.1

    # Calculer le nombre de cellules vivantes en fonction du pourcentage
    vivant = round(n*pourcent)

    # Initialiser les cellules vivantes dans la grille
    for i in range(vivant):

            #placer la valeur 1 pour représenter une cellule vivante
            grille[i] = 1

    # Brasser les cellules vivantes dans la grille
    for i in range(n-1,1,-1):

        #sélection aléatoire d'un index de cellule
        j = math.floor(random()*(i+1))

        #stockage temporaire de la valeur de la cellule actuelle
        tmp = grille[i]

        #échange valeur de la cellule actuelle avec la cellule selectionnée
        #aléatoirement
        grille[i] = grille[j]

        #placer la valeur temporaire dans la cellule selectionnée
        grille[j] = tmp




#La procédure carreRouge prend un paramètre, largeur qui est un entier positif.
#Elle sert à dessiner un carré rouge.

def carreRouge(largeur):
    pencolor(1,0,0)    # rouge
    pensize(largeur)   # largeur du tracé
    fd(largeur)        # carré rouge


#La procédure positionner prend 2 paramètres qui sont des entiers, x qui est la
#position sur l'axe des abscisses et y la position sur l'axe des ordonnées.
#La fonction déplace la tortue aux coordonnées spécifié.

#Source: Chapitre 6 p.15

def positionner(x,y):
    pu()      # lever le stylo
    fd(x)     # avancer à la position x sur l'axe des abscisses
    lt(90)    # tourner à gauche de 90 degrés
    fd(y)     # avancer à la position y sur l'axe des ordonnées
    rt(90)    # tourner à droite de 90 degrés
    pd()      # baisser le stylo


#La procédure lignes prend 3 paramètres qui sont des entiers: nbLignes qui est
#le nombre de lignes à tracer, pas qui est l'espacement vertical entre les
#lignes et largeur qui est la largeur des lignes à tracer.
#La fonction aide à tracer des lignes en utilisant la tortue.

#Source: chapitre 6 p.15

def lignes(nbLignes, pas, largeur) :
    for _ in range(nbLignes) :

        fd (largeur)  # avancer pour tracer une ligne de la largeur specifiée

        #positionner tortue pour tracer la prochaine ligne
        positionner(-largeur, pas)

    positionner(0, -pas*nbLignes) #positionner tortue à la fin des lignes tracé


# La procédure dessinerGrille prend 2 paramètres : tailleGrille et grille,
# tailleGrille est la taille de la grille qui est un enregistrement avec les
# champs nx,ny,largeur, et grille est le modele de grille de jeu qui est un
# tableau représentat l'état des cellules.
# La fonction affiche l'état du jeu selon le contenu de la variable modèle.

def dessinerGrille(tailleGrille, grille):

    nx = tailleGrille.nx  # nombre de cases sur l’axe x de la grille
    ny = tailleGrille.ny  # nombre de cases sur l’axe y de la grille
    largeur = tailleGrille.largeur #la largeur d'une case de grille, en pixels

    clear() #effacer dessin et centrer la tortue
    ht()    #cacher tortue

    # Dessiner les cases vivantes rouges

    #Positionner tortue en bas à gauche avec correction pour tracer carrés
    positionner(-largeur//2*nx, -largeur//2*ny + largeur//2)

    #parcourir chaque ligne (x) et chaque colonne (y) de la grille
    for x in range(nx):
        for y in range(ny):

            #position de la tortue au coin supérieur gauche de la case
            positionner(x*largeur,y*largeur)

            #convertir les coordonnées 2D (x,y) en un index 1D dans la grille
            index = index2dTo1d([x,y],ny)

           #si la case dans la grille est vivante (valeur égale à 1), alors
           #dessiner un carré rouge
            if grille[index] == 1:
                carreRouge(largeur)

            else:
                pu()         # lever stylo
                fd(largeur)  # avancer d'une case
                pd()         # baisser stylo

            #Revenir à la position initiale pour dessiner la case suivante
            positionner(-(x+1)*largeur, -y*largeur)

    #Source: chapitre 6 p.15
    #Dessiner la grille noire

    pensize(1)        # largeur du tracé
    pencolor(0,0,0)   # noir

    positionner(0, -largeur//2)         #Reculer la tortue pour tracé la grille
    lignes(ny+1, largeur, largeur*nx)   #Lignes horizontales
    lt(90)                              #tourner à gauche de 90 degrés
    lignes(nx+1, -largeur, largeur*ny)  #Lignes verticales
    rt(90)                              #tourner à droite de 90 degrés
    positionner(largeur//2*nx, largeur//2*ny) #Repositionner tortue au centre




#La fonction index2dTo1d prend 2 paramètres de type entier positif, index2D et
#qui est un tableau 1D de longueur 2 et nbColonnes qui est le nombre de
#colonnes dans un tableau 2D.
#La fonction permet de convertir un index d'un tableau à deux dimensions à un
#index d'un tableau à 1 dimension. Elle retourne un entier positif.

def index2dTo1d(index2D, nbColonnes):
    index1D = nbColonnes*index2D[0] + index2D[1]  # calcul de l'index 1D
    return index1D                                # retourner l'index 1D


def testIndex2dTo1d(): #tests unitaires

    # cas où l'index est 0
    assert index2dTo1d([0,0],4) == 0

    # cas où la valeur de l'indice x et la valeur de l'indice y est la même
    assert index2dTo1d([3,3],4) == 15

    # cas où la valeur de l'indice x et la valeur de l'indice y est différente
    assert index2dTo1d([1,2],3) == 5

    # cas où on change l'ordre des valeurs dans l'index
    assert index2dTo1d([2,1],2) == 5

    # cas général
    assert index2dTo1d([3,2],3) == 11

testIndex2dTo1d()


#La fonction nbVoisins compte le nombre de voisins vivants pour une cellule
#dans la grille du jeu. Elle prend 5 paramètres : x et y représentent
#les coordonnées de la cellule dans la grille (type:entiers), nx et ny qui sont
#les nombres de cases dans l'axe des x et dans l'axe des y respectivement
#(type:entiers), et grille qui est le modèle du jeu à un état représenté sous
#forme de tableau.
#Elle retourne un entier, qui est le nombre de voisins vivants pour la cellule
#spécifiée.


def nbVoisins(x,y,nx,ny,grille):

    nb = 0                          # compteur de voisins
    index0 = index2dTo1d([x,y],ny)  # index 1D de la cellule courante

    #Parcourir les cellules voisines dans la grille
    #Le max et Le min évitent que les variables i et j prennent les
    #indexes hors de la grille.

    for i in range(max(x-1,0), min(x+1,nx-1)+1):
        for j in range(max(y-1,0), min(y+1,ny-1)+1):

            index = index2dTo1d([i,j], ny) # index 1D de la cellule voisine

            # incrémentation du compteur de voisins si la cellule est vivante
            nb +=  grille[index]

    #retourner le nombre de voisins vivants, en excluant la cellule courante
    return (nb - grille[index0])

def testNbVoisins(): #tests unitaires

    # Nombre de voisins au ...

    # premier point du tableau 2D [[1,1,1], [1,1,1], [1,1,1]]
    assert nbVoisins(0,0, 3,3,[1,1,1,1,1,1,1,1,1]) == 3

    # point milieu du tableau 2D [[1,1,1], [1,1,1], [1,1,1]]
    assert nbVoisins(1,1, 3,3,[1,1,1,1,1,1,1,1,1]) == 8

    # premier point du tableau 2D [[1,0,1], [1,1,1], [1,1,1]]
    assert nbVoisins(0,0, 3,3,[1,0,1,1,1,1,1,1,1]) == 2

    # dernier point du tableau 2D  [[1,0,1], [1,1,1], [1,1,1]]
    assert  nbVoisins(2,2, 3,3,[1,0,1,1,1,1,1,1,1]) == 3

    # cas où le nombre de ligne est diffèrent du nombre de colonne
    # point à la ligne 1 et colonne 0
    assert nbVoisins(1,0, 3,3,[1,0,1,1,1,1,1,1,1]) == 4

    # point à la ligne 0 et colonne 1
    assert nbVoisins(0,1, 3,3,[1,0,1,1,1,1,1,1,1]) == 5

    #cas général: point (0,1) du tableau 2D à 2 lignes et 3 colonnes
    #[[1,0,1], [1,1,1], [1,1,1]]
    assert nbVoisins(0,1,2,3,[1,0,1,1,1,1]) == 5

    #cas général: point (0,1) du tableau 2D à 3 lignes et 2 colonnes
    #[[1,0],[1,1],[1,1]]
    assert nbVoisins(0,1,3,2,[1,0,1,1,1,1]) == 3

testNbVoisins()


# La procédure jouer prend un paramètre tailleGrille, qui est un enregistrement
# possédant 3 champs : nx le nombre de cases sur l'axe x, ny le nombre de
# cases sur l'axe y et largeur qui est la largeur d'une case.
# La procédure créé une grille de jeu, initialise et démarre le jeu en boucle
# infinie.

def jouer(tailleGrille):

    nx = tailleGrille.nx   # le nombre de cases sur l'axe x
    ny = tailleGrille.ny   # le nombre de cases sur l'axe y

    #Créer la grille
    grille = creerGrille(tailleGrille)

    #Initialiser la grille avec des cellules vivantes
    init(grille)

    #Passer au prochain "tour"
    while True:

        # dessiner grille du jeu à l'étape actuelle
        dessinerGrille(tailleGrille,grille)

        #création d'une nouvelle grille, modèle au prochain état du jeu
        grille2 = creerGrille(tailleGrille)

        #parcourir chaque cellule de la grille
        for x in range(0,nx):
            for y in range(0,ny):

                #nombre de voisins vivants pour la cellule courante
                voisin = nbVoisins(x,y, nx,ny, grille)
                index = index2dTo1d([x,y],ny) # index 1D de la cellule courante

                #si la cellule a 2 voisins vivants, son état reste inchangé
                if voisin == 2:
                     grille2[index] = grille[index]

                # sinon si la cellule a 3 voisins vivants, on aura la naissance
                # d'une cellule
                elif voisin == 3:
                     grille2[index] = 1

                #sinon décès de la cellule
                else:
                     grille2[index] = 0

        grille = grille2  # mettre à jour la grille avec le nouvel état
        sleep(0.1)        # attendre 0.1 seconde

#Démarrer le jeu de la vie
tailleGrille = struct(nx=20, ny=20, largeur=10)
jouer(tailleGrille)