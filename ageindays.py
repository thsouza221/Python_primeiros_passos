# Programa que calcula idade
# Inputs:
idade = int(input('Digite sua idade em dias'))
# Função:
ano = idade/365
resto1 = idade % 365
print('%.0f ano(s)' %(ano))
if resto1 != 0:
    mes = resto1 / 30
    dia = resto1 % 30
    print('%.0f mes(es)' %(mes))
    if dia != 0:
        print(f'{dia} dia(s)')
