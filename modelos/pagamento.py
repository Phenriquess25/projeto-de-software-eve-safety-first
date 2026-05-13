"""
Classe Pagamento - Funcionalidade 6: Sistema de pagamento
""" 

from abc import ABC, abstractmethod 

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
# PAGAMENTO FACTORY (PADRÃO CRIACIONAL)
# =========================
class PagamentoFactory:
    """
    Factory Method para criar instâncias de Pagamentos.
    Centraliza a lógica de criação de diferentes formas de pagamento.
    """
    
    @staticmethod
    def criar(tipo_pagamento: str, valor: float) -> Pagamento:
        """
        Cria e retorna um pagamento do tipo especificado.
        
        Args:
            tipo_pagamento (str): Tipo de pagamento ('pix', 'cartao', 'dinheiro')
            valor (float): Valor do pagamento
            
        Returns:
            Pagamento: Instância do pagamento solicitado
            
        Raises:
            ValueError: Se o tipo de pagamento não for reconhecido
        """
        tipo_pagamento = tipo_pagamento.lower().strip()
        
        if tipo_pagamento == "pix":
            return PagamentoPix(valor)
        elif tipo_pagamento == "cartao":
            return PagamentoCartao(valor)
        elif tipo_pagamento == "dinheiro":
            return PagamentoDinheiro(valor)
        else:
            raise ValueError(f"Tipo de pagamento '{tipo_pagamento}' não reconhecido. Use 'pix', 'cartao' ou 'dinheiro'.")

