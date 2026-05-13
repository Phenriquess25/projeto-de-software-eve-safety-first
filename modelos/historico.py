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
        self._carregar_do_banco()  # Carrega corridas salvas do banco
    
    def _carregar_do_banco(self):
        """Carrega o histórico de corridas do banco de dados"""
        try:
            from bancos_dados.corridas_bd import listar_corridas_passageiro
            corridas_salvas = listar_corridas_passageiro(self.usuario.id_usuario)
            self.corridas = corridas_salvas
        except Exception as e:
            print(f"Aviso: Não foi possível carregar histórico: {e}")
            self.corridas = []

    def adicionar(self, corrida: Corrida):
        """Adiciona uma corrida ao histórico"""
        self.corridas.append(corrida)

    def visualizar(self):
        """Exibe o histórico de corridas"""
        print(f"\n{'='*50}")
        print(f"  HISTÓRICO DE {self.usuario.nome_completo.upper()}")
        print(f"{'='*50}")
        
        if not self.corridas:
            print("\n  Nenhuma corrida registrada ainda.")
        else:
            print(f"\n  Total de corridas: {len(self.corridas)}\n")
            for i, corrida in enumerate(self.corridas, 1):
                if isinstance(corrida, dict):
                    # Corrida vinda do banco (dicionário)
                    print(f"  {i}. {corrida.get('origem')} → {corrida.get('destino')}")
                    print(f"     Veículo: {corrida.get('tipo_veiculo')} | Status: {corrida.get('status')}")
                    print(f"     Valor: R${corrida.get('valor', 0):.2f} | Distância: {corrida.get('distancia', 0)}km")
                else:
                    # Corrida vinda da memória (objeto)
                    print(f"  {i}. {corrida.origem} → {corrida.destino}")
                    print(f"     Veículo: {corrida.veiculo.tipo if corrida.veiculo else 'N/A'} | Status: {corrida.status}")
                    print(f"     Valor: R${corrida.valor:.2f} | Distância: {corrida.distancia}km")
                print()
        
        print(f"{'='*50}")
