# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 09:39:23 2021

@author: Yann
"""
fin = ''

nombre = float(input('entrez le nombre a convertir: '))
n = nombre
#si le nombre est négatif on met le MSB à 1 et on passe le nombre réel en positif
while n<0:
    fin = fin+'1'
    #on sépare l'entier de la paartie décimale
    entier = int((nombre*-1)//1)
    nombre = (nombre*-1)/1

    n = 0
#si le nombre est négatif on met le MSB à 0

while n>0:
    fin = fin+'0'
    #on sépare l'entier de la paartie décimale
    entier= int(nombre//1)
    n=-1
#on affiche le MSB
print("le MSB: "+fin)

#Puis on convertit l'entier en binaire
i =1
entier2=entier
integerbin = ''
#on initialise le compteur pour la longueur de la mantisse (max 23)
exposant_positif = 0
while entier2!=0:
    r=entier2%2
    entier2=entier2//2
    while r==0:
        integerbin = '0' + integerbin
        r = 2
        exposant_positif = exposant_positif+1
    while r==1:
        entier3 = entier2
        while entier3!=0:
            integerbin = '1' + integerbin
            exposant_positif = exposant_positif+1
            entier3 = 0
        r = 2
    i = i+1

#exeption si l'entier est nul il se peut que l'exposant soit négatif
entier2 = entier
decimal = nombre-entier #on calcule le décimal en retirant la partie entière du nombre de départ
decimal2 = decimal
decimal3 = decimal
decimal4 = decimal
decimalbin = ""
count = exposant_positif
i = 0
exposant_negatif = 0
#tant que le décimal*2 est plus petit que 1 alors enlève 1 a l'exposant negatif
while entier2==0:
    while decimal3<1:
        decimal2=decimal2*2
        exposant_negatif = exposant_negatif-1 #on enlève 1 a l'exposant négatif
        decimal3 = decimal2
        decimal4 = decimal2
        while decimal4>1:
            decimal2 = decimal2-1
            decimal4 = 0
    entier2 = 1


#Ici on calcule le reste de la mantisse
while decimal2>0:

    decimal2=decimal2*2
    decimal3 = decimal2
    #si le reesulat est plus grand ou égal à 1
    while decimal3>=1:
        decimal2 = decimal2-1 #on enlève 1 au résulat et on continue

        decimalbin = decimalbin +'1' #on ajoute le caractère"1" à la mantisse
        count = count+1
        decimal3=0



#si le reesulat est plus grand ou égal à 1
    while decimal3<1:
        while decimal3!=0:

            decimalbin = decimalbin +'0'#on enlève 1 au résulat et on continue
            count = count+1
            decimal3 = 0

        decimal3 = 1
        
        longueurmax_mantisse=23
#si la mantisse est égale à 23 alors on quite le while de plus haut
    while count>=longueurmax_mantisse:
        decimal2=0
        longueurmax_mantisse=24


mantisse = integerbin+decimalbin
i = 0
while i<23-count:#on rajoute les zéros nécéssaires pour avoir une mantisse de 23 bits
    mantisse = mantisse+'0'
    i =i+1
print("La mantisse: "+mantisse)



exposant = 254-127+exposant_positif+exposant_negatif

#on convertit l'exposant en binaire
q = exposant
i =1
exposantbin = ''
while q!=0:
    r=q%2
    q=q//2
    while r==0:
        exposantbin = '0' + exposantbin
        r = 2
    while r==1:
        exposantbin = '1' + exposantbin
        r = 2

    i = i+1
#on rajoute les Zéros nécéssaires pour faire un octet
while i<9:
    exposantbin = '0' + exposantbin
    i = i+1

print("le binaire de l'exposant: "+exposantbin)
#enfin on rassemble toutes les parties et le tour est joué
fin = fin+exposantbin+mantisse
print("le résulat final: "+fin)
