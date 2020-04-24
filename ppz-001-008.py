# 8) Converta uma temperatura digitada em Fahrenheit para Celsius. 

print('Conversao de Fahrenheit para Celsius')

fahrenheit = float(input('Informe a temperatura em fahrenheit (ºF): '))

celsius = (fahrenheit - 32) * 5 / 9

print(f'{fahrenheit} ºF correspondem a {celsius} ºC')
