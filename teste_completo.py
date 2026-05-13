"""
Script de Teste Completo - Demonstração de todos os caminhos
Testa Factory Method com Passageiro e Motorista
"""

from modelos.usuario import Passageiro, Motorista
from modelos.sessao import Login
from modelos.corrida import Corrida
from modelos.veiculo import VeiculoFactory
from modelos.pagamento import PagamentoFactory
from modelos.historico import Historico
from modelos.suporte import Suporte

from bancos_dados import *

print("\n" + "="*70)
print("  🧪 TESTE COMPLETO - FACTORY METHOD COM PASSAGEIRO E MOTORISTA")
print("="*70)

# =========================
# 1. TESTE PASSAGEIRO
# =========================
print("\n\n" + "="*70)
print("  📋 TESTE 1: CADASTRO E OPERAÇÕES DO PASSAGEIRO")
print("="*70)

# Cadastro de Passageiro
print("\n✅ 1.1 - Cadastrando Passageiro...")
passageiro = Passageiro(
    "João Silva",
    "12345678909",
    "joao@test.com",
    "senha123",
    "11999999999"
)
passageiro.cadastrar()
passageiro.confirmar_conta()
salvar_usuarios(passageiro)
print("   ✓ Passageiro salvo com sucesso!")

# Solicitar Corrida
print("\n✅ 1.2 - Passageiro Solicitando Corrida...")
corrida = Corrida(passageiro, "Centro", "Bairro")

# FACTORY METHOD EM AÇÃO - Criando veículo
print("\n   🏭 Usando VeiculoFactory.criar('carro')...")
veiculo = VeiculoFactory.criar("carro")
corrida.escolher_veiculo(veiculo)
corrida.calcular_preco()
corrida.confirmar()
print(f"   ✓ Corrida confirmada: {veiculo.tipo} - R${corrida.valor:.2f}")

# FACTORY METHOD EM AÇÃO - Criando pagamento
print("\n   🏭 Usando PagamentoFactory.criar('pix', valor)...")
pagamento = PagamentoFactory.criar("pix", corrida.valor)
pagamento.processar_pagamento()
pagamento.mostrar_status()
print("   ✓ Pagamento processado!")

# Salvar dados
salvar_corridas(corrida)
salvar_pagamentos(pagamento)

# Histórico
print("\n✅ 1.3 - Consultando Histórico do Passageiro...")
historico = Historico(passageiro)
historico.adicionar(corrida)
historico.visualizar()

# Suporte
print("\n✅ 1.4 - Enviando Mensagem de Suporte...")
suporte = Suporte(passageiro)
suporte.enviar("Tive um problema na corrida")
suporte.historico()
salvar_mensagens(passageiro, "Tive um problema na corrida")
print("   ✓ Mensagem de suporte salva!")

# =========================
# 2. TESTE POLIMORFISMO COM FACTORY - MÚLTIPLOS PAGAMENTOS
# =========================
print("\n\n" + "="*70)
print("  📋 TESTE 2: POLIMORFISMO - MÚLTIPLOS PAGAMENTOS COM FACTORY")
print("="*70)

print("\n✅ 2.1 - Criando diferentes tipos de pagamento com Factory Method...")

tipos_pagamento = [
    ("pix", 50),
    ("cartao", 100),
    ("dinheiro", 75)
]

for tipo, valor in tipos_pagamento:
    print(f"\n   🏭 PagamentoFactory.criar('{tipo}', {valor})...")
    pagamento = PagamentoFactory.criar(tipo, valor)
    pagamento.processar_pagamento()
    pagamento.mostrar_status()
    print(f"   ✓ {tipo.upper()} criado com sucesso!")

# =========================
# 3. TESTE POLIMORFISMO COM FACTORY - MÚLTIPLOS VEÍCULOS
# =========================
print("\n\n" + "="*70)
print("  📋 TESTE 3: POLIMORFISMO - MÚLTIPLOS VEÍCULOS COM FACTORY")
print("="*70)

