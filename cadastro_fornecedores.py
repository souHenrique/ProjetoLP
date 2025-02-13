listaFornecedores = []

def cadastrarFornecedores():
    nomeFornecedor = str(input("Qual o nome do(a) fornecedor? ")).strip()
    listaFornecedores.append(nomeFornecedor)

def consultarFornecedores():
    if len(listaFornecedores) <= 0:
        print("Não há fornecedor cadastrado")
    else:
        for pos, fornec in enumerate(listaFornecedores):
            print(f"Fornecedor {pos + 1}: {fornec}")

def alterarFornecedores():
    alterar_fornecedor = input("Digite o nome do Fornecedor para alterar o cadastro: ")
    if alterar_fornecedor in listaFornecedores:
        listaFornecedores.remove(alterar_fornecedor)
        novo_nomefornecedor = input("Digite o novo nome do Fornecedor: ")
        listaFornecedores.append(novo_nomefornecedor)
        print("Cadastro alterado com sucesso.")
    else:
        print("O fornecedor digitado não está na lista.")

def excluirFornecedores():
    excluir_fornecedor = input("Digite o nome do fornecedor para excluir o cadastro: ")
    if excluir_fornecedor in listaFornecedores:
        listaFornecedores.remove(excluir_fornecedor)
        print("Cadastro removido com sucesso.")
    else:
        print("O fornecedor digitado não está na lista.")