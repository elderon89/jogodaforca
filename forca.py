import random

def print_abertura():
    print("---------- Bem vindo(a) ao Jogo da Forca! ----------")

def cria_palavra():
    palavras = []
    with open("palavras.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_corretas(palavra):
    return ["_" for letra in palavra]

def pede_chute():
    chute = input("Diga uma letra: ")
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(chute, letras_corretas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_corretas[index] = letra
        index += 1

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("Que pena, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def print_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def novamente():
    # Take input from user
        jogar_dnv = input('''
Você deseja calcular novamente?
Favor digitar S para SIM ou N para NÃO.
''')

    # If user types Y, run the calculate() function
        if jogar_dnv == 'S':
            jogo()

    # If user types N, say good-bye to the user and end the program
        elif jogar_dnv == 'N':
            print('Até mais!')

    # If user types another key, run the function again
        else:
            novamente()

def jogo():

    print_abertura()

    palavra_secreta = cria_palavra()

    letras_corretas = inicializa_letras_corretas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0
    letras_faltando = len(letras_corretas)

    print(letras_corretas)
    while (not acertou and not enforcou):

        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_corretas, palavra_secreta)
            letras_faltando = str(letras_corretas.count('_'))
            if (letras_faltando == "0"):
                print("PARABÉNS!! Você encontrou todas as letras formando a palavra '{}'".format(palavra_secreta.upper()))
        else:
            erros += 1
            print(letras_corretas)
            print('Ainda faltam acertar {} letras'.format(letras_faltando))
            print('Você ainda tem {} tentativas'.format(7-erros))
            print_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_corretas

        print(letras_corretas)

    if (acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

    print("Fim do jogo")
    novamente()

if(__name__ == '__main__'):
    jogo()
