# 05) Leia três notas e calcule a média. Classifique o estudante: média ≥ 7 → aprovado; média entre 5 e 7 → recuperação; média < 5 → reprovado

nota1 = float(input("Digite a sua primeira nota:"))
nota2 = float(input("Digite a sua segunda nota:"))
nota3 = float(input("Digite a sua terceira nota:"))

nota_final = (nota1 + nota2 + nota3) / 3

if nota_final >= 7:
      print("Aprovado")
elif nota_final >= 5 and nota_final < 7:
        print("Recuperação")
else:
        print("Reprovado")