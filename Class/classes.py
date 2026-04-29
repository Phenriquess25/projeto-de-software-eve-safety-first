import uuid
import re  # biblioteca para manipulação de strings (regex)
import random 
from datetime import date 
from abc import ABC, abstractmethod

# =========================
# FUNÇÕES DE VALIDAÇÃO
# =========================

def validar_cnh(cnh):
    # Remove todos os caracteres que não são números (ex: ".", "-", espaços)
    cnh = re.sub(r'\D', '', cnh)

    # Verifica se a CNH tem exatamente 11 dígitos
    if len(cnh) != 11:
        return False

    # Verifica se todos os dígitos são iguais (ex: 11111111111)
    if cnh == cnh[0] * 11:
        return False

    # Cálculo do Primeiro Dígito Verificador (DV1)
    soma = 0
    # Pesos de 9 até 1
    for i in range(9):
        soma += int(cnh[i]) * (9 - i)

    resto1 = soma % 11
    
    # Define o valor do decremento para o próximo cálculo
    # Se o resto for > 9, o dígito é 0 e o decremento é 2
    if resto1 > 9:
        v_dsc = 2
        dig1 = 0
    else:
        v_dsc = 0
        dig1 = resto1

    # Cálculo do Segundo Dígito Verificador (DV2)
    soma = 0
    # Pesos de 1 até 9
    for i in range(9):
        soma += int(cnh[i]) * (1 + i)

    resto2 = soma % 11
    
    # Aplicação da regra do decremento
    dig2 = resto2 - v_dsc
    
    # Ajustes finais para o segundo dígito
    if dig2 < 0:
        dig2 += 11
    if dig2 > 9:
        dig2 = 0

    # Comparação Final
    # Verifica se os dígitos calculados batem com os informados
    return str(dig1) == cnh[9] and str(dig2) == cnh[10]

    
def validar_cpf(cpf):
    cpf = re.sub(r'\D', '', cpf)

    if len(cpf) != 11:
        return False

    if cpf == cpf[0] * 11:
        return False

    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    dig1 = (soma * 10 % 11) % 10

    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    dig2 = (soma * 10 % 11) % 10

    return dig1 == int(cpf[9]) and dig2 == int(cpf[10])


def validar_email(email):
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$' 
    return re.match(padrao, email) is not None


# =========================
# 1. USUARIO
# =========================
class Usuario(ABC):
    def __init__(self, nome_completo, cpf, email, senha, telefone, tipo_usuario):
        self.id_usuario = self._gerar_id_unico()
        self.nome_completo = nome_completo
        self.cpf = cpf 
        self.email = email
        self.senha = senha
        self.telefone = telefone
        self.tipo_usuario = tipo_usuario
        self.status_conta = False
    
    def _gerar_id_unico(self):
        return str(uuid.uuid4())
    
    def cadastrar(self):
        print(f"{self.tipo_usuario.title()} {self.nome_completo} criado com ID: {self.id_usuario}")
        return self
    
    def validar_documentos(self):
        if not self.nome_completo:
            print("Nome inválido")
            return False

        if not validar_cpf(self.cpf):
            print("CPF inválido")
            return False

        if not validar_email(self.email):
            print("Email inválido")
            return False

        print("Validação básica concluída")
        return True
    
    def confirmar_conta(self):
        self.status_conta = True
        print(f"Conta de {self.tipo_usuario} confirmada com sucesso!")

    @abstractmethod
    def mostrar_dados(self):
        pass

# =========================
# HERANÇA E POLIMORFISMO USUARIO
# =========================
class Passageiro(Usuario):
    def __init__(self, nome_completo, cpf, email, senha, telefone):
        super().__init__(nome_completo, cpf, email, senha, telefone, "passageiro")
        self.historico = []

    def solicitar_corrida(self, origem, destino):
        print(f"{self.nome_completo} solicitou corrida de {origem} para {destino}")

    def validar_documentos(self):
        if not super().validar_documentos():
            return False

        print("Documentos do passageiro validados")
        return True

    def mostrar_dados(self):
        print("=== Dados do Passageiro ===")
        print(f"Nome: {self.nome_completo}")
        print(f"CPF: {self.cpf}")
        print(f"Email: {self.email}")
        print(f"Telefone: {self.telefone}")


class Motorista(Usuario):
    def __init__(self, nome_completo, cpf, email, senha, telefone, cnh,
                 placa, modelo_veiculo):
        super().__init__(nome_completo, cpf, email, senha, telefone, "motorista")
        self.cnh = cnh
        self.placa = placa
        self.modelo_veiculo = modelo_veiculo
        self.veiculo = None
        self.cancelamentos = 0

    def cadastrar_veiculo(self, veiculo):
        self.veiculo = veiculo
        print(f"Veículo {veiculo.tipo} cadastrado para {self.nome_completo}")

    def validar_documentos(self):
        if not super().validar_documentos():
            return False

        if not validar_cnh(self.cnh):
            print("CNH inválida")
            return False

        print("Documentos do motorista validados")
        return True

    def mostrar_dados(self):
        print("=== Dados do Motorista ===")
        print(f"Nome: {self.nome_completo}")
        print(f"CNH: {self.cnh}")
        print(f"Placa: {self.placa}")
        print(f"Modelo: {self.modelo_veiculo}")
        if self.veiculo:
            print(f"Tipo de veículo: {self.veiculo.tipo}")


# =========================
# 2. LOGIN
# =========================
class Login:
    def __init__(self, usuario: Usuario):
        self.usuario = usuario

    def autenticar(self, email, senha):
        if self.usuario.email == email and self.usuario.senha == senha:
            if self.usuario.status_conta:
                print("Login realizado com sucesso!")
                return True
            else:
                print("Conta não confirmada")
        else:
            print("Dados incorretos")
        return False


