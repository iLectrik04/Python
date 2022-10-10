#TP 02 - LOISEAU Lucas TD4

#Exo 1 :

def somme_chiffres(n):
    """
    Fait la somme des chiffres fourni en parametre
    
    :param: n(int)
    :return: res(int)
    """
    if n // 10 == 0:
        return n
    else:
        return n % 10 + somme_chiffres( n // 10 )
    
#Exo 2 :
    
def nombre_ordonne(n):
    """
    Determine si les chiffres en parametre sont en ordre croissant
    
    :param: n(int)
    :return: boolean(True or False)
    """
    n = str(n)
    for i in range(0,len(str(n))-1):
        if n[i] > n[i+1]:
            return False
    return True

#Exo 3:
        
def est_voyelle_min(L):
    """
    Teste si une chaine de caracteres comporte une voyelle miniscule.

    :param: L(list)
    :return: boolean(True or False)
    """
    list_1 = ["a","e","i","o","u","y"]
    return L in list_1
        
#Exo 4 :
        
def est_voyelle_maj(L):
    """
    Teste si une chaine de caracteres comporte une voyelle majuscule ou miniscule.
    
    :param: L(list)
    :return: boolean(True or False)
    """
    list_1 = ["A","E","I","O","U","Y"]
    return L in list_1
        
#Exo 5 :
        
def est_voyelle(L):
    """
    Teste si une chaine de caracteres comporte une voyelle majuscule ou miniscule.
    
    :param: L(list)
    :return: boolean(True or False)
    """
    list_1 = ["A","E","I","O","U","Y","a","e","i","o","u","y"]
    return L in list_1
        
#Exo 6 :
def compte_voyelles(mot):
    """
    Cette fonction donne le nombre de voyelle qu'il y a dans un mot
    
    :param: mot(str)
    :return: compte(int)
    """
    compte = 0
    for i in range(len(mot)):
        if est_voyelle(mot[i]):
            compte+=1
    return compte


#Exo 7 :
def est_majuscule(lettre):
    maj = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
    """
    Cette fonction dit si oui ou non la lettre est une majuscule
    
    :param: lettre(str)
    :return: boolean(True or False)
    """
    return lettre in maj


#Exo 8 :
def est_minuscule(lettre):
    min = ['a','b','c','d','e','f','g','h','i','j','k','l','m', 'n','o','p','q','r','s','t','u','v','w','x','y','z']
    """
    Cette fonction dit si oui ou non la lettre est une minuscule
    
    :param: lettre(str)
    :return: boolean(True or False)
    """
    return lettre in min


#Exo 9 :
def est_lettre(l):
    """
    Cette fonction dit si oui ou non l est une lettre (minuscule ou majuscule)
    
    :param: l(str)
    :return: boolean(True or False)
    """
    return est_majuscule(l) or est_minuscule(l)


#Exo 10 :
def compte_maj(mot):
    """
    Cette fonction donne le nombre de majuscule dans un mot/phrase
    
    :param: mot(str)
    :return: maj(int)
    """
    maj = 0
    for i in range(len(mot)):
        if est_majuscule(mot[i]):
            maj += 1
    return maj


#Exo 11 :
def maj(mot):
    """
    Cette fonction dit si il y a une majuscule dans le mot/phrase
    
    :param: mot(str)
    :return: boolean(True or False)
    """
    for i in range(len(mot)):
        if est_majuscule(mot[i]):
            return True
    return False


def minu(mot):
    """
    Cette fonction dit si il y a une minuscule dans le mot/phrase
    
    :param: mot(str)
    :return: boolean(True or False)
    """
    for i in range(len(mot)):
        if est_minuscule(mot[i]):
            return True
    return False


chiffres = ["1","2","3","4","5","6","7","8","9","0"]
def chiffre(mot):
    """
    Cette fonction dit si il y a un chiffre dans le mot/phrase
    
    :param: mot(str)
    :return: boolean(True or False)
    """
    for i in range(len(mot)):
        if mot[i] in chiffres:
            return True
   
   
symboles = ["+","-","@","?","!","*","$"]
def symbole(mot):
    """
    Cette fonction dit si il y a un symbole dans le mot/phrase
    
    :param: mot(str)
    :return: boolean(True or False)
    """
    for i in range(len(mot)):
        if mot[i] in symboles:
            return True
 
 
def teste_mdp(mot):
    """
    Cette fonction donne si le mot de passe rentré est assez fort ou non
    
    :param: mot(str)
    :return: boolean(True or False)
    """
    return maj(mot) and minu(mot) and  chiffre(mot) and symbole(mot) and len(mot)>=8


#Exo 12 :
def copie_sauf(mot, lettre):
    """
    Cette fonction donne un mot sans une lettre choisi
    
    :param: mot, lettre(str)
    :return: mot_sans_lettre
    """
    mot_sans_lettre = ""
    for i in range(len(mot)):
        if mot[i] != lettre:
            mot_sans_lettre += mot[i]
    return mot_sans_lettre
            

#Exo 13 :
def remplace(mot, enlever, remplacer):
    """
    Cette fonction remplace une lettre par une autre lettre dans un mot/phrase
    
    :param: mot, enlever, remplacer(str)
    :return: mot_remplace(str)
    """
    mot_remplace = ""
    for i in range(len(mot)):
        if mot[i] == enlever:
            mot_remplace += remplacer
        else:
            mot_remplace += mot[i]
    return mot_remplace
    
    
#Exo 14 :
def derniers(mot, nbr):
    """
    Cette fonction donne les nbr dernières lettre d'un mot
    
    :param: mot(str), nbr(int)
    :return: mot_
    """
    mot_ = ""
    for i in range(len(mot)-nbr, len(mot)):
        mot_ += mot[i]
    return mot_


#Exo 15 :
alphabet_maj = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
alphabet_min = ('a','b','c','d','e','f','g','h','i','j','k','l','m', 'n','o','p','q','r','s','t','u','v','w','x','y','z')
def min_to_maj(lettre):
    """
    Cette fonction donne une lettre minuscule en majuscule
    
    :param: lettre(str)
    :return: alphabet_maj[i](str)
    """
    for i in range(len(alphabet_min)):
        if lettre == alphabet_min[i]:
            return alphabet_maj[i]


#Exo 16 :
def maj_to_min(lettre):
    """
    Cette fonction donne une lettre majuscule en minuscule
    
    :param: lettre(str)
    :return: alphabet_min[i](str)
    """
    for i in range(len(alphabet_maj)):
        if lettre == alphabet_maj[i]:
            return alphabet_min[i]


#Exo 17 :
def majuscules(mot):
    """
    Cette fonction donne un mot minuscule+majuscule en majuscule
    
    :param: lettre(str)
    :return: new_mot(str)
    """
    new_mot = ""
    for i in range(len(mot)):
        if mot[i] in alphabet_min:
            new_mot += min_to_maj(mot[i])
        else:
            new_mot += mot[i]
    return new_mot


def minuscules(mot):
    """
    Cette fonction donne un mot minuscule+majuscule en minuscule
    
    :param: lettre(str)
    :return: new_mot(str)
    """
    new_mot = ""
    for i in range(len(mot)):
        if mot[i] in alphabet_maj:
            new_mot += maj_to_min(mot[i])
        else:
            new_mot += mot[i]
    return new_mot
    

    