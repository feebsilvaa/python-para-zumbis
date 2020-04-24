# 6) Calcule o tempo de uma viagem de carro.
# Pergunte a distância a percorrer e a velocidade média
# esperada para a viagem.


print('Calculo de tempo de viagem')

distancia = float(input('Informe a distancia em km: '))
velocidade_media = float(input('Informe a velocidade media (km/h): '))

tempo_viagem = distancia / velocidade_media

print(f'O tempo aproximado da viagem sera de: {tempo_viagem} horas')
