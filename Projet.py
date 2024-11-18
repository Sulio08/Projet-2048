




def grille():
    """Retourne une grille de points
    :param x: (int) le nombre de colonnes
    :param y: (int) le nombre de lignes
    :return: (list) une grille de x lignes et y colonnes"""
    x= int(input("Combien de ligne pour la grille?"))
    y= int(input("Combien de colonne pour la grille?"))
    return[['.' for i in range(x)] for j in range(y)]
print(grille())


def afficher_grille(g):
    """Affiche la grille <g>
    :param g: (list) une grille
    :return: (None)"""
    for ligne in g:
        print("".join(ligne))


def deplacement_tuiles():
    pass

def jeu():
    pass