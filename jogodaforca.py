#jogo-da-forca
print("*********************************")
print("Bem vindo ao jogo da forca")
print("*********************************")

palavrasecreta = "forte"
palavrasacertadas = ("_","_","_","_","_","_",)

enforcou = falso
acertou = falso

while(not enforcou and not acertou):
    chute = input("Digite uma letra")
    chute = chute.strip()

    index = 0
    for letra in pallavrasecreta:
        if(chute.upper() == letra.upper())
        print("encontrei a letra {} na posição{}".format(letra,index))
        index = index + 1

        t("jogando")

        im do jogo