"""
Padrão Comportamental - Mediator
Centraliza a comunicação entre os componentes do sistema.
Reduz o acoplamento entre Passageiro, Motorista, Corrida, Pagamento e Suporte.
"""

from abc import ABC, abstractmethod
from typing import List, Optional, Dict
from datetime import datetime


# =========================
# INTERFACES PARA COMPONENTES
# =========================
class ComponenteCentral(ABC):
    """Interface para componentes que se comunicam através do mediador"""
    
    @abstractmethod
    def notificar(self, evento: str, dados: Dict) -> None:
        pass


# =========================
# MEDIATOR - CENTRAL DE CORRIDAS
# =========================
class CentralCorridas:
    """
    Mediator que centraliza a comunicação entre:
    - Passageiros
    - Motoristas
    - Corridas
    - Pagamentos
    - Suporte
    """
    
    def __init__(self):
        self.passageiros_registrados = []
        self.motoristas_registrados = []
        self.corridas_ativas: List[Dict] = []
        self.corridas_historico: List[Dict] = []
        self.motoristas_disponiveis = []
        self.mensagens_suporte: List[Dict] = []
        self.observadores = []
    
    # ===== GERENCIAMENTO DE USUÁRIOS =====
    
    def registrar_passageiro(self, passageiro) -> bool:
        """Registra um novo passageiro no sistema"""
        if passageiro not in self.passageiros_registrados:
            self.passageiros_registrados.append(passageiro)
            self._notificar_observadores("passageiro_registrado", {
                "passageiro": passageiro.nome_completo,
                "timestamp": datetime.now()
            })
            return True
        return False
    
    def registrar_motorista(self, motorista) -> bool:
        """Registra um novo motorista no sistema"""
        if motorista not in self.motoristas_registrados:
            self.motoristas_registrados.append(motorista)
            self.motoristas_disponiveis.append(motorista)
            self._notificar_observadores("motorista_registrado", {
                "motorista": motorista.nome_completo,
                "veiculo": motorista.modelo_veiculo,
                "timestamp": datetime.now()
            })
            return True
        return False
    
    # ===== GERENCIAMENTO DE CORRIDAS =====
    
    def solicitar_corrida(self, passageiro, origem: str, destino: str) -> Optional[Dict]:
        """
        Passageiro solicita uma corrida.
        Mediator busca motorista disponível.
        """
        if not self.motoristas_disponiveis:
            self._notificar_observadores("corrida_recusada", {
                "passageiro": passageiro.nome_completo,
                "motivo": "Nenhum motorista disponível",
                "timestamp": datetime.now()
            })
            print("❌ Nenhum motorista disponível no momento")
            return None
        
        # Buscar motorista (primeiro disponível)
        motorista = self.motoristas_disponiveis[0]
        
        # Criar corrida
        corrida_info = {
            "id_corrida": len(self.corridas_ativas) + 1,
            "passageiro": passageiro,
            "motorista": motorista,
            "origem": origem,
            "destino": destino,
            "status": "aceita",
            "valor": 0,
            "timestamp_inicio": datetime.now(),
            "timestamp_fim": None
        }
        
        self.corridas_ativas.append(corrida_info)
        self.motoristas_disponiveis.remove(motorista)
        
        self._notificar_observadores("corrida_aceita", {
            "passageiro": passageiro.nome_completo,
            "motorista": motorista.nome_completo,
            "origem": origem,
            "destino": destino,
            "id_corrida": corrida_info["id_corrida"],
            "timestamp": datetime.now()
        })
        
        print(f"✅ Corrida aceita! Motorista: {motorista.nome_completo}")
        return corrida_info
    
    def atualizar_preco_corrida(self, id_corrida: int, valor: float) -> bool:
        """Atualiza o preço da corrida no mediator"""
        for corrida in self.corridas_ativas:
            if corrida["id_corrida"] == id_corrida:
                corrida["valor"] = valor
                self._notificar_observadores("preco_atualizado", {
                    "id_corrida": id_corrida,
                    "valor": valor,
                    "timestamp": datetime.now()
                })
                return True
        return False
    
    def finalizar_corrida(self, id_corrida: int) -> Optional[Dict]:
        """Finaliza uma corrida ativa"""
        corrida_finalizada = None
        
        for corrida in self.corridas_ativas:
            if corrida["id_corrida"] == id_corrida:
                corrida["status"] = "finalizada"
                corrida["timestamp_fim"] = datetime.now()
                corrida_finalizada = corrida
                self.corridas_ativas.remove(corrida)
                self.corridas_historico.append(corrida)
                
                # Liberar motorista
                self.motoristas_disponiveis.append(corrida["motorista"])
                
                self._notificar_observadores("corrida_finalizada", {
                    "id_corrida": id_corrida,
                    "passageiro": corrida["passageiro"].nome_completo,
                    "motorista": corrida["motorista"].nome_completo,
                    "valor": corrida["valor"],
                    "timestamp": datetime.now()
                })
                break
        
        return corrida_finalizada
    
    def cancelar_corrida(self, id_corrida: int, motivo: str) -> bool:
        """Cancela uma corrida ativa"""
        for corrida in self.corridas_ativas:
            if corrida["id_corrida"] == id_corrida:
                corrida["status"] = "cancelada"
                self.corridas_ativas.remove(corrida)
                
                # Liberar motorista
                if corrida["motorista"] not in self.motoristas_disponiveis:
                    self.motoristas_disponiveis.append(corrida["motorista"])
                
                self._notificar_observadores("corrida_cancelada", {
                    "id_corrida": id_corrida,
                    "motorista": corrida["motorista"].nome_completo,
                    "motivo": motivo,
                    "timestamp": datetime.now()
                })
                
                print(f"❌ Corrida {id_corrida} cancelada: {motivo}")
                return True
        
        return False
    
    # ===== GERENCIAMENTO DE PAGAMENTOS =====
    
    def processar_pagamento(self, id_corrida: int, pagamento) -> bool:
        """Processa o pagamento de uma corrida"""
        for corrida in self.corridas_historico:
            if corrida["id_corrida"] == id_corrida:
                pagamento.processar_pagamento()
                
                self._notificar_observadores("pagamento_processado", {
                    "id_corrida": id_corrida,
                    "passageiro": corrida["passageiro"].nome_completo,
                    "valor": corrida["valor"],
                    "tipo_pagamento": pagamento.__class__.__name__,
                    "status": pagamento.status,
                    "timestamp": datetime.now()
                })
                
                print(f"✅ Pagamento de R${corrida['valor']:.2f} processado")
                return True
        
        return False
    
    # ===== GERENCIAMENTO DE SUPORTE =====
    
    def enviar_mensagem_suporte(self, usuario, mensagem: str) -> Dict:
        """Envia mensagem de suporte"""
        msg_info = {
            "id": len(self.mensagens_suporte) + 1,
            "usuario": usuario.nome_completo,
            "mensagem": mensagem,
            "status": "recebida",
            "timestamp": datetime.now()
        }
        
        self.mensagens_suporte.append(msg_info)
        
        self._notificar_observadores("mensagem_suporte_recebida", {
            "usuario": usuario.nome_completo,
            "mensagem": mensagem,
            "id_mensagem": msg_info["id"],
            "timestamp": datetime.now()
        })
        
        print(f"✅ Mensagem de suporte registrada (ID: {msg_info['id']})")
        return msg_info
    
    def responder_suporte(self, id_mensagem: int, resposta: str) -> bool:
        """Responde uma mensagem de suporte"""
        for msg in self.mensagens_suporte:
            if msg["id"] == id_mensagem:
                msg["status"] = "respondida"
                msg["resposta"] = resposta
                
                self._notificar_observadores("suporte_respondido", {
                    "usuario": msg["usuario"],
                    "resposta": resposta,
                    "id_mensagem": id_mensagem,
                    "timestamp": datetime.now()
                })
                
                return True
        
        return False
    
    # ===== OBSERVER PATTERN =====
    
    def registrar_observador(self, observador) -> None:
        """Registra um observador para eventos do sistema"""
        if observador not in self.observadores:
            self.observadores.append(observador)
    
    def remover_observador(self, observador) -> None:
        """Remove um observador do sistema"""
        if observador in self.observadores:
            self.observadores.remove(observador)
    
    def _notificar_observadores(self, evento: str, dados: Dict) -> None:
        """Notifica todos os observadores sobre um evento"""
        for observador in self.observadores:
            observador.notificar(evento, dados)
    
    # ===== CONSULTAS E RELATÓRIOS =====
    
    def obter_corrida_ativa(self, id_corrida: int) -> Optional[Dict]:
        """Busca uma corrida ativa pelo ID"""
        for corrida in self.corridas_ativas:
            if corrida["id_corrida"] == id_corrida:
                return corrida
        return None
    
    def obter_corridas_passageiro(self, passageiro) -> List[Dict]:
        """Retorna histórico de corridas do passageiro"""
        return [c for c in self.corridas_historico if c["passageiro"] == passageiro]
    
    def obter_corridas_motorista(self, motorista) -> List[Dict]:
        """Retorna histórico de corridas do motorista"""
        return [c for c in self.corridas_historico if c["motorista"] == motorista]
    
    def obter_motoristas_disponiveis(self) -> List:
        """Retorna lista de motoristas disponíveis"""
        return self.motoristas_disponiveis.copy()
    
    def obter_estatisticas(self) -> Dict:
        """Retorna estatísticas do sistema"""
        total_corridas = len(self.corridas_historico)
        valor_total = sum(c["valor"] for c in self.corridas_historico)
        
        return {
            "passageiros_registrados": len(self.passageiros_registrados),
            "motoristas_registrados": len(self.motoristas_registrados),
            "motoristas_disponiveis": len(self.motoristas_disponiveis),
            "corridas_ativas": len(self.corridas_ativas),
            "corridas_total": total_corridas,
            "valor_total": valor_total,
            "mensagens_suporte": len(self.mensagens_suporte),
            "timestamp": datetime.now()
        }


