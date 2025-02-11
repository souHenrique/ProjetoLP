#Nesse aqui eu só mexi mesmo na questão da exclusão e da alteração também. Detalhe que tá tudo bem engessado, você precisa seguir uma única linha pra poder fazer o código funcionar, ele não vai tratar exceções

def cadastro_produtos():

    listaProdutos = []

    while True:

        print(10 * "==", "CADASTRO DE PRODUTOS", 10 * "==")
        print("1. Adicionar;\n2. Consultar;\n3. Alterar;\n4. Excluir;\n5. Voltar ao Menu de Cadastros;")
        cadastroProdutos = int(input("Selecione a sua opção: "))

        if cadastroProdutos == 1:
            nomeProduto = str(input("Digite a descrição: ")).strip()
            listaProdutos.append(nomeProduto)
            quantidadeProdutos = int(input("Digite o saldo em estoque: "))
            listaProdutos.append(quantidadeProdutos)
            precoProduto = float(input("Digite o preço de venda:"))
            listaProdutos.append(precoProduto)

        elif cadastroProdutos == 2:
            if len(listaProdutos) <= 0:
                print("Não há produto cadastrado.")
            else:
                for pos, prod in enumerate(listaProdutos):
                    print(f"Produto {pos + 1}: {prod}")

        elif cadastroProdutos == 3:
            alterar_produto = input("Digite o nome do Produto para alterar o cadastro: ")
            if alterar_produto in listaProdutos:
                indice_produto = listaProdutos.index(alterar_produto)
                del listaProdutos [indice_produto:indice_produto + 3]
                nova_descricaoProduto = input("Digite a nova descrição do produto: ")
                listaProdutos.append(nova_descricaoProduto)
                novo_saldoEstoque = input("Digite o novo saldo em estoque: ")
                listaProdutos.append(novo_saldoEstoque)
                novo_Preco = input("Digite o novo preço de venda: ")
                listaProdutos.append(novo_Preco)
                print("Cadastro alterado com sucesso.")
            else:
                print("O Produto digitado não está nos cadastros.")

        elif cadastroProdutos == 4:
            excluir_produto = input("Digite o nome do produto para excluir o cadastro: ")
            if excluir_produto in listaProdutos:
                indice_produto = listaProdutos.index(excluir_produto)
                del listaProdutos [indice_produto:indice_produto + 3]
                print("Cadastro removido com sucesso.")
            else:
                print("O produto digitado não está na lista.")

        elif cadastroProdutos == 5:
            return

        else:
            print("Opção inválida, tente novamente.")