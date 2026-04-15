"""
Classe Corrida - Funcionalidade 3: Solicitar uma corrida
""" 

import uuid
import random
from .usuario import Passageiro
from .veiculo import Veiculo 

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
