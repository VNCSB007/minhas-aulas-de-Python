a=float(input("digite um numero qualquer: "))
b = float(input("agora escolha outro: "))

soma = a+b
subtracao = a-b
multiplicacao = a*b
divisao = a/b
resto = a%b

print("\n\n\n\n\nO valor de 'a' é {} e o valor de 'b' é {}. Portanto:\n\nSoma: {}\nSubtracao (a - b): {}\nMultiplicacao: {}\nDivisao (a/b): {}\nResto: {}\n".format(a, b, soma, subtracao, multiplicacao, divisao, resto))
print("Importante lembrar que alguns números podem ser do tipo {} enquanto que outros são do tipo {}\n".format(type(1), type(1.1)))


x = "1"
soma2 = int(x) + 1
print(soma2, " - caso seja definido uma string para integer, o python sabera o que fazer")

"""
x = "1"
soma2 = int(x) + 1
print(soma2)
agora qualquer coisa que eu escrever o python considera como um comentário
"""

