"""
Classe Rastreamento - Funcionalidade 4: Visualização do motorista no mapa
""" 

from .corrida import Corrida

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
