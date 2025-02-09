# Muito semelhante ao cadastro do cliente

def cadastro_fornecedores():

    listaFornecedores = []

    print(10 * "==", "MENU PRINCIPAL", 10 * "==")
    print("1. Cadastros;\n2. Vendas / MVP;\n3. Relatórios;\n4. Sair;")
    menuPrincipal = int(input("Selecione a sua opção: "))

    while True:

        if menuPrincipal == 1:
            print(10 * "==", "CADASTROS", 10 * "==")
            print("1. Clientes;\n2. Produtos;\n3. Fornecedores;\n4. Voltar ao Menu Principal;")
            menuCadastro = int(input("Selecione qual cadastro deseja realizar: "))

            while True:

                if menuCadastro == 3:
                    print(10 * "==", "CADASTRO DE FORNECEDORES", 10 * "==")
                    print("1. Adicionar;\n2. Consultar;\n3. Alterar;\n4. Excluir;\n5. Voltar ao Menu de Cadastros;")
                    cadastroFornecedores = int(input("Selecione a sua opção: "))

                    if cadastroFornecedores == 1:
                        nomeFornecedore = str(input("Qual o nome do(a) cliente? ")).strip()
                        listaFornecedores.append(nomeFornecedore)

                    elif cadastroFornecedores == 2:
                        print(", " .join(listaFornecedores))

                    elif cadastroFornecedores == 3:
                        alterar_fornecedor = input("Digite o nome do Fornecedor para alterar o cadastro: ")
                        if alterar_fornecedor in listaFornecedores:
                            listaFornecedores.remove(alterar_fornecedor)
                            novo_nomefornecedor = input("Digite o novo nome do Fornecedor: ")
                            listaFornecedores.append(novo_nomefornecedor)
                            print("Cadastro alterado com sucesso.")
                        else:
                            print("O fornecedor digitado não está na lista.")
                
                    elif cadastroFornecedores == 4:
                        excluir_fornecedor = input("Digite o nome do fornecedor para excluir o cadastro: ")
                        if excluir_fornecedor in listaFornecedores:
                            listaFornecedores.remove(excluir_fornecedor)
                            print("Cadastro removido com sucesso.")
                        else:
                            print("O fornecedor digitado não está na lista.")

                    elif cadastroFornecedores == 5:
                        break
                    else:
                        print("Opção inválida, tente novamente.")


cadastro_fornecedores()



                