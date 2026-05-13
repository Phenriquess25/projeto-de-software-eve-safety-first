"""
Teste de Extensibilidade - Factory Method Pattern
Demonstra como adicionar novos tipos de veículos e pagamentos é trivial
"""

from modelos.veiculo import Veiculo, VeiculoFactory
from modelos.pagamento import Pagamento, PagamentoFactory

print("\n" + "="*60)
print("   DEMONSTRAÇÃO - FACTORY METHOD PATTERN")
print("="*60 + "\n")

# =========================
# 1. USANDO VEÍCULOS COM FACTORY
# =========================
print("1️⃣  CRIANDO VEÍCULOS COM FACTORY\n")

tipos_veiculos = ["moto", "carro", "vip"]

for tipo in tipos_veiculos:
    veiculo = VeiculoFactory.criar(tipo)
    tarifa = veiculo.calcular_tarifa(10)  # 10 km
    print(f"   {tipo.upper()}: R${tarifa:.2f} (para 10 km)")

print()

# =========================
# 2. USANDO PAGAMENTOS COM FACTORY
# =========================
print("2️⃣  CRIANDO PAGAMENTOS COM FACTORY\n")

pagamentos_dados = [
    ("pix", 100),
    ("cartao", 250),
    ("dinheiro", 50)
]

for tipo, valor in pagamentos_dados:
    pagamento = PagamentoFactory.criar(tipo, valor)
    print(f"\n   Processando {tipo.upper()}...")
    pagamento.processar_pagamento()
    pagamento.mostrar_status()

print()

# =========================
# 3. TRATAMENTO DE ERROS
# =========================
print("3️⃣  TRATAMENTO DE ERROS\n")

try:
    print("   Tentando criar veículo inválido...")
    veiculo = VeiculoFactory.criar("helicoptero")
except ValueError as e:
    print(f"   ❌ Erro capturado: {e}")

try:
    print("\n   Tentando criar pagamento inválido...")
    pagamento = PagamentoFactory.criar("bitcoin", 100)
except ValueError as e:
    print(f"   ❌ Erro capturado: {e}")

print()

# =========================
# 4. BENEFÍCIOS DO PADRÃO
# =========================
print("4️⃣  BENEFÍCIOS DO FACTORY METHOD\n")

print("   ✅ Desacoplamento: Código cliente não conhece classes concretas")
print("   ✅ Centralização: Toda criação em um único lugar")
print("   ✅ Escalabilidade: Adicionar novo tipo é trivial")
print("   ✅ Validação: Erros capturados na factory")
print("   ✅ Manutenção: Mudanças afetam apenas a factory")

print()

# =========================
# 5. COMO ESTENDER
# =========================
print("5️⃣  COMO ADICIONAR NOVOS TIPOS\n")

print("""
   Para adicionar NOVO VEÍCULO (ex: Bicicleta):
   
   1. Criar classe no modelos/veiculo.py:
      
      class Bicicleta(Veiculo):
          def __init__(self):
              super().__init__("Bicicleta")
          def calcular_tarifa(self, distancia):
              return distancia * 0.5
   
   2. Adicionar à factory:
      
      elif tipo_veiculo == "bicicleta":
          return Bicicleta()
   
   3. Usar em qualquer lugar:
      
      bicicleta = VeiculoFactory.criar("bicicleta")

   ✨ Nenhuma mudança necessária em outro código!
""")

print("="*60 + "\n")
