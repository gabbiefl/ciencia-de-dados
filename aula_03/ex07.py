"""
07)

Crie um dicionário com 3 produtos e seus preços. Depois:
- Adicione um novo produto
- Atualize o preço de um produto
- Remova um produto
- Consulte o preço de um item
"""

produtos = {
    "arroz": 25.90,
    "massa": 8.50,
    "cafe": 14.00
}

# adicionando produto
produtos["acucar"] = 5.90
print(produtos)

# atualizando preço
produtos["massa"] = 9.40

# removendo produto
del produtos["arroz"]

print(produtos)

# consultando preço
print(produtos["cafe"])

