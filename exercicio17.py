#Leia quatro números em uma tupla e exiba: 
#a tupla original
#uma lista ordenada apenas para visualização
#o tipo da variável ordenada
#Objetivo: mostrar diferença entre tupla e lista sem precisar modificar nada.Use: sorted(), print(), type()

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
n4 = int(input("Digite o quarto número: "))

numeros = (n1, n2, n3, n4)

print("Tupla original:", numeros)

ordenada = sorted(numeros)

print("Lista ordenada:", ordenada)

print("Tipo da variável ordenada:", type(ordenada))
