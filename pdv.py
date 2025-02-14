import cadastro_clientes
import cadastro_produtos
import cadastro_fornecedores

item_comprado = []
resumo_venda = []
valor_total_venda = []

vendasRealizadas = []
vendasFornecedores = []
vendasProdutos = []

def verificarClienteVenda():
    global nome_cliente_venda

    nome_cliente_venda = input("Digite o nome do cliente: ")

    if nome_cliente_venda in cadastro_clientes.listaClientes:
        print(f"{nome_cliente_venda} está cadastrado. Seguindo...")

    else:
        print("O cliente digitado não está na lista.")
        nome_cliente_venda = input("Digite o nome do cliente para cadastrar: ")
        cadastro_clientes.listaClientes.append(nome_cliente_venda)
        print("Cadastro realizado com sucesso.")

def adicionaPedido():
    valor_venda = 0
    produto_encontrado = False

    nome_produto_venda = input("Digite o produto: ")
    quantidade_produto_venda = int(input("Digite a quantidade: "))

    for prod in cadastro_produtos.listaProdutos:
        if nome_produto_venda == prod[0]:
            produto_encontrado = True

            item_comprado.append(nome_produto_venda)
            item_comprado.append(quantidade_produto_venda)
            item_comprado.append(prod[2])
            item_comprado.append(prod[3])
            resumo_venda.append(item_comprado[:])
            item_comprado.clear()

            valor_venda += prod[2]
            valor_total_venda.append(valor_venda * quantidade_produto_venda)

            print("Produto adicionado ao carrinho com sucesso.")
            break

    if not produto_encontrado:

        print("O produto digitado não está cadastrado.")
        cadastro_produto_venda = input("Digite o nome do produto para cadastrar: ")
        cadastro_produtos.produto.append(cadastro_produto_venda)

        quantidadeProdutos = int(input("Digite a quantidade em estoque: "))
        cadastro_produtos.produto.append(quantidadeProdutos)

        precoProduto = float(input("Digite o preço de venda: R$ "))
        cadastro_produtos.produto.append(precoProduto)

        fornecedorProduto = str(input("Digite o nome do fornecedor do produto: "))
        cadastro_produtos.produto.append(fornecedorProduto)
        if fornecedorProduto not in cadastro_fornecedores.listaFornecedores:
            cadastro_fornecedores.listaFornecedores.append(fornecedorProduto)
            print(f"{fornecedorProduto} acabou de ser cadastrado. Seguindo...")

        cadastro_produtos.listaProdutos.append(cadastro_produtos.produto[:])
        cadastro_produtos.produto.clear()

        print("Cadastro realizado com sucesso.")

        quantidade_produto_venda = int(input("Digite a quantidade: "))

        item_comprado.append(cadastro_produto_venda)
        item_comprado.append(quantidade_produto_venda)
        item_comprado.append(precoProduto)
        item_comprado.append(fornecedorProduto)
        resumo_venda.append(item_comprado[:])
        item_comprado.clear()

        valor_venda += precoProduto
        valor_total_venda.append(valor_venda * quantidade_produto_venda)

        print("Produto adicionado ao carrinho com sucesso.")

def verificaCompra():
    if len(resumo_venda) <= 0:
        print("Nenhum produto foi comprado.")
        return

    else:
        print(30 * "==")
        print(f"Aqui está(ão) o(s) item(ns) que {nome_cliente_venda} deseja comprar: ")

        for pos, venda in enumerate(resumo_venda):
            print(f"Item {pos + 1}: {venda[0]}")
        print(30 * "==")

        print(f"Valor total da Compra: R$ {sum(valor_total_venda)}")
        print(30 * "==")

def finalizaCompra():
    print("FORMAS DE PAGAMENTO PARA FINALIZAR A VENDA: ")
    print("1 - DINHEIRO\n2 - PIX\n3 - CARTÃO DE CRÉDITO\n4 - CARTÃO DE DÉBITO")

    pagamento = int(input("Digite a forma de pagamento desejada: "))

    forma_de_pagamento = ""

    if pagamento == 1:
        forma_de_pagamento = 'DINHEIRO'
    elif pagamento == 2:
        forma_de_pagamento = 'PIX'
    elif pagamento == 3:
        forma_de_pagamento = 'CARTÃO DE CRÉDITO'
    elif pagamento == 4:
        forma_de_pagamento = 'CARTÃO DE DÉBITO'

    print(30 * "==")
    print(f"O valor de R$ {sum(valor_total_venda)} foi realizado com a forma de pagamento {forma_de_pagamento}\nCOMPRA REALIZADA COM SUCESSO!")

    for pos, venda in enumerate(resumo_venda):
        vendasFornecedores.append(venda[3])
        vendasProdutos.append(venda[0])

    vendasRealizadas.append(valor_total_venda[:])
    valor_total_venda.clear()

    resumo_venda.clear()
