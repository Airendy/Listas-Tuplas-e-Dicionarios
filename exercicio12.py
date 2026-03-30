#Leia três frutas e coloque em uma tupla. Depois leia uma fruta e diga se ela está ou não na tupla.
#usar in
#usar input()
#tipo: str, tuple
#conceito: operador de pertinência

fruta1 = input("Digite a primeira fruta: ")
fruta2 = input("Digite a segunda fruta: ")
fruta3 = input("Digite a terceira fruta: ")

frutas = (fruta1, fruta2, fruta3)

fruta_procurada = input("Digite uma fruta para verificar: ")

if fruta_procurada in frutas:
    print("A fruta está na tupla.")
else:
    print("A fruta NÃO está na tupla.")
