# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 00:39:29 2021

@author: vini
"""
#no cmd, foi requisitado pip install requests para baixar o pacote no computador
#depois, se verificou a função pip freeze que deus todos os status do pip baixado

#sobre criar novos projetos, caso um projeto velho esteja numa versão diferente de VirtualEnv - virtual environment. è possível preparar as versões com o uso de virtualenv
import requests

def retorna_dados_cep(cep):
    response = requests.get("https://viacep.com.br/ws/{}/json/".format(cep))
    print(response.status_code)
    print(response.text)
    
    dados_cep = response.json()
    print(dados_cep['logradouro'])
    print(dados_cep['complemento'])
    return dados_cep

def retorna_dados_pokemon (pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    dados_pokemon = response.json()
    return dados_pokemon

def retorna_response(url):
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    response = retorna_response("https://globallabs.academy/")
    print(response)
    
    #retorna_dados_cep()
    #dados_pokemon = retorna_dados_pokemon('pikachu')
    #print(dados_pokemon)
