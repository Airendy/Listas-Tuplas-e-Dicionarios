#Leia três notas (float) e armazene em uma tupla. Exiba a tupla e a média das notas.
#Use: float(), sum(), len(), print()
#Sem alterar tupla.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

notas = (nota1, nota2, nota3)

media = sum(notas) / len(notas)

print("Notas:", notas)
print("Média:", media)
