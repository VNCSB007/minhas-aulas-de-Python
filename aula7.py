# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 11:33:44 2021

@author: vini
"""
""" Televisão
class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 1
        
    def power(self):
        if self.ligada:
            self.ligada =False
        else:
            self.ligada = True
    
    def aumenta_canal(self):
        self.canal += 1
        
    def diminui_canal(self):
        self.canal -= 1

tv = Televisao()
print("ligada: {}".format(tv.ligada))
tv.power()
print("ligada: {}".format(tv.ligada))
tv.aumenta_canal()
print("canal: {}".format(tv.canal))
tv.diminui_canal()
tv.diminui_canal()
print("canal: {}".format(tv.canal))
"""






"""calculadora 2
class Calculadora:
    #nessesse caso, o init é irrelevante para o funcionamento da class
    #def __init__(self):
    #    pass
    
    def soma(self, a, b):
        return "A função soma resulta em: {}".format(a+b)
    def sub(self, a, b):
        return "A função sub resulta em: {}".format(a-b)
    def vezes(self, a, b):
        return "A função vezes resulta em: {}".format(a*b)
    def divis(self, a, b):
        return "A função divis resulta em: {}".format(a/b)
x = Calculadora()

print(x.soma( 10,2))
print(x.sub( 10,2))
print(x.vezes( 10,2))
print(x.divis( 10,2))
"""


""" Criando a primeira calculadora
class Calculadora:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def soma(self):
        return "A função soma resulta em: {}".format(self.a+self.b)
    def sub(self):
        return "A função sub resulta em: {}".format(self.a-self.b)
    def vezes(self):
        return "A função vezes resulta em: {}".format(self.a*self.b)
    def divis(self):
        return "A função divis resulta em: {}".format(self.a/self.b)

calculadora = Calculadora(6, 2)
print(calculadora.soma())
"""