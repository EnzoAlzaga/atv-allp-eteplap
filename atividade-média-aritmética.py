#PRIMEIRA NOTA.

while True:
    nota1 = float(input("Digite a primeira nota (0 a 10): "))
    if 0 <= nota1 <= 10:
        break 
else: print("Nota Inválida. Digite um valor de 0 a 10.")

#SEGUNDA NOTA.

while True:
    nota2 = float(input("Digite a segunda nota (0 a 10): "))
    if 0 <= nota2 <= 10:
        break
else: print("Nota Inválida. Digite um valor de 0 a 10.")

#CÁLCULO DA MÉDIA.

media = (nota1 + nota2) / 2
print("Média é:", media)

#VIZUALIZAÇÃO DA MÉDIA E RESOLUÇÃO.

if media >= 6:
    print("Aluno aprovado. Parabéns!")
else:
    print("Aluno reprovado. Estude mais.")
