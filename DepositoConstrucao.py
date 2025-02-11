import cadastro_clientes
import cadastro_fornecedores
import cadastro_produtos
import menu_principal

menu = menu_principal.menuPrincipal()

#Está chamando cada função de cadastro
while True:
    if menu == 1:
        print(10 * "==", "CADASTROS", 10 * "==")
        print("1. Clientes;\n2. Produtos;\n3. Fornecedores;\n4. Voltar ao Menu Principal;")
        menuCadastro = int(input("Selecione qual cadastro deseja realizar: "))

        while True:
            if menuCadastro == 1:
                cadastro_clientes.cadastro_cliente()

            elif menuCadastro == 2:
                cadastro_produtos.cadastro_produtos()

            elif menuCadastro == 3:
                cadastro_fornecedores.cadastro_fornecedores()

    elif menu == 4:
        break