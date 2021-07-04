# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 22:54:33 2021

@author: vini
"""

#docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior

from datetime import date, time, datetime, timedelta
#datetime fornecce o horario e o dia em que foi executado a função datetime.now()
#timedelta é ótimo para verificar a difernça de dias, quanto tempo falta para um evento como pagamento ou deadline (leva em consideração o ano bissexto)

#data_atual = date.today()
#print(data_atual.strftime("%d/%m/%y"))
#print(data_atual.strftime("%d-%m-%Y"))
#print(data_atual.strftime("%d/%B/%y - %A"))

#type(data_atual)
#caso se coloque o 'data_atual' dentro de uma variável, ela se torna uma str

def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime("%d/%m/%y"))
    tupla = ('segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabado', "dommingo")
    print(tupla[data_atual.weekday()])
    data_criada = datetime(2021, 2, 5, 8, 50, 44)
    print(data_criada.strftime("%c"))
    data_string = "01/01/2021"
    data_convertida = datetime.strptime(data_string, "%d/%m/%Y")
    print(data_convertida)
    print(data_convertida.year)
    nova_data = data_convertida - timedelta(days = 365)
    print(nova_data)









def trabalhando_com_date():
    data_atual = date.today()
    data_atual_str = data_atual.strftime("%A %B %Y")
    print(type(data_atual))
    print(data_atual_str)
    print(type(data_atual_str))
    


def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    horario_str = horario.strftime("%H:%M:%S")
    print(type(horario_str))


if __name__ == '__main__':
    #trabalhando_com_date()
    #trabalhando_com_time()
    trabalhando_com_datetime()
    
    
data_viagem = datetime.now() - timedelta(days=1)
print(datetime.now().weekday()) #retornou 0
print(data_viagem)

