'''Escreva um programa para aprovar o empréstimo bancário para
a compra de uma casa. Pergunte o valor da casa, o salário do comprador
e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário
ou então o empréstimo será negado.'''

casa = float(input('qual é o preço da casa? R$'))
salario = float(input('o seu salario é de quanto? R$'))
anos = int(input('em quantos anos vc quer pagar essa casa: '))

valorMensal = float(casa/(anos * 12))
porcentagem = salario * 0.30
print('para pagar uma casa de R${:.2f} em {} anos, a prestação ficara de  R${:.2f}'
      .format(casa, anos, valorMensal))
if valorMensal <= porcentagem:
    print('empréstimo pode ser \033[4;32mAPROVADO!\033[m')
else:
    print('empréstimo \033[4;31mNEGADO!\033[m')
