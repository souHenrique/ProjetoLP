listaClientes = []
listaProdutos = []
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
            if menuCadastro == 1:
                print(10 * "==", "CADASTRO DE CLIENTES", 10 * "==")
                print("1. Adicionar;\n2. Consultar;\n3. Alterar;\n4. Excluir;\n5. Voltar ao Menu de Cadastros;")
                cadastroClientes = int(input("Selecione a sua opção: "))
                if cadastroClientes == 1:
                    nomeCliente = str(input("Qual o nome do(a) cliente? ")).strip()
                    listaClientes.append(nomeCliente)
                elif cadastroClientes == 2:
                    print(listaClientes)
                elif cadastroClientes == 3:
                    print("Alterar")
                elif cadastroClientes == 4:
                    print("Excluir")
                elif cadastroClientes == 5:
                    break
                else:
                    print("Opção inválida, tente novamente.")
            elif menuCadastro == 2:
                print(10 * "==", "CADASTRO DE PRODUTOS", 10 * "==")
                print("1. Adicionar;\n2. Consultar;\n3. Alterar;\n4. Excluir;\n5. Voltar ao Menu de Cadastros;")
                cadastroProdutos = int(input("Selecione a sua opção: "))
                if cadastroProdutos == 1:
                    nomeProduto = str(input("Qual o nome do produto? ")).strip()
                    listaProdutos.append(nomeProduto)
                    quantidadeProdutos = int(input("Quantos produtos? "))
                    listaProdutos.append(quantidadeProdutos)
                    precoProduto = float(input("Valor do produto (preço individual):"))
                    listaProdutos.append(precoProduto)
                elif cadastroProdutos == 2:
                    print(listaProdutos)
                elif cadastroProdutos == 3:
                    print("Alterar")
                elif cadastroProdutos == 4:
                    print("Excluir")
                elif cadastroProdutos == 5:
                    break
                else:
                    print("Opção inválida, tente novamente.")
            elif menuCadastro == 3:
                print(10 * "==", "CADASTRO DE FORNECEDORES", 10 * "==")
                print("1. Adicionar;\n2. Consultar;\n3. Alterar;\n4. Excluir;\n5. Voltar ao Menu de Cadastros;")
                cadastroFornecedores = int(input("Selecione a sua opção: "))
                if cadastroFornecedores == 1:
                    nomeFornecedore = str(input("Qual o nome do(a) cliente? ")).strip()
                    listaFornecedores.append(nomeFornecedore)
                elif cadastroFornecedores == 2:
                    print(listaFornecedores)
                elif cadastroFornecedores == 3:
                    print("Alterar")
                elif cadastroFornecedores == 4:
                    print("Excluir")
                elif cadastroFornecedores == 5:
                    break
                else:
                    print("Opção inválida, tente novamente.")