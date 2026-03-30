#Leia quatro inteiros e crie uma lista. Leia um valor alvo e remova se ele estiver na lista. Mostre o tamanho antes e depois
#Use: int(), input(), in, remove(), len(), print()

a = int(input("Digite o 1º número: "))
b = int(input("Digite o 2º número: "))
c = int(input("Digite o 3º número: "))
d = int(input("Digite o 4º número: "))

lista = [a, b, c, d]

# Mostrar o tamanho antes
print("Tamanho antes:", len(lista))

# Ler o valor alvo
alvo = int(input("Digite o valor a remover: "))

# Verificar e remover se existir
if alvo in lista:
    lista.remove(alvo)

# Mostrar o tamanho depois
print("Tamanho depois:", len(lista))
