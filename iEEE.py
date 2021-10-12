# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 09:39:23 2021

@author: Yann
"""
fin = ''
intbin = ''
nombre = float(input('entrez le nombre a convertir: '))
n = nombre
while n<0:
    fin = fin+'1'
    entier = int((nombre*-1)//1)
    n = 0

while n>0:
    fin = fin+'0'
    entier= int(nombre//1)

    n=0
i =1
q=entier
count = 0
while q!=0:
    r=q%2
    q=q//2
    while r==0:
        intbin = '0' + intbin
        r = 2
        count = count+1
    while r==1:
        c = q
        while c!=0:
            intbin = '1' + intbin
            count = count+1
            c = 0
        r = 2
    i = i+1
decimal = nombre-entier
d = decimal
decbin = ""
i = 0
counttwo =0
while d>0:
    d=d*2
    a = d
    while a>=1:
        d = d-1
        a=0
        decbin = decbin +'1'
        counttwo = counttwo+1
    while a<1:
        while a!=0:
            a = 0
            decbin = decbin +'0'
            counttwo = counttwo+1
        a = 1
mantisse = intbin+decbin
d = 0
while d<23-counttwo-count:
    mantisse = mantisse+'0'
    d =d+1
exponant = 254-(127-count)
q = exponant
i =1
exponantbin = ''
while q!=0:
    r=q%2
    q=q//2
    while r==0:
        exponantbin = '0' + exponantbin
        r = 2
    while r==1:
        exponantbin = '1' + exponantbin
        r = 2
    i = i+1

fin = fin+exponantbin+mantisse
print(fin)
