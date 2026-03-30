#agenda = {"Ana", "1111-1111", "Bruno": "2222-2222"}
#Adicionar um novo contato (nome→telefone)
#Atualizar o telefone de um contato informado (se existir)
#Remover um contato pelo nome (se existir)
#Exibir a lista ordenada de nomes de contatos

agenda = {
    "Ana": "1111-1111",
    "Bruno": "2222-2222"
}

print("Agenda inicial:", agenda)

nome_novo = input("Digite o nome do novo contato: ")
telefone_novo = input("Digite o telefone do novo contato: ")
agenda[nome_novo] = telefone_novo
print("Após adicionar:", agenda)

nome_atualizar = input("Digite o nome para atualizar o telefone: ")
if nome_atualizar in agenda:
    novo_telefone = input("Digite o novo telefone: ")
    agenda[nome_atualizar] = novo_telefone
print("Após atualizar:", agenda)

nome_remover = input("Digite o nome do contato a remover: ")
agenda.pop(nome_remover, None)
print("Após remover:", agenda)

print("Contatos ordenados:")
for nome in sorted(agenda):
    print(nome, "-", agenda[nome])
