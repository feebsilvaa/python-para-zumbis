# Faça um programa que calcule o aumento de um salário.
# Ele deve solicitar o valor do salário e a
# porcentagem do aumento. Exiba o valor do aumento e do novo salário.


print('Calculo de aumento de salario')

salario_atual = float(input('Informe o salario atual: '))
pct_aumento = float(input('Informe a porcentagem do aumento (Ex: 10% = 10): '))

valor_aumento = salario_atual * (pct_aumento / 100)

novo_salario = salario_atual + valor_aumento

print('O valor de aumento é: ', valor_aumento)
print('O novo salario é: ', novo_salario)
