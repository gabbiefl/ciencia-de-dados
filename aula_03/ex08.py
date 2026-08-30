"""
08)

Dado:
alunos = {
"Ana": 8.5,
"João": 7.0,
"Maria": 9.0
}
● Imprima nome e nota de cada aluno
● Calcule a média da turma
"""

alunos = {
  "Ana": 8.5,
  "João": 7.0,
  "Maria": 9.0
}

notas = []

for nome, nota in alunos.items():
  print(f"Nome: {nome} | Nota: {nota}")
  notas.append(nota)

media_turma = sum(notas) / len(notas)
print(f"Média da turma: {media_turma:.2f}")