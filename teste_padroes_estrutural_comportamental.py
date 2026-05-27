"""
Script de Teste - Padrões Estrutural e Comportamental
Demonstra o uso do Decorator e do Mediator Pattern
"""

print("\n" + "="*80)
print("  🎨 PADRÕES ESTRUTURAL E COMPORTAMENTAL - EVE SAFETY FIRST")
print("="*80)

# ===========================
# 1. DEMONSTRAÇÃO DO DECORATOR
# ===========================
print("\n\n" + "="*80)
print("  1️⃣  PADRÃO ESTRUTURAL - DECORATOR")
print("="*80)

from modelos.decorador_corrida import (
    CorridaSimples,
    CorridaVIP,
    PrioridadeAtendimento,
    SeguroAdicional,
    TaxaExtra,
    Promocao,
    ConstrutorCorrida
)

print("\n📋 Demonstração: Criando corridas com diferentes decoradores\n")

# Exemplo 1: Corrida simples
print("✅ 1.1 - Corrida Simples")
corrida1 = CorridaSimples(valor_base=50.0)
print(f"   {corrida1.obter_descricao()}")
print(f"   Valor final: R${corrida1.calcular_valor():.2f}")

# Exemplo 2: Corrida com VIP
print("\n✅ 1.2 - Corrida com VIP")
corrida2 = CorridaVIP(CorridaSimples(50.0))
print(f"   {corrida2.obter_descricao()}")
print(f"   Valor final: R${corrida2.calcular_valor():.2f}")

# Exemplo 3: Corrida com múltiplos decoradores
print("\n✅ 1.3 - Corrida com VIP + Prioridade + Seguro")
corrida3 = SeguroAdicional(
    PrioridadeAtendimento(
        CorridaVIP(CorridaSimples(50.0))
    )
)
print(f"   {corrida3.obter_descricao()}")
print(f"   Valor final: R${corrida3.calcular_valor():.2f}")

# Exemplo 4: Usando construtor fluente (melhor legibilidade)
print("\n✅ 1.4 - Corrida Premium (usando construtor fluente)")
corrida4 = (ConstrutorCorrida(50.0)
    .adicionar_vip()
    .adicionar_prioridade()
    .adicionar_seguro()
    .adicionar_taxa_extra())

print(f"   {corrida4.obter_descricao()}")
print(f"   Valor final: R${corrida4.obter_valor_final():.2f}")

# Exemplo 5: Corrida com promoção
print("\n✅ 1.5 - Corrida com Promoção (15% OFF)")
corrida5 = Promocao(
    SeguroAdicional(
        CorridaVIP(CorridaSimples(100.0))
    ),
    desconto_percentual=0.15
)
print(f"   {corrida5.obter_descricao()}")
print(f"   Valor final: R${corrida5.calcular_valor():.2f}")

# Exemplo 6: Comparação de preços
print("\n✅ 1.6 - Comparação de Preços")
print(f"   Simples:                   R${CorridaSimples(50).calcular_valor():.2f}")
print(f"   + VIP:                     R${CorridaVIP(CorridaSimples(50)).calcular_valor():.2f}")
print(f"   + VIP + Prioridade:        R${PrioridadeAtendimento(CorridaVIP(CorridaSimples(50))).calcular_valor():.2f}")
print(f"   + VIP + Seguro:            R${SeguroAdicional(CorridaVIP(CorridaSimples(50))).calcular_valor():.2f}")
print(f"   + Tudo (Premium):          R${ConstrutorCorrida(50).adicionar_vip().adicionar_prioridade().adicionar_seguro().adicionar_taxa_extra().obter_valor_final():.2f}")

print("\n✨ VANTAGENS DO DECORATOR:")
print("   ✓ Adiciona funcionalidades sem modificar classes existentes")
print("   ✓ Combina decoradores dinamicamente")
print("   ✓ Reduz duplicação de código")
print("   ✓ Facilita manutenção e expansão")
print("   ✓ Permite criação de combinações complexas")


# ===========================
# 2. DEMONSTRAÇÃO DO MEDIATOR
# ===========================
print("\n\n" + "="*80)
print("  2️⃣  PADRÃO COMPORTAMENTAL - MEDIATOR")
print("="*80)

from modelos.mediador_corridas import CentralCorridas, ObservadorEventos
from modelos.usuario import Passageiro, Motorista
from modelos.veiculo import Carro
from modelos.pagamento import PagamentoPix

print("\n📋 Demonstração: Centralização de comunicação entre componentes\n")

# Criar mediator (central de corridas)
central = CentralCorridas()

# Criar observador para monitorar eventos
monitor = ObservadorEventos(nome="Monitor Principal")
central.registrar_observador(monitor)

# Criar usuários
print("✅ 2.1 - Registrando Usuários no Sistema\n")

passageiro1 = Passageiro(
    nome_completo="Maria Silva",
    cpf="12345678901",
    email="maria@email.com",
    senha="senha123",
    telefone="11999999999"
)

passageiro2 = Passageiro(
    nome_completo="João Santos",
    cpf="98765432101",
    email="joao@email.com",
    senha="senha456",
    telefone="11988888888"
)

