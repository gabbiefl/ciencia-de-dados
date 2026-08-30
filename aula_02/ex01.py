# 01) Leia um número inteiro digitado pelo usuário e informe se ele é: positivo, negativo ou zero

num = int(input("Digite um número inteiro: "))

if num > 0:
  print(f"{num} é positivo")
elif num < 0:
    print(f"{num} é negativo")
else:
    print(f"{num} é igual a zero")