# Programa que simula um dado de n lados
contador = True
while contador:
    from random import randint
    lado = input("Quantos lados tem o dado? ")
    if lado == 'x':
        contador = False
    else:
        x = randint(1,int(lado))
        print(f'Número sorteado {x}')
