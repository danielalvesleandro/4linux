
import banco

acertos = 0
tolerancia = 15

while acertos < 3:
    for usuario in banco.lista_de_usuarios:
        idade = usuario['idade']
        numero = input('Tente adivinhar a idade: ')
        numero = int(numero)
        if numero in range(idade - tolerancia, idade + tolerancia):
            acertos = acertos + 1
            print('Você já acertou: ' + str(acertos))
            if acertos == 3:
                break
print('Acertô miserávi!')

# input sempre é incialmente str para aceitar número e string
