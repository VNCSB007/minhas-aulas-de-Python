# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 16:10:59 2021

@author: vini
"""

def contador_letras (lista_palavra):
    contador = []
    for x in lista_palavra:
        quantidade = len(x)
        contador.append(quantidade)
    return contador

if __name__ == '__main__':
    lista = ['cachorro', 'gato']
    print(contador_letras(lista))