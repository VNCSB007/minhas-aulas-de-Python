# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 16:57:59 2021

@author: vini
"""


""" Entendendo range
for x in range(90, 100):
    print(x)
"""

""" entendendo for, if e else (alem do +=) 
a = int(input("digite um numero: "))

div = 0
for x in range (1, a+1):
    resto = a % x
    print(x, resto, "\n")
    if resto == 0:
        div += 1
        
if div == 2:
    print("numero {} é primo".format(a))
else:
    print("número {} não é primo".format(a))
"""

""" bagui a mais
b = int(input("digite um valor: "))  

for a in range(b+1):
    div = 0
    for x in range (1, a+1):
        resto = a % x
        if resto == 0:
            div += 1
    if div == 2:
        print(a)
"""

""" criando um programa para análise de notas no final do ano
nota1 = float(input("entre com a nota: "))
while nota1 > 10 or nota1 < 0:
    nota1 =float(input("Primeira Nota inválida. digite um numero igual ou menor a 10: "))

nota2 = float(input("entre com a nota: "))
while nota2 > 10 or nota2 < 0:
    nota2 =float(input("Segunda Nota inválida. digite um numero igual ou menor a 10: "))

nota3 = float(input("entre com a nota: "))
while nota3 > 10 or nota3 < 0:
    nota3 =float(input("Terceira Nota inválida. digite um numero igual ou menor a 10: "))

media = (nota1+nota2+nota3)/3
if media >=6:
    print("\nAluno aprovado com {}".format(media))
else:
    print("\nFalta {} ponto/os\n".format(-media+6))
    x=-media+6
    if x<=0.5:
        print("o aluno em questão deverá ser julgado no conselho de classe")
    else:
        print("Reprovação")
"""

