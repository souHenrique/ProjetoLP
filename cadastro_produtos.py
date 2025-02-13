listaProdutos = []
produto = []

def cadastrarProdutos():

    nomeProduto = str(input("Digite qual o produto: ")).strip()
    produto.append(nomeProduto)

    quantidadeProdutos = int(input("Digite a quantidade em estoque: "))
    produto.append(quantidadeProdutos)

    precoProduto = float(input("Digite o preço de venda: R$ "))
    produto.append(precoProduto)

    fornecedorProduto = str(input("Digite o fornecedor do produto: "))
    produto.append(fornecedorProduto)

    listaProdutos.append(produto)

def consultarProdutos():
    print(30 * "==")
    tamanho = len(listaProdutos) / 3
    if tamanho <= 0:
        print("Não há produto cadastrado.")
    else:
        for pos, prod in enumerate(listaProdutos):
            print(f"Produto {pos + 1}\n")
            print(f"Produto: {prod[0]}\nQuantidade em estoque: {prod[1]}\nPreço unitário: R$ {prod[2]}\nFornecedor: {prod[3]}")
            print(30 * "==")

def alterarProdutos():
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

def excluirProdutos():
    excluir_produto = input("Digite o nome do produto para excluir o cadastro: ")
    if excluir_produto in listaProdutos:
        indice_produto = listaProdutos.index(excluir_produto)
        del listaProdutos [indice_produto:indice_produto + 3]
        print("Cadastro removido com sucesso.")
    else:
        print("O produto digitado não está na lista.")