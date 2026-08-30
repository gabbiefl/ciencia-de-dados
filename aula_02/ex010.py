"""
10)

Crie um programa em que:
● Um número secreto seja definido no código (por exemplo 7)
● O usuário tente adivinhar o número
● O programa informe:
  ○ "maior" se o palpite for maior que o número
  ○ "menor" se o palpite for menor
● O programa continua até o usuário acertar. """

num_secreto = 7

while num != num_secreto:
    num = int(input(f"Adivinhe um número: "))

    if num > num_secreto:
      print("O número secreto é menor!")
    elif num < num_secreto:
      print("O número secreto é maior!")
    else:
      print("Acertou!")

