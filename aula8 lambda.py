# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 19:26:12 2021

@author: vini
"""

#from aula8 contador_letras import contador_letras
#é possivel importar mais de uma class por módulo, ao digitar from aula8 contador_letras import contador_letras, teste

lista = ['cachorro', 'gato', 'elefante']
#print(contador_letras(lista))


#lambda: função anõnima 
#só e eficiente com funções de apenas uma linha 
contador_letras = lambda lista: [len(x) for x in lista]
soma = lambda a, b: a+b
sub = lambda a, b: a-b
    
print(contador_letras(lista))
print(soma(5,10))
print( sub(10,9))

calculadora = {
    "soma": lambda a, b: a+b,
    'subtracao': lambda a, b: a-b,
    "divisao": lambda a, b: a/b,
    "multiplicação": lambda a, b: a*b,
}
type(calculadora)


soma = calculadora['soma']
multiplicação = calculadora["multiplicação"]
divisão = calculadora["divisao"]
subtração = calculadora["subtracao"]

print("a soma é: {}".format(soma(45,54)))
print("a multiplicação é: {}".format(multiplicação(10, 2)))
