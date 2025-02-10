listaClientes = []
listaProdutos = []
    
def realizar_venda():

#Contador para totalizar o valor a receber na venda    

    valor_total_venda = 0

#Deixei as listas como variáveis globais para o código inteiro acessar. Não sei como vai funcionar quando modularizar

    global listaClientes
    global listaProdutos

#Lista para listar os produtos da venda. Toda vez que finalizar uma venda ela será limpa para adicionar uma nova venda

    resumo_venda = []

    nome_cliente_venda = input("Digite o nome do cliente: ")

#No geral, no caso da identificação do produto e do cliente na venda, coloquei as opções para cadastrar na hora, caso não haja cadastro. Pra não precisar voltar para a tela inicial de cadastro. Então basicamente se trata de condições, laços e manipulação de lista.

    if nome_cliente_venda in listaClientes:
        print(f"{nome_cliente_venda} está cadastrado. Seguindo...")

    else:
        print("O cliente digitado não está na lista.")
        cadastro_cliente_venda = input("Digite o nome do cliente para cadastrar: ")
        listaClientes.append(cadastro_cliente_venda)
        print("Cadastro realizado com sucesso.")

        while True:
        
            adicionar_pedido = int(input("Deseja continuar a venda [1 - SIM / 2 - NÃO]: "))

            if adicionar_pedido == 1:

                nome_produto_venda = input("Digite o produto: ")
                quantidade_produto_venda = int(input("Digite a quantidade: "))

                if nome_produto_venda in listaProdutos:

                    resumo_venda.append(nome_produto_venda)
                    resumo_venda.append(quantidade_produto_venda)

                    indice_produto_cadastrado = listaProdutos.index(nome_produto_venda)

                    for c in range(indice_produto_cadastrado, len(listaProdutos), 3):

                        resumo_venda.append(listaProdutos[c])
                        valor_total_item = listaProdutos[c] * quantidade_produto_venda
                        valor_total_venda += valor_total_item

                    print("Produto adicionado a venda com sucesso.")

                else:
                    print("O produto digitado não está cadastrado.")
                    cadastro_produto_venda = input("Digite o nome do produto para cadastrar: ")
                    listaProdutos.append(cadastro_produto_venda)
                    quantidadeProdutos = int(input("Digite o saldo em estoque: "))
                    listaProdutos.append(quantidadeProdutos)
                    precoProduto = float(input("Digite o preço de venda:"))
                    listaProdutos.append(precoProduto)
                    print("Cadastro realizado com sucesso.")
                    
                    resumo_venda.append(cadastro_produto_venda)
                    resumo_venda.append(quantidade_produto_venda)

                    indice_produto = listaProdutos.index(cadastro_produto_venda)

                    for c in range(indice_produto + 2, len(listaProdutos), 3):

                        resumo_venda.append(listaProdutos[c])
                        valor_total_item = listaProdutos[c] * quantidade_produto_venda
                        valor_total_venda += valor_total_item

                    print("Produto adicionado a venda com sucesso.")

            elif adicionar_pedido == 2:

                print(f"Aqui está os itens que {nome_cliente_venda} deseja comprar: ")

                for c in range(0, len(resumo_venda), 3):

                    bloco_listado = resumo_venda[c:c+3]
                    listagem_venda = "     --     " .join(map(str, bloco_listado))
                    print(listagem_venda)

                print(f"Valor total da Compra: {valor_total_venda}")

                print("FORMAS DE PAGAMENTO PARA FINALIZAR A VENDA: ")
                print("1 - DINHEIRO\n 2 - PIX\n 3 - CARTÃO DE CRÉDITO\n 4- CARTÃO DE DÉBITO")
                
                pagamento = int(input("Digite a forma de pagamento desejada: "))

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

realizar_venda()

