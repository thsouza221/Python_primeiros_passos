money = float(input('Digite o valor do dinheiro: '))
n100 = money//100
print('NOTAS:')
print('%.0f nota(s) de R$ 100.00' %(n100))
montante = money % 100
n50 = montante//50
print('%.0f nota(s) de R$50.00' %(n50))
montante = montante % 50
n20 = montante//20
print('%.0f nota(s) de R$20.00' %(n20))
montante = montante % 20
n10 = montante//10
print('%.0f nota(s) de R$10.00' %(n10))
montante = montante % 10
n5 = montante//5
print('%.0f nota(s) de R$5.00' %(n5))
montante = montante % 5
n2 = montante//2
print('%.0f nota(s) de R$2.00' %(n2))
print('MOEDAS:')
montante = (montante % 2)*100
n1 = montante//100
print('%.0f moedas(s) de R$1.00' %(n1))
montante = montante % 100
n05 = montante//50
print('%.0f moedas(s) de R$0.50' %(n05))
montante = montante % 50
n025 = montante//25
print('%.0f moedas(s) de R$0.25' %(n025))
montante = montante % 25
n010 = montante//10
print('%.0f moedas(s) de R$0.10' %(n010))
montante = montante % 10
n005 = montante//5
print('%.0f moedas(s) de R$0.05' %(n005))
n001= montante % 5
print('%.0f moedas(s) de R$0.01' %(n001))