# =========================
# OBSERVADOR PADRÃO
# =========================
class ObservadorEventos(ComponenteCentral):
    """Observador que monitora eventos da central de corridas"""
    
    def __init__(self, nome: str = "Monitor"):
        self.nome = nome
        self.eventos_recebidos: List[Dict] = []
    
    def notificar(self, evento: str, dados: Dict) -> None:
        """Recebe notificação de um evento"""
        info_evento = {
            "evento": evento,
            "dados": dados,
            "timestamp": datetime.now()
        }
        self.eventos_recebidos.append(info_evento)
        self._exibir_evento(evento, dados)
    
    def _exibir_evento(self, evento: str, dados: Dict) -> None:
        """Exibe o evento de forma formatada"""
        print(f"\n📢 [{self.nome}] Evento: {evento}")
        for chave, valor in dados.items():
            if chave != "timestamp":
                print(f"   - {chave}: {valor}")
    
    def obter_historico_eventos(self) -> List[Dict]:
        """Retorna histórico de eventos recebidos"""
        return self.eventos_recebidos.copy()
    
    def contar_eventos(self, tipo_evento: str) -> int:
        """Conta ocorrências de um tipo específico de evento"""
        return sum(1 for e in self.eventos_recebidos if e["evento"] == tipo_evento)
