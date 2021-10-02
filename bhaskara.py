# Programa que calcula a fórmula de Bhaskara
# Inputs:
a = float(input('Digite o valor de a'))
b = float(input('Digite o valor de b'))
c = float(input('Digite o valor de c'))
# Função:
def bhaskara(a,b,c):
    delta = (b*b)-(4*a*c)
    x1 = (-b + (delta**0.5))/(2*a)
    x2 = (-b - (delta**0.5))/(2*a)
    # Resultados
    return f'X1= {x1} ; X2= {x2}'
#Fim da Função
print(bhaskara(a,b,c))