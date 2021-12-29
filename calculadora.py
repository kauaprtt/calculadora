import math
print('Olá isso é uma calculadora rapida')
num = float(input('Digite o numero: '))
val = float(input('Digite o seu mutiplicador: '))

r = num * val
ra = math.sqrt(num)
exp = num ** num


print('R: {:.2f}'.format(r))
print('Raiz: {:.2f}'.format(ra))
print('Exponencia: {:.2f}'.format(exp))