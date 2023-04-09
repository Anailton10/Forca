from random import choice
from colorama import Fore

palavras = ['amor', 'vida', 'cachorro', 'computador', 'controle', 'caixa']
palavra = str(choice(palavras)).upper()
letras_tentadas = list()
palavra_certa = list('-') * len(palavra)
tentativa = 0
chance = 0
print('JOGO DA FORCA')
print('''NIVEIS DE DIFICULDADE
[ 1 ] FÀCIL
[ 2 ] MÈDIO
[ 3 ] DIFICIL''')
while True:
    try:
        nivel = int(input('ESCOLHA O NIVEL DE DIFICULDADE:'))
        if nivel == 1:
            chance = 8
        elif nivel == 2:
            chance = 6
        elif nivel == 3:
            chance = 4
        break
    except:
        print(Fore.RED + 'OPÇÃO INVÁLIDA!!')
        print('Digite apenas numeros de 1 a 3.' + Fore.RESET)

while tentativa < chance and ''.join(palavra_certa) != palavra:
    print(f'\nA PALAVRA TEM {len(palavra)} LETRAS')
    print(f'\nDESCUBRA A PALAVRA PARA GANHAR O JOGO, VOCÊ TERÀ {chance - tentativa} TENTATIVAS')

    letra = str(input('Informe a letra: ')).upper()
    if letra.isnumeric():
        print('INFORME APENAS LETRAS')
    while letra in letras_tentadas:
        print(Fore.RED + 'VOCÊ JÀ DIGITOU ESSA LETRA...' + Fore.RESET)
        print('DIGITE NOVAMENTE...')
        letra = str(input('Informe a letra: ')).upper()
        if letra.isnumeric():
            print('INFORME APENAS LETRAS')
    letras_tentadas.append(letra)

    if letra in palavra:
        print(Fore.GREEN + 'Acertou' + Fore.RESET)
        for l in range(len(palavra)):
            if letra == palavra[l]:
                palavra_certa[l] = letra
    else:
        print(Fore.RED + 'Errou' + Fore.RESET)
        tentativa += 1
    print(Fore.BLUE + '\nESTADO ATUAL...' + Fore.RESET)
    for x in palavra_certa:
        print(Fore.YELLOW + f'{x}', end=' ' + Fore.RESET)
    print(Fore.BLUE + '\nLETRAS TENTADAS...' + Fore.RESET)
    for x in letras_tentadas:
        print(Fore.YELLOW + f'{x}', end=' ' + Fore.RESET)

if tentativa == chance:
    print('\nVOCÊ PERDEU...')
    print(f'\nA PALAVRA ERA {palavra}')
else:
    print(Fore.GREEN + '\nPARABÈNS VOCÊ GANHOU!!' + Fore.RESET)
