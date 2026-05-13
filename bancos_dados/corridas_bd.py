from .utils import ler_dados, salvar_dados

ARQUIVO = "bancos_dados/json/corridas.json"

def salvar_corridas(corrida):
    dados = ler_dados(ARQUIVO) 

    # Criamos um dicionário limpo para o JSON
    corrida_dict = {
        "id_corrida": corrida.id_corrida,
        "id_passageiro": corrida.passageiro.id_usuario,
        "passageiro": corrida.passageiro.nome_completo,
        "origem": corrida.origem,
        "destino": corrida.destino,
        "distancia": corrida.distancia,
        "status": corrida.status,
        "valor": corrida.valor, # <--- Aqui pega o resultado do calcular_preco()
        "tipo_veiculo": corrida.veiculo.tipo if corrida.veiculo else None
    }

    dados.append(corrida_dict)
    salvar_dados(ARQUIVO, dados)


def listar_corridas():
    return ler_dados(ARQUIVO)


def listar_corridas_passageiro(id_passageiro):
    """Retorna todas as corridas de um passageiro específico"""
    todas_corridas = ler_dados(ARQUIVO)
    corridas_passageiro = [
        c for c in todas_corridas 
        if c.get('id_passageiro') == id_passageiro
    ]
    return corridas_passageiro