#Leia produto = {"nome": str, "preco": float}. Tente remover a chave "desconto" se existir, sem gerar erro. Mostre antes e depois.
#Use: input(), float(), dict.pop("chave", valor_padrao), print()

nome = input("Nome do produto: ")
preco = float(input("Preço do produto: "))

produto = {
    "nome": nome,
    "preco": preco
}

print("Antes:", produto)

produto.pop("desconto", None)

print("Depois:", produto)