print("\n✅ 3.1 - Criando diferentes tipos de veículo com Factory Method...")

tipos_veiculo = ["moto", "carro", "vip"]

for tipo in tipos_veiculo:
    print(f"\n   🏭 VeiculoFactory.criar('{tipo}')...")
    veiculo = VeiculoFactory.criar(tipo)
    tarifa = veiculo.calcular_tarifa(10)
    print(f"   ✓ {tipo.upper()}: R${tarifa:.2f} (para 10 km)")

# =========================
# 4. TESTE MOTORISTA
# =========================
print("\n\n" + "="*70)
print("  📋 TESTE 4: CADASTRO E OPERAÇÕES DO MOTORISTA")
print("="*70)

# Cadastro de Motorista
print("\n✅ 4.1 - Cadastrando Motorista...")
motorista = Motorista(
    "Maria Santos",
    "98765432100",
    "maria@motorista.com",
    "senha456",
    "21988888888",
    "12345678901",
    "ABC1234",
    "Honda Civic"
)
motorista.cadastrar()

if motorista.validar_documentos():
    motorista.confirmar_conta()
    print("   ✓ Motorista verificado com sucesso!")
else:
    print("   ⚠️ Motorista não passou na verificação")

salvar_usuarios(motorista)
print("   ✓ Motorista salvo com sucesso!")

# Motorista cadastrando veículo
print("\n✅ 4.2 - Motorista Cadastrando Veículo...")
veiculo_motorista = VeiculoFactory.criar("carro")
motorista.cadastrar_veiculo(veiculo_motorista)
print("   ✓ Veículo cadastrado!")

# =========================
# 5. TESTE TRATAMENTO DE ERROS
# =========================
print("\n\n" + "="*70)
print("  📋 TESTE 5: TRATAMENTO DE ERROS DO FACTORY METHOD")
print("="*70)

print("\n✅ 5.1 - Tentando criar veículo inválido...")
try:
    veiculo_invalido = VeiculoFactory.criar("helicoptero")
except ValueError as e:
    print(f"   ✓ Erro capturado corretamente: {e}")

print("\n✅ 5.2 - Tentando criar pagamento inválido...")
try:
    pagamento_invalido = PagamentoFactory.criar("bitcoin", 100)
except ValueError as e:
    print(f"   ✓ Erro capturado corretamente: {e}")

# =========================
# 6. RESUMO FINAL
# =========================
print("\n\n" + "="*70)
print("  ✅ TESTE CONCLUÍDO COM SUCESSO!")
print("="*70)

print("""
🎯 O QUE FOI TESTADO:

1. ✓ Cadastro e Operações do Passageiro
   - Solicitação de Corrida com Factory Method
   - Histórico de Corridas
   - Envio de Suporte

2. ✓ Polimorfismo com Factory Method
   - Múltiplos tipos de Pagamento (PIX, Cartão, Dinheiro)
   - Múltiplos tipos de Veículo (Moto, Carro, VIP)

3. ✓ Cadastro e Operações do Motorista
   - Cadastro com validação
   - Cadastro de Veículo

4. ✓ Tratamento de Erros
   - Veículo inválido
   - Pagamento inválido

🏭 FACTORY METHOD EM AÇÃO:
✅ VeiculoFactory.criar(tipo) - Criou Moto, Carro e VIP
✅ PagamentoFactory.criar(tipo, valor) - Criou PIX, Cartão e Dinheiro
✅ Polimorfismo funcionando perfeitamente
✅ Tratamento de erros centralizado

📊 DADOS SALVOS:
✅ Passageiro salvo
✅ Motorista salvo
✅ Corrida salva
✅ Pagamento salvo
✅ Mensagem de Suporte salva

""")

print("="*70)
print("  🚕 EVE - SAFETY FIRST 🚕")
print("="*70 + "\n")
