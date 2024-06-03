from math import sqrt, floor     # importar biblioteca de matemática
num = int(input('Digite um número: '))
raiz = sqrt(num)
###print('A raiz de {}, é igual há {}'.format(num, math.ceil(raiz))) #arredondando para cima
print('A raiz de {}, é igual há {:.2f}'.format(num, floor(raiz)))  

