# Muito semelhante ao cadastro do cliente

def cadastro_fornecedores():

    listaFornecedores = []

    while True:

        print(10 * "==", "CADASTRO DE FORNECEDORES", 10 * "==")
        print("1. Adicionar;\n2. Consultar;\n3. Alterar;\n4. Excluir;\n5. Voltar ao Menu de Cadastros;")
        cadastroFornecedores = int(input("Selecione a sua opção: "))

        if cadastroFornecedores == 1:
            nomeFornecedor = str(input("Qual o nome do(a) cliente? ")).strip()
            listaFornecedores.append(nomeFornecedor)

        elif cadastroFornecedores == 2:
            if len(listaFornecedores) <= 0:
                print("Não há fornecedor cadastrado")
            else:
                for pos, fornec in enumerate(listaFornecedores):
                    print(f"Fornecedor {pos + 1}: {fornec}")

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
            return

        else:
            print("Opção inválida, tente novamente.")