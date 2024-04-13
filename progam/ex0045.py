from random import choice
print('{:=^40}'.format(' \033[36mJOKENPO\033[m '))
usuario = str(input('Escolha sua jogada: ')).lower().strip()
lista = ['pedra', 'tesoura', 'papel']
computador = choice(lista)

#mostrando o ganhador
print('o computador escolheu {}'.format(computador))

#caso o usuario escolha papel
if computador == 'pedra' and usuario == 'papel':
    print('você \033[32mGANHOU\033[m! papel \033[32mganha\033[m de pedra')
elif computador == 'tesoura' and usuario == 'papel':
    print('você \033[31mPERDEU\033[m! papel \033[31mperde\033[m para tesoura.')
elif computador == 'papel' and usuario == 'papel':
    print('deu \033[33mEMPATE\033[m!')

#caso o usuario escolha tesoura
elif computador == 'papel' and usuario == 'tesoura':
    print('você \033[32mGANHOU\033[m! tesoura ganha de papel')
elif computador == 'pedra' and usuario == 'tesoura':
    print('você \033[31mPERDEU\033[m! tesoura perde para pedra')
elif computador == 'tesoura' and usuario == 'tesoura':
    print('deu \033[33mEMPATE!\033[m')

#caso o usuario escolha pedra
elif computador == 'tesoura' and usuario == 'pedra':
    print('você \033[32mGANHOU\033[m! pedra ganha de tesoura')
elif computador == 'papel' and usuario == 'pedra':
    print('você \033[31mPERDEU\033[m! pedra perde para papel')
elif computador == 'pedra' and usuario == ('pedra'):
    print('deu \033[33mEMPATE\033[m!')
else:
    print('você deu uma resposta \033[31mINVALIDA\033[m!')
#fim do programa.