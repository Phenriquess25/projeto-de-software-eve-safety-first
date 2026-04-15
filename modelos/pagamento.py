"""
Classe Pagamento - Funcionalidade 6: Sistema de pagamento
""" 

# =========================
# 6. PAGAMENTO (HERANÇA E POLIMORFISMO)
# =========================
class Pagamento:
    def __init__(self, valor):
        self.valor = valor
        self.status = "pendente"

    def processar_pagamento(self):
        raise NotImplementedError

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
