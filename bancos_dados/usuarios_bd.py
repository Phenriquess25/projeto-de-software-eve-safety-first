from .utils import ler_dados, salvar_dados

ARQUIVO = "bancos_dados/json/usuarios.json"

def salvar_usuarios(usuario):
    dados = ler_dados(ARQUIVO)

    # Percorre a lista e vê se algum usuário já tem o mesmo CPF
    for u in dados:
        if u['cpf'] == usuario.cpf:
            print(f"Erro: Já existe um usuário cadastrado com o CPF {usuario.cpf}.")
            return False

    # Se o loop terminar sem encontrar nada, adicionamos o usuário
    dados.append(usuario.__dict__)
    salvar_dados(ARQUIVO, dados)
    print("Usuário cadastrado com sucesso!")
    return True


def listar_usuarios():
    return ler_dados(ARQUIVO)


def buscar_usuario_por_cpf(cpf):
    dados = ler_dados(ARQUIVO)

    for usuario in dados:
        if usuario["cpf"] == cpf:
            return usuario
    return None