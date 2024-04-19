from random import randint

random = randint(0, 10)
print('qual numero de 0 a 10 eu estou pensano???')
player = int(input('de o seu palpite: '))
tentativas = 1
while player != random:
    if player < random:
        player = int(input('MAIS... tente novamente: '))
    else:
        player = int(input('MENOS... tente novamente:'))
    tentativas += 1
if player == random:
    print('\033[32mPARABENS\033[m vc acertou com {} tentativas'.format(tentativas))
print('eu estava pensando no numero {}'.format(random))
