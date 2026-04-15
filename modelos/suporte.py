"""
Classe Suporte - Funcionalidade 10: Suporte ao cliente
""" 

from .usuario import Usuario

# =========================
# 10. SUPORTE
# =========================
class Suporte:
    def __init__(self, usuario: Usuario):
        self.usuario = usuario
        self.mensagens = []

    def enviar(self, mensagem):
        self.mensagens.append(mensagem)
        print("Mensagem enviada ao suporte")

    def historico(self):
        print("Mensagens:")
        for m in self.mensagens:
            print("-", m)
