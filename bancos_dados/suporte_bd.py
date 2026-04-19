from datetime import datetime
from .utils import ler_dados, salvar_dados

ARQUIVO = "bancos_dados/json/mensagens_suporte.json"

def salvar_mensagens(usuario, mensagem):
    dados = ler_dados(ARQUIVO)

    dados.append({
        "usuario": usuario.nome_completo,
        "mensagem": mensagem,
        "data_hora": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    })

    salvar_dados(ARQUIVO, dados)


def listar_mensagens():
    return ler_dados(ARQUIVO)
