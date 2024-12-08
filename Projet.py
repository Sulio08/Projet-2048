import random

def init_grille():
    x = int(input("Combien de lignes pour la grille? (doit être >= 4)    "))
    y = int(input("Combien de colonnes pour la grille? (doit être >= 4)  "))
    if x < 4 or y < 4:
        print("Attention les dimensions de la grille doivent être supérieures ou égales à 4.")
        return init_grille()  
    else:
        return [[0 for i in range(y)] for j in range(x)]


def demander_direction():
    directions = {"z": "haut", "s": "bas", "q": "gauche", "d": "droite"}
    choix = ""
    while choix not in directions:
        choix = input("Choisissez une direction (z=haut, s=bas, q=gauche, d=droite) : ").lower()
    return choix

def afficher_grille(g):
    lignes = len(g)
    colonnes = len(g[0])
    print("|" + "-------" * colonnes)
    for i in range(lignes):
        ligne = "| "
        for j in range(colonnes):
            if g[i][j] == 0:
                ligne += "     "
            else:
                ligne += str(g[i][j]).rjust(5)
            ligne += "| "
        print(ligne)
        print("|" + "-------" * colonnes)

def ajouter_tuile(g):
    cases_vides = []
    for i in range(len(g)):
        for j in range(len(g[i])):
            if g[i][j] == 0:
                cases_vides.append((i, j))
    if cases_vides:
        i, j = random.choice(cases_vides)
        g[i][j] = random.choice([2, 4])


def deplacer_a_gauche(ligne):
    n_ligne = []
    for x in ligne:
        if x != 0:
            n_ligne.append(x)

    i = 0
    while i < len(n_ligne) - 1:
        if n_ligne[i] == n_ligne[i + 1]:
            n_ligne[i] = n_ligne[i] + n_ligne[i + 1]
            n_ligne.pop(i + 1)
        i += 1

    while len(n_ligne) < len(ligne):
        n_ligne.append(0)

    return n_ligne

def deplacer_grille(g, direction):
    lignes = len(g)
    colonne = len(g[0])

    if direction == "q":
        for i in range(lignes):
            g[i] = deplacer_a_gauche(g[i])

    elif direction == "d":
        for i in range(lignes):
            g[i] = deplacer_a_gauche(g[i][::-1])[::-1]

    elif direction == "z":
        for j in range(colonne):
            colonne = [g[i][j] for i in range(lignes)]
            nouvelle_c = deplacer_a_gauche(colonne)

            for i in range(lignes):
                g[i][j] = nouvelle_c[i]

    elif direction == "s":
        for j in range(colonne):
            colonne = [g[i][j] for i in range(lignes)]
            nouvelle_c = deplacer_a_gauche(colonne[::-1])[::-1]

            for i in range(lignes):
                g[i][j] = nouvelle_c[i]


g = init_grille()
ajouter_tuile(g)
ajouter_tuile(g)

while True:
    afficher_grille(g)
    direction = demander_direction()
    ancienne_g = [ligne[:] for ligne in g]  
    deplacer_grille(g, direction)
    if g != ancienne_g:  
        ajouter_tuile(g)
    else:
        print("Déplacement impossible. Essayez une autre direction.")