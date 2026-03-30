#Inicie fila = ["Ana", "Bruno"]. Leia dois nomes e adicione (use extend). Leia um cliente prioritário e insira na posição 1. Atenda (remova e capture) o primeiro com pop(0). Exiba a fila a cada etapa.
#Use: input(), extend(), insert(), pop(), print()

fila = ["Ana", "Bruno"]
print("Fila inicial:", fila)

nome1 = input("Digite um nome: ")
nome2 = input("Digite outro nome: ")
fila.extend([nome1, nome2])
print("Após adicionar nomes:", fila)

prioritario = input("Digite o nome do cliente prioritário: ")
fila.insert(1, prioritario)
print("Após inserir prioritário:", fila)

atendido = fila.pop(0)
print("Cliente atendido:", atendido)

print("Fila final:", fila)
