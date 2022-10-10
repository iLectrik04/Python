import math
# Exo1 :
def triangle():
    """
    Calculez l'aire d'un triangle equilateral
    
    :param: h(int)
    :return: aire(float)
    """
    h = int(input("Donnez la hauteur du triangle :"))
    aire = h**2 * math.sqrt(3) / 4
    return aire
# Exo 2 :
def etoile_six_branches():
    """
    Calculez l'aire d'une etoile consitué de deux triangles equilateral
    
    :param: h(int)
    :return: aire(float)
    """
    aire_1 = triangle()
    aire_2 = aire_1 / 3
    return aire_2
# Exo 3 :
def surface_a_peindre():
    """
    Calculez le nombre de pot de peinture selon une surface definie
    
    :param: dimension(int)
    :return: total_pot(float)
    """
    largeur = int(input("Donnez la largeur du mur :"))
    longueur = int(input("Donnez la longueur du mur :"))
    hauteur = int(input("Donnez la hauteur de la pièce :"))
    air1 = longueur * hauteur * 2
    air2 = largeur * hauteur * 2
    air3 = longueur * largeur
    surface = (air1 + air2 + air3)
    return surface

def litres(contenance_pot,couv_litre):
    """
    Calculez le nombre de surface avec 1 pot
    
    :param: contenance_pot and couv_litre
    :return: couv_pot
    """
    couv_pot = contenance_pot * couv_litre
    return couv_pot

def nombre_pots(surface,couv_pot):
    """
    Determiner le nbr de pots total pour peindre la piece.
    
    :param: surface and couv_pot
    :return: nb_pots(float)
    """
    nb_pots = surface / couv_pot
    return nb_pots

# Exo 4 :
"""

>>> a = 6
>>> type(a) -> class int

>>> b = a / 4
>>> type(b) -> class float

>>> nom = "Dupont"
>>> type(nom) -> class str

>>> cond1 = a < b
>>> type(cond1) -> class bool

"""

# Exo 5 :

def annee_bissextile(year):
    """
    Determine si une annee est bissextile
    
    :param: year(int)
    :return: Booleen(True or False)
    """
    bool = False
    if (year % 4 == 0 and
        year % 100 != 0 or
        year % 400 == 0):
        bool = True
    return bool

#Exo 6 :

def nbre_jours_mois(month,year):
    """
    Determine le nombre de jour d'un mois et d'une annee.
    
    :param: month(int),year(int)
    :return: nj(int)
    """
    nj = (0,31,28,31,30,31,30,31,31,30,31,30,31)[month] # nj = nombre-jour et month = mois.
    if month == 2 and ((year % 4 == 0 and
                        year % 100 != 0) or
                        year % 400 == 0):
        return nj + 1
    return nj

#Exo 7 :

def numero_jour(d,m,y):
    """
    Determine le numero d'un jour choisit en parametre.
    
    :param: d(int),m(int),y(int)
    :return: nb_d(int)
    """
    nb_d = 0
    for i in range(1, m):
        nb_d = nbre_jours_mois(i,y) + nb_d
    return nb_d + d

#Exo 8 :

def nbre_jours_debut_ere(year):
    """
    Determine le nombre de jours depuis le début de l'ere chretienne.
    
    :param: year(int)
    :return: days(int)
    """
    days = 0
    i = 0
    for i in range(year):
        if annee_bissextile(i):
            days += 366
        else :
            days += 365
    return days

#Exo 9 :

def nbre_jours_debut_ere_jma(d,m,y):
    """
    Determine le nombre de jour depuis l'ere chretienne pour une date precise.
    
    :param: d(int),m(int),y(int)
    :return: days(int)
    """
    days = 0
    days = numero_jour(d,m,y) + nbre_jours_debut_ere(y-1)
    return days

#Exo 10 :

def nbre_jours_entre_deux_dates(d1,m1,y1,d2,m2,y2):
    """
    Determine le nombre de jorus entre deux dates.
    
    :param: date1(int),date2(int)
    :return: days(int)
    """
    days = nbre_jours_debut_ere_jma(d2,m2,y2) - nbre_jours_debut_ere_jma(d1,m1,y1)
    return days

#Exo 11 :

def suivant_syracuse(n):
    """
    Determine la suite de syracuse
    
    :param: n(int)
    :return: n(int)
    """
    if n % 2 == 0:
        n = n // 2
    else :
        n = n*3 + 1
    return n
    
#Exo 12 :

def nb_etapes_syracuse(n):
    """
    Determine le nombre d'etapes afin d'arriver a la valeur 1.
    
    :param: n(int)
    :return: etapes(int)
    """
    etapes = 0
    while n!= 1:
        etapes = etapes + 1
        n = suivant_syracuse(n)
    return etapes
        
def altitude_syracuse(n):
    """
    Determine la plus grande valeur sur le chemin de n a 1 dans la suite de Syracuse
    
    :param: n(int)
    :return: alt(int)
    """
    alt = 0
    while n != 1:
        n = suivant_syracuse(n)
        if alt < n:
            alt = alt + 1
    return alt

    
