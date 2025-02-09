#Vai ficar faltando refinar, com o tratamento de exceções, tratamento de strings, inclusão da função time pra melhorar a interação e etc.

def cadastro_cliente():

    listaClientes = []

    print(10 * "==", "MENU PRINCIPAL", 10 * "==")
    print("1. Cadastros;\n2. Vendas / MVP;\n3. Relatórios;\n4. Sair;")
    menuPrincipal = int(input("Selecione a sua opção: "))

    while True:

        if menuPrincipal == 1:
            print(10 * "==", "CADASTROS", 10 * "==")
            print("1. Clientes;\n2. Produtos;\n3. Fornecedores;\n4. Voltar ao Menu Principal;")
            menuCadastro = int(input("Selecione qual cadastro deseja realizar: "))
            
            while True:
                
                if menuCadastro == 1:
                    print(10 * "==", "CADASTRO DE CLIENTES", 10 * "==")
                    print("1. Adicionar;\n2. Consultar;\n3. Alterar;\n4. Excluir;\n5. Voltar ao Menu de Cadastros;")
                    cadastroClientes = int(input("Selecione a sua opção: "))
                
                    if cadastroClientes == 1:
                        nomeCliente = str(input("Qual o nome do(a) cliente? ")).strip()
                        listaClientes.append(nomeCliente)
                
                    elif cadastroClientes == 2:
                        print(", " .join(listaClientes))
            
                    #Do que você fez, eu avancei um pouco na parte de Exclusão e Alteração de cadastros
                    elif cadastroClientes == 3:
                        alterar_cliente = input("Digite o nome do cliente para alterar o cadastro: ")
                        if alterar_cliente in listaClientes:
                            listaClientes.remove(alterar_cliente)
                            novo_nomecliente = input("Digite o novo nome do cadastro: ")
                            listaClientes.append(novo_nomecliente)
                            print("Cadastro alterado com sucesso.")
                        else:
                            print("O cliente digitado não está na lista.")
                
                    elif cadastroClientes == 4:
                        excluir_cliente = input("Digite o nome do cliente para excluir o cadastro: ")
                        if excluir_cliente in listaClientes:
                            listaClientes.remove(excluir_cliente)
                            print("Cadastro removido com sucesso.")
                        else:
                            print("O cliente digitado não está na lista.")
                
                    elif cadastroClientes == 5:
                        break
                    else:
                        print("Opção inválida, tente novamente.")

cadastro_cliente()