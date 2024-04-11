'''retaUm'''
a = float(input('Primeiro segmento: '))
'''retaDois'''
b = float(input('segundo segmento: '))
'''retaTres'''
c = float(input('terceiro segmento: '))

if a + b > c and b + c > a and c + a > b:
    print('ele é um triangulo', end=' ')
    if a == b and b == c:
        print('EQUILÁTERO')
    elif a == b or b == c or a == c:
        print('ISÓCELES')
    else:
        print('ESCALENO')
else:
    print('ele não é um triangulo')
