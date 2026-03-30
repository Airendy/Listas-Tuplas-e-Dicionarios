#Leia produto = {"nome": str, "preco": float, "quantidade": int}. Aplique aumento percentual ao preço e some 2 unidades na quantidade. Calcule total = preco * quantidade e exiba.
#Use: float(), int(), input(), acesso/atribuição por chave, print()

nome = input("Nome do produto: ")
preco = float(input("Preço do produto: "))
quantidade = int(input("Quantidade do produto: "))

produto = {
    "nome": nome,
    "preco": preco,
    "quantidade": quantidade
}

aumento = float(input("Percentual de aumento do preço: "))

produto["preco"] = produto["preco"] + (produto["preco"] * aumento / 100)

produto["quantidade"] = produto["quantidade"] + 2

total = produto["preco"] * produto["quantidade"]

print(produto)
print("Total:", total)
