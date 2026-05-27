"""
Padrão Estrutural - Decorator
Adiciona funcionalidades extras às corridas dinamicamente sem modificar a classe principal.
"""

from abc import ABC, abstractmethod


# =========================
# INTERFACE DE CORRIDA DECORADA
# =========================
class CorridaDecorada(ABC):
    """Interface para corridas e seus decoradores"""
    
    @abstractmethod
    def calcular_valor(self) -> float:
        pass
    
    @abstractmethod
    def obter_descricao(self) -> str:
        pass


# =========================
# CORRIDA SIMPLES (COMPONENTE)
# =========================
class CorridaSimples(CorridaDecorada):
    """Implementação concreta: corrida básica"""
    
    def __init__(self, valor_base: float):
        self.valor_base = valor_base
    
    def calcular_valor(self) -> float:
        return self.valor_base
    
    def obter_descricao(self) -> str:
        return f"Corrida básica: R${self.valor_base:.2f}"


# =========================
# DECORADORES
# =========================
class DecoradorCorrida(CorridaDecorada):
    """Classe base para decoradores"""
    
    def __init__(self, corrida: CorridaDecorada):
        self.corrida = corrida
    
    def calcular_valor(self) -> float:
        return self.corrida.calcular_valor()
    
    def obter_descricao(self) -> str:
        return self.corrida.obter_descricao()


class CorridaVIP(DecoradorCorrida):
    """Decorador: adiciona funcionalidades VIP"""
    
    def __init__(self, corrida: CorridaDecorada, taxa_vip: float = 50.0):
        super().__init__(corrida)
        self.taxa_vip = taxa_vip
    
    def calcular_valor(self) -> float:
        return self.corrida.calcular_valor() + self.taxa_vip
    
    def obter_descricao(self) -> str:
        return f"{self.corrida.obter_descricao()} + VIP (R${self.taxa_vip:.2f})"


class PrioridadeAtendimento(DecoradorCorrida):
    """Decorador: adiciona prioridade de atendimento"""
    
    def __init__(self, corrida: CorridaDecorada, taxa_prioridade: float = 15.0):
        super().__init__(corrida)
        self.taxa_prioridade = taxa_prioridade
    
    def calcular_valor(self) -> float:
        return self.corrida.calcular_valor() + self.taxa_prioridade
    
    def obter_descricao(self) -> str:
        return f"{self.corrida.obter_descricao()} + Prioridade (R${self.taxa_prioridade:.2f})"


class SeguroAdicional(DecoradorCorrida):
    """Decorador: adiciona seguro adicional"""
    
    def __init__(self, corrida: CorridaDecorada, taxa_seguro: float = 20.0):
        super().__init__(corrida)
        self.taxa_seguro = taxa_seguro
    
    def calcular_valor(self) -> float:
        return self.corrida.calcular_valor() + self.taxa_seguro
    
    def obter_descricao(self) -> str:
        return f"{self.corrida.obter_descricao()} + Seguro (R${self.taxa_seguro:.2f})"


class TaxaExtra(DecoradorCorrida):
    """Decorador: adiciona taxa extra (pico de demanda)"""
    
    def __init__(self, corrida: CorridaDecorada, taxa_extra: float = 10.0):
        super().__init__(corrida)
        self.taxa_extra = taxa_extra
    
    def calcular_valor(self) -> float:
        return self.corrida.calcular_valor() + self.taxa_extra
    
    def obter_descricao(self) -> str:
        return f"{self.corrida.obter_descricao()} + Taxa Extra (R${self.taxa_extra:.2f})"


class Promocao(DecoradorCorrida):
    """Decorador: aplica desconto por promoção"""
    
    def __init__(self, corrida: CorridaDecorada, desconto_percentual: float = 0.15):
        super().__init__(corrida)
        self.desconto_percentual = desconto_percentual
    
    def calcular_valor(self) -> float:
        valor_original = self.corrida.calcular_valor()
        desconto = valor_original * self.desconto_percentual
        return valor_original - desconto
    
    def obter_descricao(self) -> str:
        desconto_pct = int(self.desconto_percentual * 100)
        return f"{self.corrida.obter_descricao()} - Promoção ({desconto_pct}% OFF)"


# =========================
# CONSTRUTOR DE CORRIDA (FLUENT API)
# =========================
class ConstrutorCorrida:
    """Facilita a construção de corridas com decoradores"""
    
    def __init__(self, valor_base: float):
        self.corrida = CorridaSimples(valor_base)
    
    def adicionar_vip(self, taxa: float = 50.0) -> 'ConstrutorCorrida':
        self.corrida = CorridaVIP(self.corrida, taxa)
        return self
    
    def adicionar_prioridade(self, taxa: float = 15.0) -> 'ConstrutorCorrida':
        self.corrida = PrioridadeAtendimento(self.corrida, taxa)
        return self
    
    def adicionar_seguro(self, taxa: float = 20.0) -> 'ConstrutorCorrida':
        self.corrida = SeguroAdicional(self.corrida, taxa)
        return self
    
    def adicionar_taxa_extra(self, taxa: float = 10.0) -> 'ConstrutorCorrida':
        self.corrida = TaxaExtra(self.corrida, taxa)
        return self
    
    def aplicar_promocao(self, desconto: float = 0.15) -> 'ConstrutorCorrida':
        self.corrida = Promocao(self.corrida, desconto)
        return self
    
    def obter_corrida(self) -> CorridaDecorada:
        return self.corrida
    
    def obter_valor_final(self) -> float:
        return self.corrida.calcular_valor()
    
    def obter_descricao(self) -> str:
        return self.corrida.obter_descricao()
