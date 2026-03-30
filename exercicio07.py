#Partindo de um aluno com nome e idade, leia uma nota (float) e adicione a chave "nota". Exiba o dicionário.

nome = input("Digite o nome do aluno: ")
idade = int(input("Digite a idade do aluno: "))

aluno = {
    "nome": nome,
    "idade": idade
}

nota = float(input("Digite a nota do aluno: "))
aluno["nota"] = nota

print(aluno)
