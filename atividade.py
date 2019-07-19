# 1 - Escreva um programa que leia o nome de um funcionário,
# seu número de horas trabalhadas, o valor que recebe por hora
# e calcula o salário desse funcionário.
# A seguir, mostre o nome e o salário do funcionário.


nome_funcionario = input ('Digite seu nome ')
Horas_trabalhadas =  int(input('quantas horas foram trabalhadas? '))
salário_por_hora = float(input('Valor por hora do seu salário '))

print(f'{nome_funcionario} seu salário é {Horas_trabalhadas*salário_por_hora}')