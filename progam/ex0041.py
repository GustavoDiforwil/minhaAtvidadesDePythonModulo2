#biblioteca para pegar data em tempo real
from datetime import date
anoAtual = date.today().year
#apresenta o programa/diz oq ele faz
print('-=-' * 12)
print('em que categoria você ira competir?')
print('-=-' * 12)
#variaveis/calculo de idade
nascimento = int(input('Ano de nascimento: '))
idade = anoAtual - nascimento
#mostra sua idade
print('voce tem {} anos'.format(idade))
#se
if idade >= 1 and idade <= 9:
    print('Você comepete na categoria MIRIM')
elif idade > 9 and idade <= 14:
    print('voce compete na categoria INFANTIL')
elif idade > 14 and idade <= 19:
    print('você compete na categoria JUNIOR')
elif idade > 19 and idade <= 25:
    print('você compete na categoria SENIOR')
elif idade > 25:
    print('você compete na categoria MASTER')