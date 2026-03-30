#Leia três notas (float) em uma lista. Calcule a média. Substitua a menor nota por uma nova informada. Ordene a lista e mostre a nova média.
#Use: float(), input(), min(), list.index(), atribuição por índice, sort(), sum(), len(), print()

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

notas = [nota1, nota2, nota3]

media_inicial = sum(notas) / len(notas)
print("Média inicial:", media_inicial)

menor_nota = min(notas)
indice_menor = notas.index(menor_nota)

nova_nota = float(input("Digite a nova nota: "))
notas[indice_menor] = nova_nota

notas.sort()

nova_media = sum(notas) / len(notas)

print("Notas ordenadas:", notas)
print("Nova média:", nova_media)
