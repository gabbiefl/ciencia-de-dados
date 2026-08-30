"""
06)

A = {1,2,3,4}
B = {3,4,5,6}

● Calcule união
● Interseção
● Diferença A - B

"""

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

uniao = A | B
print("União:", uniao)

intersecao = A & B
print("Interseção:", intersecao)


diferenca = A - B
print("Diferença (A - B):", diferenca)
