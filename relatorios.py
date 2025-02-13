import pdv

def relatorioFornecedores():
    print(max(pdv.vendasFornecedores, key=pdv.vendasFornecedores.count))

def relatorioVendas():
    print(30 * "==")
    for pos, venda in enumerate(pdv.vendasRealizadas):
        print(f"{pos + 1}° venda: R$ {sum(venda)}")
    print(30 * "==")
    print(f"Quantidade de vendas realizadas: {len(pdv.vendasRealizadas)}.")