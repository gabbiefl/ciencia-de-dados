# 04) Peça ao usuário que informe sua idade e classifique: criança (0–12); adolescente (13–17); adulto (18–59); idoso (60 ou mais)

idade = int(input("Digite a sua idade:"))

if idade <= 12:
    print("Você é criança")
elif idade >= 13 and idade <= 17:
    print("Você é adolescente")
elif idade >= 18 and idade <= 59:
      print("Você é adulto")
else:
      print("Você é idoso")
