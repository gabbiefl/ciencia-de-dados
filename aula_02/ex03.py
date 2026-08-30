# 03) Leia um número inteiro e verifique: se ele é múltiplo de 3; se é múltiplo de 5; se é múltiplo de 3 e 5 ao mesmo tempo

num = int(input("Digite um número inteiro: "))


if num % 5 == 0 and num % 3 == 0:
    print(f"{num} é múltiplo de 3 e 5")
elif num % 5 == 0:
      print(f"{num} é múltiplo de 5")
elif num % 3 == 0:
      print(f"{num} é múltiplo de 3")
else:
      print(f"{num} não é múltiplo de 3 e nem de 5")