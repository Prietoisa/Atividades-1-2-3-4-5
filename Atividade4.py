# 4 - Crie uma função python que cálcule uma função de 2º Grau

#   Delta = B² - 4AC
#   Bhāskara = -B +- (raiz de delta)/ 2A

a = int (input ('Digite o valor de a'))
b = int (input ('Digite o valor de b'))
c = int (input ('Digite o valor de c'))

delta = (b*b)-(4 *(a *c))

print (delta)

if (delta >=0):
    x = ( (-b)+(delta **(1/2)) )/ (2*a)
    y = ( (-b)-(delta **(1/2)) )/ (2*a)

    print (f'O valor do X1 é {x} e o valor de X2 é {y}')

else:
    print('Não foi possível calcular pois delta é menor que 0')

x = ( (-b)+(delta **(1/2)) )/ (2*a)
y = ( (-b)-(delta **(1/2)) )/ (2*a)



