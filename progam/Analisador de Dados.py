print('{:=^30}'.format(' ANALISADOR DE DADOS '))

#masculino
nomeIdadeM = []
#feminino
nomeIdadeF = []
#todos
media = 0

#variaveis, loop para pegar nomes
for pessoas in range(1, 5):
    nome = str(input('qual é o nome da {}ª pessoa? '.format(pessoas))).strip()
    idade = int(input('qual é a idade dessa pessoa? '))
    print('''--------------------------------
[1]Masculino
[2]Feminino''')
    sexo = int(input('qual é o sexo BIOLOGICO da pessoa? '))
    print('-'*36)
    if sexo == 1:
        nomeIdadeM.append((nome, idade))
    else:
        nomeIdadeF.append((nome, idade))
    media = media + idade
print('a média de idade do grupo é {:.0f}'.format(media / 4))

#é para pegar o nome do homem mais velho!
nomeMaisVelho = None
idadeMaisVelho = 0

for nome, idade in nomeIdadeM:
    if idade > idadeMaisVelho:
        nomeMaisVelho = nome
        idadeMaisVelho = idade
print('o mais velho dos homens tem {} anos e se chama {}'.format(idadeMaisVelho, nomeMaisVelho))
#-------------------------------------
acumulador = 0
for nome, idade in nomeIdadeF:
    if idade < 20:
        acumulador += 1
print('tem {} mulheres com menos do que 20 anos'.format(acumulador))
