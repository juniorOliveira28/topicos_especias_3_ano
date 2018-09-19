""" 14 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês,
sabendo-se que são descontados 7.5% para o Imposto de Renda, 8% para o INSS e 1% para o sindicato.
Faça um programa que nos dê:
salário bruto.
quanto pagou de imposto de renda (calcule sobre o salário bruto).
quanto pagou ao INSS (calcule sobre o salário bruto).
quanto pagou ao sindicato (calcule sobre o salário bruto).
o salário líquido (o que sobrou após os descontos).
+ Salário Bruto: R$
- IR (7.5%): R$
- INSS (8%): R$
- Sindicato (1%): R$
= Salário Líquido: R$
Obs.: apresente os descontos e o salário líquido, conforme o esquema acima.
"""

vh = float (input("Valor Hora: "))
ht = float(input("Horas trabalhadas no mês:"))

sB = vh * ht
print("Salário Bruto = {}".format(sB))

iR = (sB * 7.5) / 100
print("Imposto de Renda {}".format(iR))

inss = (sB * 8) / 100
print("Inss:{}".format(inss))

sindicato = (sB * 1) / 100
print("Sindicato:{}".format(sindicato))

sL = sB - iR - inss - sindicato

print("Salário Liquido = {}".format(sL))
