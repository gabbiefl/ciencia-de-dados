# 09) Peça ao usuário para digitar números. O programa deve continuar pedindo números até que o usuário digite 0. Ao final, mostre:quantos números foram digitados; a soma total deles
numeros = []
num = -1

while num != 0:
  num = int(input(f"Digite o {i} número ou 0 para sair: "))

  if num != 0:
      numeros.append(num)

print(f"quantidade de números digitados: {len(numeros)}")
print(f"a soma total deles é: {sum(numeros)}")