motorista1 = Motorista(
    nome_completo="Carlos Souza",
    cpf="11111111111",
    email="carlos@email.com",
    senha="senha789",
    telefone="11977777777",
    cnh="987654321",
    placa="ABC1234",
    modelo_veiculo="Carro"
)

motorista2 = Motorista(
    nome_completo="Paulo Oliveira",
    cpf="22222222222",
    email="paulo@email.com",
    senha="senha101",
    telefone="11966666666",
    cnh="123456789",
    placa="XYZ5678",
    modelo_veiculo="Moto"
)

central.registrar_passageiro(passageiro1)
central.registrar_passageiro(passageiro2)
central.registrar_motorista(motorista1)
central.registrar_motorista(motorista2)

# Solicitar corrida
print("\n\n✅ 2.2 - Solicitando Corrida\n")
corrida_info = central.solicitar_corrida(passageiro1, "Aeroporto", "Centro")

if corrida_info:
    id_corrida = corrida_info["id_corrida"]
    
    # Atualizar preço
    print("\n\n✅ 2.3 - Atualizando Preço da Corrida\n")
    central.atualizar_preco_corrida(id_corrida, 75.50)
    
    # Finalizar corrida
    print("\n\n✅ 2.4 - Finalizando Corrida\n")
    corrida_finalizada = central.finalizar_corrida(id_corrida)
    
    if corrida_finalizada:
        # Processar pagamento
        print("\n\n✅ 2.5 - Processando Pagamento\n")
        pagamento = PagamentoPix(corrida_finalizada["valor"])
        central.processar_pagamento(id_corrida, pagamento)

# Enviar mensagem de suporte
print("\n\n✅ 2.6 - Enviando Mensagem de Suporte\n")
central.enviar_mensagem_suporte(passageiro1, "Tive um problema com o troco")

print("\n\n✅ 2.7 - Respondendo Mensagem de Suporte\n")
central.responder_suporte(1, "Desculpe! Vamos resolver seu problema em breve.")

# Solicitar segunda corrida
print("\n\n✅ 2.8 - Solicitando Segunda Corrida\n")
corrida_info2 = central.solicitar_corrida(passageiro2, "Estação Central", "Hospital")

if corrida_info2:
    central.atualizar_preco_corrida(corrida_info2["id_corrida"], 45.00)
    central.finalizar_corrida(corrida_info2["id_corrida"])

# Exibir estatísticas
print("\n\n✅ 2.9 - Estatísticas do Sistema\n")
stats = central.obter_estatisticas()
print(f"   Passageiros registrados:    {stats['passageiros_registrados']}")
print(f"   Motoristas registrados:     {stats['motoristas_registrados']}")
print(f"   Motoristas disponíveis:     {stats['motoristas_disponiveis']}")
print(f"   Corridas ativas:            {stats['corridas_ativas']}")
print(f"   Corridas total:             {stats['corridas_total']}")
print(f"   Valor total em corridas:    R${stats['valor_total']:.2f}")
print(f"   Mensagens de suporte:       {stats['mensagens_suporte']}")

print("\n✨ VANTAGENS DO MEDIATOR:")
print("   ✓ Reduz acoplamento entre classes")
print("   ✓ Centraliza regras de comunicação")
print("   ✓ Facilita manutenção do sistema")
print("   ✓ Simplifica futuras expansões")
print("   ✓ Evita dependências diretas excessivas")

# Exibir eventos monitorados
print("\n\n✅ 2.10 - Eventos Monitorados\n")
print(f"   Total de eventos recebidos: {len(monitor.obter_historico_eventos())}")
print(f"   Corridas aceitas:           {monitor.contar_eventos('corrida_aceita')}")
print(f"   Corridas finalizadas:       {monitor.contar_eventos('corrida_finalizada')}")
print(f"   Pagamentos processados:     {monitor.contar_eventos('pagamento_processado')}")
print(f"   Mensagens de suporte:       {monitor.contar_eventos('mensagem_suporte_recebida')}")


# ===========================
# 3. COMBINANDO OS PADRÕES
# ===========================
print("\n\n" + "="*80)
print("  3️⃣  COMBINANDO DECORATOR + MEDIATOR")
print("="*80)

print("\n📋 Demonstração: Usando decorator com mediator para corridas premium\n")

# Criar corrida com decoradores
print("✅ 3.1 - Criando Corrida Premium com Decoradores\n")

corrida_premium = (ConstrutorCorrida(100.0)
    .adicionar_vip()
    .adicionar_seguro()
    .aplicar_promocao(desconto=0.10))

print(f"   {corrida_premium.obter_descricao()}")
print(f"   Valor final: R${corrida_premium.obter_valor_final():.2f}")

# Atualizar sistema
print("\n\n✅ 3.2 - Atualizando Mediator com Corrida Premium\n")
print(f"   💳 Preço da corrida premium registrado no sistema")

print("\n\n" + "="*80)
print("  ✅ DEMONSTRAÇÃO COMPLETA - PADRÕES ESTRUTURAL E COMPORTAMENTAL")
print("="*80 + "\n")
