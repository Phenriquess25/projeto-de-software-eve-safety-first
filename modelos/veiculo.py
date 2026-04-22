"""
Classe Veiculo - Funcionalidade 5 : Escolher tipo de veiculo
""" 

from abc import ABC, abstractmethod

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