# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 00:39:29 2021

@author: vini
"""

conjunto_a = {1,2,3}
conjunto_b = {1,2,3,4,5}
lista_animais = ["cachorro","cachorro", "gato", "gato", "elefante"]

conjunto_animais = set(lista_animais)
print(conjunto_animais)
lista_animais = list(conjunto_animais)
print(lista_animais)

conjunto_subset = conjunto_b.issubset(conjunto_a)
conjunto_subset2 = conjunto_a.issubset(conjunto_b)
conjunto_superset = conjunto_b.issuperset(conjunto_a)
conjunto_superset2 = conjunto_a.issuperset(conjunto_b)

print(conjunto_subset)
print(conjunto_subset2)
print(conjunto_superset)
print(conjunto_superset2)




"""
conjunto = {5,1,2,3,4, 4, 6}
conjunto2 = {10,6,7,8,9, 7, 5}


#não faz diferença como você unirá, sempre será feito do menor pro maior (tuplas não usam union) e cada valor será mostrado uma vez
conjunto_uniao = conjunto.union(conjunto2)
conjunto_uniao2 = conjunto2.union(conjunto)

conjunto_intersecção = conjunto.intersection(conjunto2)
#nesse caso, a ordem dos sets faz DIFERENÇA
conjunto_diferença = conjunto.difference(conjunto2)
conjunto_diferença2 = conjunto2.difference(conjunto)


print(conjunto_uniao)
print(conjunto_uniao2)
print(conjunto_intersecção)
print(conjunto_diferença)
print(conjunto_diferença2)
"""

"""
conjunto = {1,2,3,4, 4}
conjunto.add(5)
conjunto.discard(2)
print(conjunto)
"""
