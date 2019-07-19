# Faça um programa que leia o raio de um círculo e faça duas
# funções: uma que calcule a área do círculo e outra que calcule
# o comprimento do círculo.

raio_circulo =  float(input('qual o raio do circulo '))
pi = 3.14

def area(raio_circulo,pi):
    area_circulo = (pi * (raio_circulo ** 2))
    print('a sua área é {}m²'.format(area_circulo))

area(raio_circulo,pi)

def comprimento_circulo(pi,raio_circulo):
    comprimento = 2 * pi * raio_circulo

    print('Seu comprimento é {}'.format(comprimento))

comprimento_circulo(pi, raio_circulo)