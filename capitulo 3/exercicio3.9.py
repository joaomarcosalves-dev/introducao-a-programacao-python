#Escreva um progama que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.

dias = int(input('Digite a quantidade de dias: '))
horas = float(input('Digite a quantidade de horas'))
minutos = float(input('Digite a quantidade de minutos: '))
segundos = int(input('Digite a quantidade de segundos: '))

tot_segundos = dias * 24 * 3600 + horas * 3600 + minutos * 60 + segundos
print(f"Convertido em segundos é igual a {tot_segundos} segundos")
