opcao = 0
nome1 = "Não definido"
tel1 = "Não defindo"
nome2 = "Não definido"
tel2 = "Não defindo"
nome3 = "Não definido"
tel3 = "Não defindo"

while opcao != 7:
    print("..: Gerenciador de Contatos :..\n")
    print("1 - Salvar Contato 1           \n")
    print("2 - Salvar Contato 2           \n")
    print("3 - Salvar Contato 3           \n")
    print("4 - Exibir Contato 1           \n")
    print("5 - Exibir Contato 2           \n")
    print("6 - Exibir Contato 3           \n")
    print("7 - Encerrar Aplicação         \n")
    opcao = int(input("Digite a opção: "))

    if opcao == 1:
        nome1 = str(input("Digite o nome do Contato 1: "))
        tel1 = str(input("Digite o número de telefone do Contato 1: "))
        print("Contato salvo!")
    if opcao == 4:
        print("O nome é: " , nome1 ,     "\n")
        print("O telefone é: " , tel1 ,  "\n")
    if opcao == 2:
        nome2 = str(input("Digite o nome do Contato 2: "))
        tel2 = str(input("Digite o número de telefone do Contato 2: "))
        print("Contato salvo!")
    if opcao == 5:
        print("O nome é: " , nome2 ,     "\n")
        print("O telefone é: " , tel2 ,  "\n")
    if opcao == 3:
        nome3 = str(input("Digite o nome do Contato 3: "))
        tel3 = str(input("Digite o número de telefone do Contato 3: "))
        print("Contato salvo!")
    if opcao == 6:
        print("O nome é: " , nome3 ,     "\n")
        print("O telefone é: " , tel3 ,  "\n")

print("..: Programa encerrado :..")
