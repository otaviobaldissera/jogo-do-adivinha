from random import randint

# sortear um número de 1 a 10
sorteado = randint(1, 10)

# inicializar 3 vidas
vidas = 3

# começar um loop infinito
while True:
    #receber um palpite de usuário
    palpite = int(input('Digite um número: ')) 

    # se o palpite é igual ao sorteado, o usuário ganhou
    if palpite == sorteado:
        print("acertou!")
        break

    # se o palpite é menor, escrever mensagem
    if palpite < sorteado:
        print('Muito baixo')
    # se o palpite é maior, escrever mensagem
    elif palpite > sorteado:
        print('Muito alto')

    # se o usuário não acertou, descontar uma vida
    vidas -= 1 

    # se vidas é igual a zero, o usuário perdeu
    if vidas == 0:
        print('Você perdeu.')
        break
    