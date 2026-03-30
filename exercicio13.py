#Leia quatro números inteiros e crie uma tupla. Depois leia um número e diga quantas vezes ele aparece na tupla.
#método: tuple.count()
#tipos: int, tuple

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
n4 = int(input("Digite o quarto número: "))

numeros = (n1, n2, n3, n4)

valor = int(input("Digite um número para contar: "))

quantidade = numeros.count(valor)

print("O número aparece", quantidade, "vez(es) na tupla.")
