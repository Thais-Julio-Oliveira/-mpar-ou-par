número_inteiro = input ('Informe um número inteiro ')

if número_inteiro.isdigit():
    número_inteiro = int(número_inteiro)

    if número_inteiro % 2 == 0:
        print(f'{número_inteiro} é par')
    else:

        print(f'{número_inteiro} é ímpar')

else:
    print('Isso não é um número inteiro.')



