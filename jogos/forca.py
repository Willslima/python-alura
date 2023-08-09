def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "ovo".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    # for letra in palavra_secreta:
    #         letras_acertadas.append('_')

    while(not enforcou and not acertou):

        chute = input("Qual é a palavra? {} ".format(letras_acertadas))
        chute = chute.strip(' ').upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        enforcou = erros == len(palavra_secreta)
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
        
    if acertou:
        print("Você ganhou!! ")
    else:
        print("Você perdeu!!")
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
