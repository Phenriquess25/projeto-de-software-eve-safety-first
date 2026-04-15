"""
Classe Veiculo - Funcionalidade 5 : Escolher tipo de veiculo
""" 

# =========================
# 5. VEICULO (HERANÇA E POLIMORFISMO)
# =========================
class Veiculo:
    def __init__(self, tipo):
        self.tipo = tipo

    def calcular_tarifa(self, distancia):
        raise NotImplementedError("Subclasse deve implementar")

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
