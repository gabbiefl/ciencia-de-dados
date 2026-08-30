"""
04)

● Conte quantas vezes o número 3 aparece
● Crie uma lista sem duplicados (usando set)
● Compare os tamanhos antes e depois
"""

valores = [1, 2, 2, 3, 3, 3, 4]

quantidade_tres = valores.count(3)

valores_unicos = list(set(valores))

tamanho_antes = len(valores)
tamanho_depois = len(valores_unicos)