# =========================
# 3. CORRIDA
# =========================
class Corrida:
    def __init__(self, passageiro: Passageiro, origem, destino):
        self.id_corrida = str(uuid.uuid4())
        self.passageiro = passageiro
        self.origem = origem
        self.destino = destino
        self.distancia = 0
        self.status = "pendente"
        self.valor = 0
        self.veiculo = None

    def calcular_distancia(self):
        self.distancia = round(random.uniform(1, 50), 2)
        print(f"Distância calculada: {self.distancia} km")

    def escolher_veiculo(self, veiculo):
        self.veiculo = veiculo
        print(f"Veículo escolhido: {veiculo.tipo}")

    def calcular_preco(self):
        if not self.veiculo:
            print("Escolha um veículo primeiro!")
            return
        
        if self.distancia == 0:
            self.calcular_distancia()

        self.valor = self.veiculo.calcular_tarifa(self.distancia)
        print(f"Preço da corrida: R${self.valor}")

    def confirmar(self):
        self.status = "confirmada"
        print("Corrida confirmada")


# =========================
# 4. RASTREAMENTO
# =========================
class Rastreamento:
    def __init__(self, corrida: Corrida):
        self.corrida = corrida

    def atualizar_localizacao(self, local):
        print(f"Motorista está em: {local}")

    def calcular_tempo(self):
        print("Tempo estimado: 5 minutos")


# =========================
# 5. VEICULO (ABSTRACT CLASS,HERANÇA E POLIMORFISMO)
# =========================
class Veiculo(ABC):
    def __init__(self, tipo):
        self.tipo = tipo

    @abstractmethod
    def calcular_tarifa(self, distancia):
        pass


class Moto(Veiculo):
    def __init__(self):
        super().__init__("Moto")

    def calcular_tarifa(self, distancia):
        return distancia * 1


class Carro(Veiculo):
    def __init__(self):
        super().__init__("Carro")

    def calcular_tarifa(self, distancia):
        return distancia * 2


class VeiculoVIP(Veiculo):
    def __init__(self):
        super().__init__("VIP")

    def calcular_tarifa(self, distancia):
        return distancia * 4


# =========================
# 6. PAGAMENTO (HERANÇA E POLIMORFISMO)
# =========================
class Pagamento(ABC):
    def __init__(self, valor):
        self.valor = valor
        self.status = "pendente"

    @abstractmethod
    def processar_pagamento(self):
        pass

    def mostrar_status(self):
        print(f"Status do pagamento: {self.status}")

class PagamentoPix(Pagamento):
    def __init__(self, valor):
        super().__init__(valor) 
        
    def processar_pagamento(self):
        self.status = "aprovado"
        print(f"Pagamento de R${self.valor} via PIX aprovado")

class PagamentoCartao(Pagamento):
    def __init__(self, valor):
        super().__init__(valor)

    def processar_pagamento(self):
        self.status = "aprovado"
        print(f"Pagamento de R${self.valor} com cartão aprovado")

class PagamentoDinheiro(Pagamento):
    def __init__(self, valor):
        super().__init__(valor)

    def processar_pagamento(self):
        self.status = "pago na entrega"
        print(f"Pagamento de R${self.valor} será feito em dinheiro")


# =========================
# 7. HISTORICO
# =========================
class Historico:
    def __init__(self, usuario: Usuario):
        self.usuario = usuario
        self.corridas = []

    def adicionar(self, corrida: Corrida):
        self.corridas.append(corrida)

    def visualizar(self):
        print(f"Histórico de {self.usuario.nome_completo}")
        for c in self.corridas:
            print(f"{c.origem} -> {c.destino} ({c.status})")


# =========================
# 8. AVALIACAO
# =========================
class Avaliacao:
    def __init__(self, usuario, motorista, nota, comentario):
        self.usuario = usuario
        self.motorista = motorista
        self.nota = nota
        self.comentario = comentario

    def avaliar(self):
        print(f"{self.usuario.nome_completo} avaliou {self.motorista.nome_completo}")
        print(f"Nota: {self.nota} - {self.comentario}")


# =========================
# 9. CONTROLE DE CANCELAMENTO
# =========================
class ControleCancelamento:
    MOTIVOS_VALIDOS = [
        "Problema no carro",
        "Trânsito extremo",
        "Emergência"
    ]

    def __init__(self, limite_por_dia):
        self.limite = limite_por_dia
        self.cancelamentos = 0
        self.data_atual = date.today() 

    def verificar_reset(self):
        if date.today()!= self.data_atual:
            self.cancelamentos = 0
            self.data_atual = date.today() 

    def mostrar_motivos(self):
        print("Motivos disponíveis:")
        for m in self.MOTIVOS_VALIDOS:
            print("-", m) 

    def cancelar_corrida(self, motivo):
        self.verificar_reset()
        
        if not motivo or motivo.strip() == "":
            print("Erro: é obrigatório informar o motivo do cancelamento")
            return

        if motivo not in self.MOTIVOS_VALIDOS:
            print("Erro: motivo inválido")
            self.mostrar_motivos()
            return

        if self.cancelamentos < self.limite:
            self.cancelamentos += 1
            print(f"Corrida cancelada. Motivo: {motivo}")
        else:
            print("Limite de cancelamentos atingido")


# =========================
# 10. SUPORTE
# =========================
class Suporte:
    def __init__(self, usuario: Usuario):
        self.usuario = usuario
        self.mensagens = []

    def enviar(self, mensagem):
        self.mensagens.append(mensagem)
        print("Mensagem enviada ao suporte")

    def historico(self):
        print("Mensagens:")
        for m in self.mensagens:
            print("-", m)
