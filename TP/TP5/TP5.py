# TP5 - Lucas LOISEAU TD4-2

import random

HUMAIN = "X"
ORDI = "O"
VIDE = " "
T_PLATEAU = 3

plateau = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

# Focntion 1 :

def init_plateau():
    """
    On créé le plateau de jeu initial.
    
    :param: None
    :return: plateau(list)
    """
    plateau_vide = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    return plateau_vide

# Fonction 2 :

def print_plateau(plateau):
    """
    On affiche le plateau de jeu.
    
    :param: init_plateau(fnt)
    :return: plateau(list)
    """
    for i in range(len(plateau)):
        print(plateau[i][0] + " ⎮" , plateau[i][1] + " ⎮" ,plateau[i][2])
        if i < 2 :
            print("------")
    return "\nTic Tac Toe"
        
# Fonction 3 :

def input_humain(plateau):
    """
    On demande au joueur de jouer.
    
    :param: plateau(list of list)
    :return: couple(double tuple)
    """
    print(print_plateau(plateau))
    couple_0 = int(input("Veuillez rentrer la première coordonée (colonne) :"))
    couple_1 = int(input("Veuillez rentrer la deuxième coordonée (case) :"))
    while True :
        if len(str(couple_0)) != 1 or len(str(couple_1)) != 1 :
            print("Les valeurs entrées ne sont pas deux entiers.")
            couple_0 = int(input("Veuillez rentrer la première coordonée (colonne) :"))
            couple_1 = int(input("Veuillez rentrer la deuxième coordonée (case) :"))
        if couple_0 < 0 or couple_1 < 0 :
            print("Les valeurs entrées sont négatives.")
            couple_0 = int(input("Veuillez rentrer la première coordonée (colonne) :"))
            couple_1 = int(input("Veuillez rentrer la deuxième coordonée (case):"))
        while couple_0 > T_PLATEAU-1 or couple_1 > T_PLATEAU-1 :
            print("Les valeurs entrées ne sont pas comprises dans le tableau de jeu")
            couple_0 = int(input("Veuillez rentrer la première coordonée (colonne) :"))
            couple_1 = int(input("Veuillez rentrer la deuxième coordonée (case) :"))
        if plateau[couple_0][couple_1] != VIDE :
            print("Les coordonnées ne sont pas disponibles.")
            couple_0 = int(input("Veuillez rentrer la première coordonée (colonne) :"))
            couple_1 = int(input("Veuillez rentrer la deuxième coordonée (case) :"))
        else :
            break
    return couple_0 , couple_1
        
# Fonction 4 :

def coords_vides(plateau):
    """
    Determine les positions vides dans le plateau.
    
    :param: plateau
    :return: liste_coo(list)
    """
    liste_coo = []
    for i in range(T_PLATEAU):
        for j in range(T_PLATEAU) :
            if plateau[i][j] == VIDE :
                ajout = i,j
                liste_coo.append(ajout)
    return liste_coo

# Fonction 5 :

def input_ordi(plateau):
    """
    On demande a l'ordi de jouer.
    
    :param: plateau(list of list)
    :return: couple(double tuple)
    """
    print_plateau(plateau)
    cases_vides = coords_vides(plateau)
    if cases_vides == [] :
        return None 
    choix_ordi = random.choice(cases_vides)
    print("***********")
    return choix_ordi


# Focntion 6 :

def horizontales(joueur, plateau):
    """
    Cette fonction nous dit si un joueur a gagner en faisant une ligne horizontale.
    
    :param: joueur, plateau(list)
    :return: boolean(True or False)
    """
    for i in range(T_PLATEAU) :
        if joueur == "humain" :
            if plateau[i] == ["X","X", "X"] : 
                return True
        if joueur == "ordi" :
            if plateau[i] == ["O", "O", "O"] : 
                return True
    return False
    
def verticales(joueur, plateau):
    """
    Cette fonction nous dit si un joueur a gagner en faisant une ligne verticale.
    
    :param: joueur, plateau(list)
    :return: boolean(True or False)
    """
    for i in range(T_PLATEAU):
        if joueur == "humain":
            if plateau[0][i] == "X" and plateau[1][i] == "X" and plateau[2][i] == "X":
                return True
        if joueur == "ordi":
            if plateau[0][i] == "O" and plateau[1][i] == "O" and plateau[2][i] == "O":
                return True
    return False


def diagonales(joueur, plateau):
    """
    Cette fonction nous dit si un joueur a gagner en diagonale.
    
    :param: joueur, list ((str), (list(list))
    :return: (booleen)
    """
    if joueur == "humain":
        if plateau[0][0] == "X" and plateau[1][1] == "X" and plateau[2][2] == "X":
            return True
        if plateau[0][2] == "X" and plateau[1][1] == "X" and plateau[2][0] == "X":
            return True
    if joueur == "ordi":
        if plateau[0][0] == "O" and plateau[1][1] == "O" and plateau[2][2] == "O":
            return True
        if plateau[0][2] == "O" and plateau[1][1] == "O" and plateau[2][0] == "O":
            return True
    return False




def est_victoire(joueur, plateau):
    """
    Cette fonction nous dit si le joueur a gagné ou si l'ordi a gagné.
    
    :param: joueur(str), plateau(list)
    :return: "Félicitations tu as gagné(e) !!!"(str)  or  "Tu as perdu, dommage!"(str)
    """
    if joueur == "humain":
        if horizontales("humain", plateau) or verticales("humain", plateau) or diagonales("humain", plateau):
            return "Félicitaions tu as gagné(e) !!!"
    if joueur == "ordi":
        if horizontales("ordi", plateau) or verticales("ordi", plateau) or diagonales("ordi", plateau):
            return "Tu as perdu, dommage !!!"
        
# Fonction 7 :

def joue_partie():
    """
    Cette fonction permet de lancer une partie de Tic Tac Toe.
    
    :param: None
    :return: None
    """
    plateau = init_plateau()
    coup = 0
    while coup != 9:
        coord_humain = input_humain(plateau)
        plateau[coord_humain[0]][coord_humain[1]] = "X"
        coup+=1
        if est_victoire("humain", plateau) == "Bravo tu as gagné(e) !!!":
            print(print_plateau(plateau))
            print("Bravo tu as gagné(e) !!!")
            print("***************************\n***************************")
            break
        coord_ordi = input_ordi(plateau)
        plateau[coord_ordi[0]][coord_ordi[1]] = "O"
        coup += 1
        if est_victoire("ordi", plateau) == "Tu as perdu, dommage!":
            print(print_plateau(plateau))
            print("Tu as perdu, dommage!")
            print("***************************\n***************************")
            break
        if coup == 9:
            print("Dommage, personne n'as gagnés...")
            print("***************************\n***************************")
            break
        
# Fonction 8 :

def input_rejouer():
    """
    Cette fonction demande si l'utilisateur veut rejouer.
    
    :param: None
    :return: boolean(True or False)
    """
    reponse = input("Voulez-vous rejouez ? (oui ou non / o ou n) : ")
    while True:
        if reponse == "oui" or reponse == "o" :
            return True
        if reponse == "non" or reponse == "n":
            return False
        reponse = input("Reponse incorrect \nVoulez-vous rejouez ? (oui ou non / o ou n) : ")
        
# Fonction 9 :

def main():
    """
    Cette fonction permet de lancer le jeu automatiquement. (Elle regroupe toutes les fonctions au dessus.)
    
    :param: None
    :return: None
    """
    joue_partie()
    while input_rejouer() != False:
        joue_partie()
        input_rejouer()
        
main()


    