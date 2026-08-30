# 07 Peça ao usuário que informe 5 números e calcule a soma total deles utilizando um laço for.

soma = 0

for i in range(1, 6):
  num = int(input(f"Digite o {i} número: "))
  soma = soma + num

print(f"{soma}")

