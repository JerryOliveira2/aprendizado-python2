# Faça um programa que peça ao usuário para digitar um número inteiro,
# informe se este número é par ou ímpar. Caso o usuário não digite um número
# inteiro, informe que não é um número inteiro.
#
try:
    numero_inteiro = int(input('Digite um numero Inteiro:'))
    if numero_inteiro % 2 == 0:
        print('O numero é par!')
    else:
        print('O número dígitado é Ímpar!')
except ValueError:
    print('Erro: Valores Digitados não condizem com um número inteiro.')
