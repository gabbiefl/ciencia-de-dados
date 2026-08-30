"""
05)

● Converta para lista
● Adicione o valor 5
● Converta de volta para tupla
● Explique por que essa conversão é necessária
"""

tupla = (1,2,3,4)

print(tupla)

tupla = list(tupla)

print(tupla)

tupla.append(5)

print(tupla)

tupla = tuple(tupla)

print(tupla)

# nao é possivel adicionar valores a tuplas pois sao imutaveis, por esse motivo a conversao para lista é necessaria