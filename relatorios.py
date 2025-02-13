import pdv

def relatorioFornecedores():
    relatorio_vendasFornecedores = {}

    for fornec in pdv.vendasFornecedores:
        if fornec in relatorio_vendasFornecedores:
            relatorio_vendasFornecedores[fornec] += 1
        else:
            relatorio_vendasFornecedores[fornec] = 1

    fornec_total_vendas = 0
    fornec_mais_vendeu = None

    for fornec, contagem in relatorio_vendasFornecedores.items():
        if contagem > fornec_total_vendas:
            fornec_total_vendas = contagem
            fornec_mais_vendeu = fornec

    print(30 * "==")
    if fornec_total_vendas == 0 and fornec_mais_vendeu == None:
        print("Não houveram vendas para o relatório.")
    else:
        print(f"O fornecedor mais solicitado foi o '{fornec_mais_vendeu}' com um total de {fornec_total_vendas} produtos que foram vendidos.")


def relatorioVendas():
    print(30 * "==")
    for pos, venda in enumerate(pdv.vendasRealizadas):
        print(f"{pos + 1}° venda: R$ {sum(venda)}")
    print(30 * "==")
    print(f"Quantidade de vendas realizadas: {len(pdv.vendasRealizadas)}.")

def relatorioProdutos():
    relatorio_vendasProdutos = {}

    for prod in pdv.vendasProdutos:
        if prod in relatorio_vendasProdutos:
            relatorio_vendasProdutos[prod] += 1
        else:
            relatorio_vendasProdutos[prod] = 1

    prod_total_vendas = 0
    prod_mais_vendido = None

    for prod, contagem in relatorio_vendasProdutos.items():
        if contagem > prod_total_vendas:
            prod_total_vendas = contagem
            prod_mais_vendido = prod

    print(30 * "==")
    if prod_total_vendas == 0 and prod_mais_vendido == None:
        print("Não houveram vendas para o relatório.")
    else:
        print(f"O produto mais vendido foi o '{prod_mais_vendido}' com um total de {prod_total_vendas} produtos que foram vendidos.")