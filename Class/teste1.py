from classes import *


# =========================
# TESTE
# =========================

#USUARIO
passageiro = Passageiro("Isaac", "123", "isaac@test.com", "1234", "9999")
motorista = Motorista(
    "João",
    "456",
    "joao@test.com",
    "abcd",
    "8888",
    "CNH123",
    "ABC-1234",
    "Toyota Corolla"
)

print("\n--- Cadastro ---")
passageiro.cadastrar()
motorista.cadastrar()

passageiro.confirmar_conta()
motorista.confirmar_conta()

print("\n--- Dados ---")
passageiro.mostrar_dados()
motorista.mostrar_dados()

# Login
print("\n--- Login ---")
login = Login(passageiro)
login.autenticar("isaac@test.com", "1234")

# Criar corrida
print("\n--- Corrida ---")
corrida = Corrida(passageiro, "Casa", "Centro")

veiculo = Carro()
motorista.cadastrar_veiculo(veiculo)

corrida.escolher_veiculo(veiculo)
corrida.calcular_preco()
corrida.confirmar()

# Pagamento
print("\n--- Pagamento ---")
pagamento = PagamentoPix(corrida.valor)
pagamento.processar_pagamento()

# Histórico
print("\n--- Histórico ---")
historico = Historico(passageiro)
historico.adicionar(corrida)
historico.visualizar()

# Avaliação
print("\n--- Avaliação ---")
avaliacao = Avaliacao(passageiro, motorista, 5, "Excelente motorista!")
avaliacao.avaliar()

# Cancelamento
print("\n--- Cancelamento ---")
controle = ControleCancelamento(2)

controle.mostrar_motivos()

controle.cancelar_corrida("")  # erro
controle.cancelar_corrida("Fome")  # inválido
controle.cancelar_corrida("Problema no carro")  # ok
controle.cancelar_corrida("Emergência")  # ok
controle.cancelar_corrida("Trânsito extremo")  # limite atingido

# Suporte
print("\n--- Suporte ---")
suporte = Suporte(passageiro)
suporte.enviar("Tive um problema na corrida")
suporte.historico()