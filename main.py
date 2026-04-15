from modelos.usuario import Passageiro, Motorista
from modelos.sessao import Login
from modelos.corrida import Corrida
from modelos.veiculo import Carro, Moto, VeiculoVIP
from modelos.pagamento import PagamentoPix, PagamentoCartao, PagamentoDinheiro
from modelos.historico import Historico
from modelos.avaliacao import Avaliacao
from modelos.controle_cancelamento import ControleCancelamento
from modelos.suporte import Suporte
from datetime import date

print("\n============================")
print("      TESTE COMPLETO")
print("============================\n")

# =========================
# 1. CRIAÇÃO DE USUÁRIOS
# =========================
passageiro = Passageiro(
    "Isaac",
    "52998224725",  # CPF válido
    "isaac@test.com",
    "1234",
    "9999"
)

motorista = Motorista(
    "João Silva",
    "12345678909",
    "joao@email.com", 
    "senha123",
    "11999999999",
    "59090100108",  # CNH valida
    "ABC1234",
    "Toyota Corolla"
)

print("\n--- Cadastro ---")
passageiro.cadastrar()
motorista.cadastrar()

# =========================
# 2. VALIDAÇÃO + CONFIRMAÇÃO
# =========================
print("\n--- Validação ---")

if passageiro.validar_documentos():
    passageiro.confirmar_conta()

if motorista.validar_documentos():
    motorista.confirmar_conta()
else:
    print("Motorista não pode ser confirmado")

# =========================
# 3. DADOS
# =========================
print("\n--- Dados ---")
passageiro.mostrar_dados()
motorista.mostrar_dados()

# =========================
# 4. LOGIN
# =========================
print("\n--- Login ---")
login = Login(passageiro)
login.autenticar("isaac@test.com", "1234")

# =========================
# 5. CORRIDA
# =========================
print("\n--- Corrida ---")
corrida = Corrida(passageiro, "Casa", "Centro")

veiculo = Carro()
motorista.cadastrar_veiculo(veiculo)

corrida.escolher_veiculo(veiculo)
corrida.calcular_preco()
corrida.confirmar()

print(f"Status da corrida: {corrida.status}")

# =========================
# 6. PAGAMENTO
# =========================
print("\n--- Pagamento ---")
pagamento = PagamentoPix(corrida.valor)
pagamento.processar_pagamento()
pagamento.mostrar_status()

# =========================
# 7. HISTÓRICO
# =========================
print("\n--- Histórico ---")
historico = Historico(passageiro)
historico.adicionar(corrida)
historico.visualizar()

# =========================
# 8. AVALIAÇÃO
# =========================
print("\n--- Avaliação ---")
avaliacao = Avaliacao(passageiro, motorista, 5, "Excelente motorista!")
avaliacao.avaliar()

# =========================
# 9. CANCELAMENTO
# =========================
print("\n--- Cancelamento ---")
controle = ControleCancelamento(2)

controle.mostrar_motivos()

controle.cancelar_corrida("")  # erro
controle.cancelar_corrida("Fome")  # inválido
controle.cancelar_corrida("Problema no carro")  # ok
controle.cancelar_corrida("Emergência")  # ok
controle.cancelar_corrida("Trânsito extremo")  # limite atingido

controle.data_atual = date(2026, 1, 1)

controle.cancelar_corrida("Emergência")  # ok

# =========================
# 10. SUPORTE
# =========================
print("\n--- Suporte ---")
suporte = Suporte(passageiro)
suporte.enviar("Tive um problema na corrida")
suporte.historico()

# =========================
# 11. POLIMORFISMO PAGAMENTO
# =========================
print("\n--- Polimorfismo Pagamento ---")

pagamentos = [
    PagamentoPix(50),
    PagamentoCartao(100),
    PagamentoDinheiro(30)
]

for p in pagamentos:
    p.processar_pagamento()
    p.mostrar_status()
    print()

# =========================
# 12. POLIMORFISMO VEÍCULO 
# =========================
print("\n--- Polimorfismo Veículo ---")

veiculos = [Moto(), Carro(), VeiculoVIP()]

for v in veiculos:
    corrida.escolher_veiculo(v)
    corrida.calcular_preco()
