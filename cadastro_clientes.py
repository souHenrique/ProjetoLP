listaClientes = []

def cadastrarCliente():
    nomeCliente = str(input("Qual o nome do(a) cliente? ")).strip()
    listaClientes.append(nomeCliente)

def consultarCliente():
    print(30 * "==")
    if len(listaClientes) <= 0:
        print("Não há cliente cadastrado.")
    else:
        for pos, cl in enumerate(listaClientes):
            print(f"Cliente {pos + 1}: {cl}")
        print(30 * "==")

def alterarCliente():
    alterar_cliente = input("Digite o nome do cliente para alterar o cadastro: ")
    if alterar_cliente in listaClientes:
        listaClientes.remove(alterar_cliente)
        novo_nomecliente = input("Digite o novo nome do cadastro: ")
        listaClientes.append(novo_nomecliente)
        print("Cadastro alterado com sucesso.")
    else:
        print("O cliente digitado não está na lista.")

def excluirCliente():
    excluir_cliente = input("Digite o nome do cliente para excluir o cadastro: ")
    if excluir_cliente in listaClientes:
        listaClientes.remove(excluir_cliente)
        print("Cadastro removido com sucesso.")
    else:
        print("O cliente digitado não está na lista.")