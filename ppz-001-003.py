# Lista I de exercicios PPZ
# Programa III

# 3) Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule
# o total em segundos.


dias = int(input('informa a quantidade de dias: '))
horas = int(input('informa a quantidade de horas: '))
minutos = int(input('informa a quantidade de minutos: '))
segundos = int(input('informa a quantidade de segundos: '))

total_segundos = segundos + (minutos * 60) + (horas * 3600) + (dias * 86400)

print(f'{dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos correspondem a {total_segundos} segundos')
