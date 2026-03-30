#Leia quatro números inteiros, coloque em uma tupla e exiba o maior e o menor.
#funções: max(), min()
#tipos: int, tuple
#conceito: operações básicas de agregação

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
n4 = int(input("Digite o quarto número: "))

numeros = (n1, n2, n3, n4)

print("Maior número:", max(numeros))
print("Menor número:", min(numeros))
