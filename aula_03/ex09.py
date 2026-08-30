"""
09)

Crie uma função

def media(lista):
Que:

● Recebe uma lista de números
● Retorna a média
● Teste com diferentes listas
"""
def media(lista):

  soma = 0
  total = 0

  for num in lista:
    soma += num
    total += 1

  media = soma / total

  return media

print(media([5, 7, 8]))
print(media([8, 9, 10]))
print(media([10, 10, 10]))
