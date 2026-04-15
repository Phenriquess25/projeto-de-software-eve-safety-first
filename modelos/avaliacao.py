"""
Classe Avaliacao - Funcionalidade 8: Sistema de avaliação
"""

from .usuario import Usuario, Motorista

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
