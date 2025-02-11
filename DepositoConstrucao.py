import cadastro_clientes
import cadastro_fornecedores
import cadastro_produtos

while True:
    print(10 * "==", "MENU PRINCIPAL", 10 * "==")
    print("1. Cadastros;\n2. Vendas / MVP;\n3. Relatórios;\n4. Sair;")
    menuPrincipal = int(input("Selecione a sua opção: "))

    if menuPrincipal == 1:

        while True:

            print(10 * "==", "CADASTROS", 10 * "==")
            print("1. Clientes;\n2. Produtos;\n3. Fornecedores;\n4. Voltar ao Menu Principal;")
            menuCadastro = int(input("Selecione qual cadastro deseja realizar: "))

            # Está chamando cada função de cadastro (clientes, produtos e fornecedores)
            while True:
                if menuCadastro == 1:

                    print(10 * "==", "CADASTRO DE CLIENTES", 10 * "==")
                    print("1. Adicionar;\n2. Consultar;\n3. Alterar;\n4. Excluir;\n5. Voltar ao Menu de Cadastros;")
                    cadastroClientes = int(input("Selecione a sua opção: "))

                    if cadastroClientes == 1:
                        cadastro_clientes.cadastrarCliente()

                    elif cadastroClientes == 2:
                        cadastro_clientes.consultarCliente()

                    elif cadastroClientes == 3:
                        cadastro_clientes.alterarCliente()

                    elif cadastroClientes == 4:
                        cadastro_clientes.excluirCliente()

                    elif cadastroClientes == 5:
                        break

                    else:
                        print("Opção inválida, tente novamente.")

                elif menuCadastro == 2:

                    print(10 * "==", "CADASTRO DE PRODUTOS", 10 * "==")
                    print("1. Adicionar;\n2. Consultar;\n3. Alterar;\n4. Excluir;\n5. Voltar ao Menu de Cadastros;")
                    cadastroProdutos = int(input("Selecione a sua opção: "))

                    if cadastroProdutos == 1:
                        cadastro_produtos.cadastrarProdutos()

                    elif cadastroProdutos == 2:
                        cadastro_produtos.consultarProdutos()

                    elif cadastroProdutos == 3:
                        cadastro_produtos.alterarProdutos()

                    elif cadastroProdutos == 4:
                        cadastro_produtos.excluirProdutos()

                    elif cadastroProdutos == 5:
                        break

                    else:
                        print("Opção inválida, tente novamente.")

                elif menuCadastro == 3:

                    print(10 * "==", "CADASTRO DE FORNECEDORES", 10 * "==")
                    print("1. Adicionar;\n2. Consultar;\n3. Alterar;\n4. Excluir;\n5. Voltar ao Menu de Cadastros;")
                    cadastroFornecedores = int(input("Selecione a sua opção: "))

                    if cadastroFornecedores == 1:
                        cadastro_fornecedores.cadastrarFornecedores()

                    elif cadastroFornecedores == 2:
                        cadastro_fornecedores.consultarFornecedores()

                    elif cadastroFornecedores == 3:
                        cadastro_fornecedores.alterarFornecedores()

                    elif cadastroFornecedores == 4:
                        cadastro_fornecedores.excluirFornecedores()

                    elif cadastroFornecedores == 5:
                        break

                    else:
                        print("Opção inválida, tente novamente.")

                #Quebra o loop dos CADASTROS
                elif menuCadastro == 4:
                    break

            #Impede que o programa fique preso no loop, quebrando o menu de cadastros
            if menuCadastro == 4:
                break

    #Quebra o loop do MENU
    elif menuPrincipal == 4:
        break

    else:
        print("Opção inválida, tente novamente.")