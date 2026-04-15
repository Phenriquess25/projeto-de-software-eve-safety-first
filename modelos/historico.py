"""
Classe Historico - Funcionalidade 7: Histórico de corridas
"""

from .usuario import Usuario
from .corrida import Corrida
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
