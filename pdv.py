import cadastro_clientes
import cadastro_produtos

def realizar_venda():

    #Contador para totalizar o valor a receber na venda
    valor_total_venda = 0
    contador = 0

    #Lista para listar os produtos da venda. Toda vez que finalizar uma venda ela será limpa para adicionar uma nova venda
    item_comprado = []
    resumo_venda = []

    nome_cliente_venda = input("Digite o nome do cliente: ")

    #No geral, no caso da identificação do produto e do cliente na venda, coloquei as opções para cadastrar na hora, caso não haja cadastro. Pra não precisar voltar para a tela inicial de cadastro. Então basicamente se trata de condições, laços e manipulação de lista.
    if nome_cliente_venda in cadastro_clientes.listaClientes:
        print(f"{nome_cliente_venda} está cadastrado. Seguindo...")

    else:
        print("O cliente digitado não está na lista.")
        cadastro_cliente_venda = input("Digite o nome do cliente para cadastrar: ")
        cadastro_clientes.listaClientes.append(cadastro_cliente_venda)
        print("Cadastro realizado com sucesso.")

    #Ainda falta concluir, está multiplicando os itens cadastrados na litas (repetidos)
    while True:
        adicionar_pedido = int(input("Deseja continuar a venda [1 - SIM / 2 - NÃO]: "))

        if adicionar_pedido == 1:

            nome_produto_venda = input("Digite o produto: ")
            quantidade_produto_venda = int(input("Digite a quantidade: "))

            for prod in cadastro_produtos.listaProdutos:
                for item in prod:
                    if nome_produto_venda == item:
                        contador += 1
                        item_comprado.append(nome_produto_venda)
                        item_comprado.append(quantidade_produto_venda)
                        item_comprado.append(prod[2])
                        item_comprado.append(prod[3])
                        resumo_venda.append(item_comprado)
                        print(resumo_venda)
                        print("Produto adicionado a venda com sucesso.")

            if contador == 0:

                print("O produto digitado não está cadastrado.")
                cadastro_produto_venda = input("Digite o nome do produto para cadastrar: ")
                cadastro_produtos.produto.append(cadastro_produto_venda)

                quantidadeProdutos = int(input("Digite a quantidade em estoque: "))
                cadastro_produtos.produto.append(quantidadeProdutos)

                precoProduto = float(input("Digite o preço de venda: R$ "))
                cadastro_produtos.produto.append(precoProduto)

                fornecedorProduto = str(input("Digite o nome do fornecedor do produto: "))
                cadastro_produtos.produto.append(fornecedorProduto)

                cadastro_produtos.listaProdutos.append(cadastro_produtos.produto)

                print("Cadastro realizado com sucesso.")

                for prod in cadastro_produtos.listaProdutos:
                    for item in prod:
                        if nome_produto_venda == item:
                            contador = 0
                            item_comprado.append(cadastro_produto_venda)
                            item_comprado.append(quantidadeProdutos)
                            item_comprado.append(precoProduto)
                            item_comprado.append(fornecedorProduto)
                            resumo_venda.append(item_comprado)
                            print(resumo_venda)

                print("Produto adicionado a venda com sucesso.")

        #Ainda não está conseguindo mostrar os itens corretamente
        elif adicionar_pedido == 2:

            if len(resumo_venda) <= 0:
                print("Nenhum produto foi comprado.")

            else:

                print(f"Aqui está os itens que {nome_cliente_venda} deseja comprar: ")

                for venda in resumo_venda:
                    print(f"{venda[0]}")

                '''for c in range(0, len(resumo_venda), 3):

                    bloco_listado = resumo_venda[c:c+3]
                    listagem_venda = "     --     " .join(map(str, bloco_listado))
                    print(listagem_venda)'''

                print(f"Valor total da Compra: {valor_total_venda}")

                print("FORMAS DE PAGAMENTO PARA FINALIZAR A VENDA: ")
                print("1 - DINHEIRO\n 2 - PIX\n 3 - CARTÃO DE CRÉDITO\n 4- CARTÃO DE DÉBITO")

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

                print(f"O valor de {valor_total_venda} foi realizado com a forma de pagamento {forma_de_pagamento}\n COMPRA REALIZADA COM SUCESSO!")

                resumo_venda.clear()

                break