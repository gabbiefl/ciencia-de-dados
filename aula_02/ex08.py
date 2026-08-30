# 08) Leia um número inteiro e mostre sua tabuada de 1 a 10 utilizando for.

num = int(input(f"Digite um número "))

for i in range(1, 11):
  operacao = num * i

  print(f"{num} * {i} = {operacao}")
