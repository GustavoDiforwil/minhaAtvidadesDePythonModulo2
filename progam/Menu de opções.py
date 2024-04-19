from time import sleep

# começo
numeroUm = float(input('escolha um numero: '))
numeroDois = float(input('outro numero: '))
escolha = 0
while escolha != 5:

    print('''ESCOLHA UMAS DAS OÇÕES:
------------------------
\033[36m[1]Somar \033[m
\033[35m[2]Multiplicar \033[m
\033[33m[3]Maior\033[m
\033[94m[4]Novos numeros\033[m
\033[31m[5]sair do progrma\033[m''')
    escolha = int(input('escolha uma opção: '))

    # soma os numeros
    if escolha == 1:
        soma = numeroUm + numeroDois
        print('A soma entre eles é: \033[4;36m{}\033[m'.format(soma))

    # multiplicar os numeros
    if escolha == 2:
        multiplicacao = numeroUm * numeroDois
        print('A multiplicação entre esses dois numero({} e {}) fica: \033[35m{}\033[m'
              .format(numeroUm, numeroDois, multiplicacao))

    # qual é o maior numero
    if escolha == 3:
        if numeroUm > numeroDois:
            print('O numero \033[32m{}\033[m é maior que o numero \033[31m{}\033[m.'.format(numeroUm, numeroDois))
        elif numeroDois > numeroUm:
            print('O numero \033[32m{}\033[m é maior que o numero \033[31m{}\033[m.'.format(numeroDois, numeroUm))
        else:
            print('\033[33mOs numeros são iguais\033[m')

    # escolher novos numeros
    if escolha == 4:
        print('-' * 24)
        print('\033[94mescolha de NOVOS numeros:\033[m')
        numeroUm = float(input('escolha outro numero: '))
        numeroDois = float(input('escolha outro numero: '))
        print('\033[94mNUMEROS NOVOS ALOCADOS:\033[m')

    # separação pra ficar mais bonito e visivel.
    sleep(1)
    print('-' * 24)

    # sair do programa
print('\033[97;102mobrigado por usar meu programa!\033[m :)')
