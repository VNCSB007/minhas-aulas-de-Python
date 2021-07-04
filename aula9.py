# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 21:06:51 2021

@author: vini
"""

con

def escrever_arquivo(nome_arquivo, texto):
    diretorio = "C:/Users/vinic/OneDrive/Desktop/Python/Trabalhos do curso da DIO/"
    arquivo = open(diretorio + nome_arquivo, "w")
    arquivo.write(texto)
    arquivo.close()
    
def atualizar_arquivo(nome_arquivo, texto):
    diretorio = "C:/Users/vinic/OneDrive/Desktop/Python/Trabalhos do curso da DIO/"
    arquivo = open(diretorio + nome_arquivo, "a")
    arquivo.write(texto)
    arquivo.close()
    
def ler_arquivo(nome_arquivo):
    diretorio = "C:/Users/vinic/OneDrive/Desktop/Python/Trabalhos do curso da DIO/"
    arquivo = open(diretorio + nome_arquivo, "r")
    texto = arquivo.read()
    print(texto)
    
def media_notas(nome_arquivo):
    diretorio = "C:/Users/vinic/OneDrive/Desktop/Python/Trabalhos do curso da DIO/"
    aquivo = open(diretorio + nome_arquivo, "r")
    aluno_nota = aquivo.read()
    #print(aluno_nota)
    aluno_nota = aluno_nota.split("\n")
    lista_media = []
    #print(aluno_nota)
    for x in aluno_nota:
        lista_notas = x.split(",")
        aluno = lista_notas[0]
        lista_notas.pop(0)
        media = lambda notas: sum(float(i) for i in notas)/4
        print(aluno)
        print(media(lista_notas))
        print(lista_notas)
        lista_media.append({aluno:media(lista_notas)})
    return lista_media
    
if __name__ == '__main__':
    media_notas('notas.md')
    #escrever_arquivo("primeira linha. \n")
    #aluno = "cesar: 7, 9 , 3 , 5\n"
    #atualizar_arquivo("terceira linha. \n")
    #ler_arquivo("teste.md)


#escrever_arquivo("notas.md", "# NOTAS DO COLEGIO")
#atualizar_arquivo("notas.md", "\nbruno: 5, 6.5, 7, 2\nLeticia:4,4,5,7.5\njunior:7,7,7,7")
