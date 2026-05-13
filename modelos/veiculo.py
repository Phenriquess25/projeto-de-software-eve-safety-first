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


# =========================
# VEICULO FACTORY (PADRÃO CRIACIONAL)
# =========================
class VeiculoFactory:
    """
    Factory Method para criar instâncias de Veículos.
    Centraliza a lógica de criação de diferentes tipos de veículos.
    """
    
    @staticmethod
    def criar(tipo_veiculo: str) -> Veiculo:
        """
        Cria e retorna um veículo do tipo especificado.
        
        Args:
            tipo_veiculo (str): Tipo de veículo ('moto', 'carro', 'vip')
            
        Returns:
            Veiculo: Instância do veículo solicitado
            
        Raises:
            ValueError: Se o tipo de veículo não for reconhecido
        """
        tipo_veiculo = tipo_veiculo.lower().strip()
        
        if tipo_veiculo == "moto":
            return Moto()
        elif tipo_veiculo == "carro":
            return Carro()
        elif tipo_veiculo == "vip":
            return VeiculoVIP()
        else:
            raise ValueError(f"Tipo de veículo '{tipo_veiculo}' não reconhecido. Use 'moto', 'carro' ou 'vip'.")