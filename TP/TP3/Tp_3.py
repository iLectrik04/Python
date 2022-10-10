# TP 03 - LOISEAU Lucas TD4-2

#Exo 1 :

from string import ascii_letters, digits
ACCENTS = 'àâäèéêëîïòôöùûüç'
SYMBOLES = ',.!?:; \n\t&"\'@%+-/\\*_()[]{}'
ALPHABET = ascii_letters + ACCENTS + digits + SYMBOLES


# Exo 2 :

def input_mode():
    """
    Determine un choix a faire
    
    :param: input(str)
    :return: choix(str)
    """
    choix = input("Voulez-vous chiffrer ou déchiffrer un message (c/d) ?")
    choix_possible = ("c","d","C","D")
    while choix not in choix_possible :
        print("Option invalide")
        choix = input("Voulez-vous chiffrer ou déchiffrer un message (c/d) ?")
    return choix

# Exo 3 :

def input_cle():
    """
    Determine la cle de cryptage
    
    :param: input(int)
    :return: cle(int)
    """
    cle = int(input("Entrez la clé de chiffrement (1-104) :"))
    while cle > len(ALPHABET):
        print("Clé invalide")
        cle = int(input("Entrez la clé de chiffrement (1-104) :"))
    else :
        return cle
    
    
# Exo 4 :

def pos(c):
    """
    Determine la position d'une lettre dans ALPHABET
    
    :param: c(str)
    :return: i(int)
    """
    if c not in ALPHABET:
        return "-1"
    for i in range(0,104):
        if c == ALPHABET[i] :
            return i

# Exo 5 :

def car(n):
    """
    Determine le caractere qui se trouve a la position n dans ALPHABET
    
    :param: n(int)
    :return: ALPHABET[n](str)
    """
    if n > len(ALPHABET):
       n -= len(ALPHABET)
    return ALPHABET[n]

# Exo 6 :

def chiffre_car(c,n):
    """
    Determine l'element dans ALPHABET qui est a n indice de c
    
    :param: c(str), n(int)
    :return: ALPHABET[n]
    """
    c = pos(c)
    return car(c+n)

# Exo 7 :

def cesar(message,mode,cle):
    """
    La fonction crypte et decrytpte un message en code cesar
    
    :param: message(str), mode(str), cle(int)
    :return: message(str)
    """
    result = ""
    for i in range(len(message)):
        if mode == "c" :
            result = result + car(pos(message[i]) + cle)
        if mode == "d" :
            result = result + car(pos(message[i]) - cle)
    return result
    

# Exo 8 :

def input_methode():
    """
    Determine un choix a faire
    
    :param: input(str)
    :return: choix(str)
    """
    choix = input("Quelle methode voulez-vous utiliser : Cesar (c) ou Vigenere (v) ?")
    choix_possible = ("c","v")
    while choix not in choix_possible :
        print("Option invalide")
        choix = input("Quelle methode voulez-vous utiliser : Cesar (c) ou Vigenere (v) ?")
    return choix

# Exo 9 :

def vigenere(message,mode,mot_cle):
    """
    La fonction crypte et decrytpte un message en code Vigenere
    
    :param: message(str), mode(str), mot_cle(int)
    :return: message(str)
    """
    result = ""
    j = 0
    for i in range(len(message)):
        if mode == "c":
            result = result + car(pos(message[i]) + pos(mot_cle[j]))     
        if mode == "d":
            result = result + car(pos(message[i]) - pos(mot_cle[j]))
        j += 1
        if j+1 == len(mot_cle)+ 1 :
            j = 0
    return result
    
# Exo 10 :

def main():
    """
    """
    result = ""
    message = input("Veuillez entrer votre message :")
    print(message)
    mode = input("Voulez-vous chiffrer ou déchiffrez un message (c/d) ?")
    choix_possible1 = ("c","d")
    while mode not in choix_possible1 :
        print("Option invalide")
        mode = input("Quelle methode voulez-vous utiliser : Cesar (c) ou Vigenere (v) ?")
    methode = input("Quelle méthode voulez-vous utiliser : Cesar (c) ou Vigenere (v) ?")
    choix_possible = ("c","v")
    while methode not in choix_possible :
        print("Option invalide")
        methode = input("Quelle methode voulez-vous utiliser : Cesar (c) ou Vigenere (v) ?")
    if methode == "c" :
        cle = int(input("Veuillez indiquer la clé :"))
        for i in range(len(message)):
            if mode == "c" :
                result = result + car(pos(message[i]) + cle)
            if mode == "d" :
                result = result + car(pos(message[i]) - cle)
        return result
    if methode == "v" :
        mot_cle = input("Veuillez indiquer le mot clé:")
        j = 0
        for i in range(len(message)):
            if mode == "c":
                result = result + car(pos(message[i]) + pos(mot_cle[j]))     
            if mode == "d" :
                result = result + car(pos(message[i]) - pos(mot_cle[j]))
            j += 1
            if j+1 == len(mot_cle)+ 1 :
                j = 0
        return result
        
    
    
    
    
    
    
    