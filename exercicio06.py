#Leia nome e idade. Crie aluno = {"nome": ..., "idade": ...} e exiba o dicionário e seu tipo.
#Use: input(), int(), literal {}, acesso por chave dict["chave"], print(), type()

nome = input("Digite o nome do aluno: ")
idade = int(input("Digite a idade do aluno: "))

aluno = {
    "nome": nome,
    "idade": idade
}

print(aluno)
print(type(aluno))
