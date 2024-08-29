from random import randint

print("""DIGITE UMA OPÇÃO:          
[1] PAR
[2] IMPAR""")

opc = int(input('ESCOLHA UMA: '))

n = int(input('Digite um numero de 0 a 10: '))

computador = randint(0, 10)

print(f'O Jogador escolheu {n} e a Maquina escolheu {pc} a soma é {n+computador} ')

if opc == 1:
    if (n + computador) % 2 == 0:
        print('O jogador GANHOU!')
    else:
        print('A maquina GANHOU!')
if opc == 2:
    if (n + computador) % 2 == 0:
        print('A maquina GANHOU!')
    else:
        print('O jogador GANHOU')
