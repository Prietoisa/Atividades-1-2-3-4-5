# 2 - crie uma função que receba uma lista de 20 valores aleatórios, retornar
# apenas o maior valor e printar em tela.

import random 
V = random.randrange(0,20)
lista = []
contador = 0

while contador < 20:
    lista.append(random.randrange(0,100))
    contador +=1

print(lista)

valores = [0,20]

def valores_aleatorio(aleatorios):
    return print(max(aleatorios))

valores_aleatorio(lista)