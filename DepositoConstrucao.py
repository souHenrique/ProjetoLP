import cadastro_clientes
import cadastro_fornecedores
import cadastro_produtos
import pdv
import relatorios

while True:
    print(10 * "==", "MENU PRINCIPAL", 10 * "==")
    print("1. Cadastros;\n2. Vendas / MVP;\n3. Relatórios;\n4. Sair;")
    menuPrincipal = int(input("Selecione a sua opção: "))

    if menuPrincipal == 1:
        while True:

            print(10 * "==", "CADASTROS", 10 * "==")
            print("1. Clientes;\n2. Produtos;\n3. Fornecedores;\n4. Voltar ao Menu Principal;")
            menuCadastro = int(input("Selecione qual cadastro deseja realizar: "))

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

    elif menuPrincipal == 2:
        pdv.verificarClienteVenda()

        while True:
            adicionar_pedido = int(input("Deseja continuar a venda [1 - SIM / 2 - NÃO]: "))

            if adicionar_pedido == 1:
                pdv.adicionaPedido()

            elif adicionar_pedido == 2:
                pdv.verificaCompra()
                if len(pdv.resumo_venda) <= 0:
                    break
                pdv.finalizaCompra()
                break

    elif menuPrincipal == 3:
        print(10 * "==", "RELATÓRIO", 10 * "==")
        print("1 - FORNECEDORES: \n2 - VENDAS: \n3 - SAIDA DE PRODUTOS: Ranque de saida dos produtos durante as vendas")
        menuRelatorio = int(input("Digite a sua opção: "))

        if menuRelatorio == 1:
            relatorios.relatorioFornecedores()

        if menuRelatorio == 2:
            relatorios.relatorioVendas()

    #Quebra o loop do MENU
    elif menuPrincipal == 4:
        print("PROGRAMA ENCERRADO...")
        break

    else:
        print("Opção inválida, tente novamente.")