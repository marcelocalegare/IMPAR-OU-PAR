from random import randint

print('=-'*20)
print("""DIGITE UMA OPÇÃO:          
[1] IMPAR
[2] PAR""")

opc = int(input('\nQUAL SUA ESCOLHA? '))

n = int(input('Digite um numero de 0 a 10: '))

computador = randint(0, 10)
print('=-'*20)
print(f'O Jogador escolheu {n} e a Maquina escolheu {computador}!')
if (n + computador) % 2 == 0:
    print(f'A soma é {n+computador}, esse numero é PAR!')
else:
    print(f'A soma é {n+computador}, esse numero é IMPAR!')
if opc == 1:
    if (n + computador) % 2 == 1:
        print('O jogador GANHOU!')
    else:
        print('A maquina GANHOU!')
if opc == 2:
    if (n + computador) % 2 == 0:
        print('O jogador GANHOU')
    else:
        print('A maquina GANHOU!')
print('=-'*20)
