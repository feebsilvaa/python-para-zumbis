# 5) Solicite o preço de uma mercadoria e o
# percentual de desconto. Exiba o valor do desconto e o
# preço a pagar.


print('Calculo de percentual de desconto')

preco = float(input('Informe o preco da mercadoria: '))
pct_desconto = float(input('Informe a porcentagem do desconto (Ex: 10% = 10): '))

valor_desconto = preco * (pct_desconto / 100)

preco_final = preco - valor_desconto

print('O valor de desconto é: ', valor_desconto)
print('O preço final é: ', preco_final)
