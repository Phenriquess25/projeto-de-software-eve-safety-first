from .utils import ler_dados, salvar_dados

ARQUIVO = "bancos_dados/json/pagamentos.json"

def salvar_pagamentos(pagamento):
    dados = ler_dados(ARQUIVO)

    dados.append({
        "valor": pagamento.valor,
        "status": pagamento.status,
        "metodo": pagamento.__class__.__name__ # Salva se é 'Pix', 'Cartao', etc.
    })

    salvar_dados(ARQUIVO, dados)


def listar_pagamentos():
    return ler_dados(ARQUIVO)
