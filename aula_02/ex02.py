# 02) Leia dois números inteiros e mostre qual deles é o maior. Caso sejam iguais, informe isso ao usuário.

num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite mais um número inteiro: "))

if num1 > num2:
    print(f"{num1} é maior do que {num2}")
elif num1 == num2:
    print(f"{num1} e {num2} são iguais")
else:
      print(f"{num2} é maior do que {num1}")
