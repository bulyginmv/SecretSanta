# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 23:57:42 2018

@author: Misha
"""
from numpy import random
get_families=open('families.txt','r',encoding='utf-8-sig')
families=get_families.readlines()
get_genres=open('genres.txt','r',encoding='utf-8-sig')
genres=get_genres.readlines()
def shufflelist(f):
    rf=f[:]
    while True:
        random.shuffle(rf)
        for a,b in zip(f,rf):
            if a==b:
                break
        else:
            return rf
rfamilies=shufflelist(families)
nl='\n'
random.shuffle(genres)
for a,b,c in zip(families,rfamilies,genres):
    text=open(f'C:/new_year/{a.rstrip(nl)}.txt','w',encoding='utf-8')
    text.write(f'Привет! Вы дарите подарок этой семье: {b.rstrip(nl)} ! {nl}Для сценки вам выпал жанр: {c.rstrip(nl)} !')
    text.close()
