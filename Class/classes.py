import uuid

# =========================
# 1. USUARIO
# =========================
class Usuario:
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
        if self.tipo_usuario == "motorista":
            print("Validando CNH e documentos do motorista...")
        else:
            print("Validando CPF e documentos do passageiro...")
        return True
    
    def confirmar_conta(self):
        self.status_conta = True
        print(f"Conta de {self.tipo_usuario} confirmada com sucesso!")


# =========================
# HERANÇA USUARIO
# =========================
class Passageiro(Usuario):
    def __init__(self, nome_completo, cpf, email, senha, telefone):
        super().__init__(nome_completo, cpf, email, senha, telefone, "passageiro")
        self.historico = []

    def solicitar_corrida(self, origem, destino):
        print(f"{self.nome_completo} solicitou corrida de {origem} para {destino}")

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
        self.distancia = 10
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
# 5. VEICULO (HERANÇA)
# =========================
class Veiculo:
    def __init__(self, tipo, preco_km):
        self.tipo = tipo
        self.preco_km = preco_km

    def calcular_tarifa(self, distancia):
        return distancia * self.preco_km


class Moto(Veiculo):
    def __init__(self):
        super().__init__("Moto", 1.0)


class Carro(Veiculo):
    def __init__(self):
        super().__init__("Carro", 2.0)


class VeiculoVIP(Veiculo):
    def __init__(self):
        super().__init__("VIP", 4.0)


# =========================
# 6. PAGAMENTO (HERANÇA)
# =========================
class Pagamento:
    def __init__(self, valor, metodo):
        self.valor = valor
        self.metodo = metodo
        self.status = "pendente"

    def processar_pagamento(self):
        self.status = "aprovado"
        print("Pagamento realizado com sucesso")


class PagamentoPix(Pagamento):
    def __init__(self, valor):
        super().__init__(valor, "pix")

    def processar_pagamento(self):
        self.status = "aprovado"
        print(f"Pagamento de R${self.valor} via PIX realizado com sucesso")


class PagamentoCartao(Pagamento):
    def __init__(self, valor):
        super().__init__(valor, "cartao")

    def processar_pagamento(self):
        self.status = "aprovado"
        print(f"Pagamento de R${self.valor} com cartão realizado com sucesso")


class PagamentoDinheiro(Pagamento):
    def __init__(self, valor):
        super().__init__(valor, "dinheiro")

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

    def mostrar_motivos(self):
        print("Motivos disponíveis:")
        for m in self.MOTIVOS_VALIDOS:
            print("-", m)

    def cancelar_corrida(self, motivo):
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