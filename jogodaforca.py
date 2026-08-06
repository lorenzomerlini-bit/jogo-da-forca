#jogo-da-forca
print("*********************************")
print("Bem vindo ao jogo da forca")
print("*********************************")

palavrasecreta = "forte"
palavrasacertadas = ("_","_","_","_","_","_",)

enforcou = falso
acertou = falso
tentativas = 0
while(not enforcou and not acertou):
    chute = input("Digite uma letra")
    chute = chute.strip()

    index = 0
    for letra in pallavrasecreta:
        if(chute.upper() == letra.upper())
          print("encontrei a letra {} na posição{}".format(letra,index))
        index = index + 1

        print("jogando")

        print("fim do jogo")

        else
        tentativas += 1

        # controle de tentativas
        enforcou = tentativas == total_tentativas
        acertou = "_" not in letrascartadas
        print("letrasacertadas: {}",format(letrasacertadas))
        print("tentativasrestantes: {}",format(total_tentativa - tentativa))

        if(acerto):
          print("parabens, voce ganhou!")
          elif(enforco):
            print("voce perdeu! A palavra era {}",format(palavrassecretas))

            print("fim do jogo")