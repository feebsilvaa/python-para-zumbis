# 7) Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C/5 + 32

print('Conversao de Celsius para Fahrenheit')

celsius = float(input('Informe a temperatura em celsius (ºC): '))

fahrenheit = celsius * 9 / 5 + 32

print(f'{celsius} ºC correspondem a {fahrenheit} ºF')
