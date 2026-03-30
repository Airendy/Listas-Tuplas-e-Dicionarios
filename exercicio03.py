#Crie uma lista com três inteiros. Atualize o último elemento para a soma dos dois primeiros. Exiba a lista.
#Use: int(), input(), indexação lista[i], print()

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

lista = [n1, n2, n3]

lista[2] = lista[0] + lista[1]

print(lista)
