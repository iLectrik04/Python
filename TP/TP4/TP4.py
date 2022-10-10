#TP 4 - LOISEAU Lucas TD4-2

import random

def choisir_mot():
    """
    Demande a l'utilisateur de choisir des mots
    
    :param: None
    :return: mot(str)
    """
    liste_mot = []
    for i in range(0,2):
        mot = str(input("Choisissez votre mot :"))
        liste_mot.append(mot)
    return random.choice(liste_mot)

def est_dans(lettre,mot):
    """
    Teste si un caractere apparaît dans une autre chaine de caractere
    
    :param: lettre(str),mot(str)
    :return: boolean(True or False)
    """
    for i in range(len(mot)):
        if lettre == mot[i]:
            return True
    return False


chiffre = ("0","1","2","3","4","5","6","7","8","9","0")
def input_lettre():
    """
    Demande a l'utilisateur de choisir une lettre
    
    :param: None
    :return: lettre(str)
    """
    props = []
    lettre = str(input("Proposez une lettre (en minuscule) :"))
    while True :
        if len(lettre) != 1 :
            print("Proposez une seule lettre, s'il vous plaît.")
            lettre = str(input("Proposez une lettre(en miniscule) :"))
        elif lettre in chiffre:
            print(lettre,"n'est pas une lettre.")
            lettre = str(input("Proposez une lettre(en minuscule) :"))
        elif lettre in props :
            print("Vous avez déjà proposé cette lettre.")
            lettre = str(input("Proposez une lettre(en minuscule) :"))
        else :
            break
    props.append(lettre)
    print(props)
    return lettre

def dessine_ecran(erreurs):
    """
    Dessine l'ecran du jeu de base
    
    :param: erreurs(int)
    :return: dessin(str)
    """
    FIGURES_PENDU = ['''
   +---+
   |   |
       |
       |
       |
       |
==========''','''
   +---+
   |   |
   O   |
       |
       |
       |
==========''','''
   +---+
   |   |
   O   |
   |   |
       |
       |
==========''','''
   +---+
   |   |
   O   |
  /|   |
       |
       |
==========''','''
   +---+
   |   |
   O   |
  /|\  |
       |
       |
==========''','''
   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
==========''','''
   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
==========''']
    return FIGURES_PENDU[erreurs]
    
    
def affiche_erreurs(erreurs):
    """
    Affiche les erreurs
    
    :param: erreurs(str)
    :return: recap_erreur(str)
    """
    if erreurs > 1 :
        print("Erreurs : ")
    else :
        
        print("Erreur : ")
    return erreurs
    
def affiche_correctes(lettre,mot):
    """
    Affiche les lettres correctes dans le mot
    
    :param: lettre(str),mot(str)
    :return: affiche(str)
    """
    affiche = ""
    for i in range(len(mot)):
        if mot[i] in lettre :
            affiche += " " + mot[i]
        else :
            affiche += " _ "
    return affiche

def gagne(lettres_b,mot):
    """
    Determine si le joueur a trouver le mot
    
    :param: lettres(str), mot(str)
    :return: boolean(True or False)
    """
    for i in range(len(mot)):
        if mot[i] not in lettres_b :
            return False
    return True


def main():
    """
    Fonction principale du jeu du pendu
    
    :param: None
    :return: None
    """
    erreurs = 0
    lettres_b = ""
    lettres_m = ""
    props =[]
    mot = choisir_mot()
    while erreurs != 6 or gagne :
        print(dessine_ecran(erreurs))
        lettre  = input_lettre()
        if lettre in mot :
            lettres_b += lettre
            props += lettre
            print(dessine_ecran(erreurs))
            print(affiche_correctes(lettres_b,mot))
        if lettre not in mot :
            erreurs += 1
            lettres_m += lettre
            props += lettre
            print(props)
            print(dessine_ecran(erreurs))
            print(affiche_erreurs(erreurs))
        if erreurs == 6 :
            print("Tu as perdu dommage, essaie une autre fois")
            break
        if gagne(lettres_b,mot) :
            print("Bravo tu as trouvé le mot")
            break
        
        
        
        
            
            