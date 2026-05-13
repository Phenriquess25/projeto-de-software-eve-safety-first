from modelos.usuario import Passageiro, Motorista
from modelos.sessao import Login
from modelos.corrida import Corrida
from modelos.veiculo import VeiculoFactory
from modelos.pagamento import PagamentoFactory
from modelos.historico import Historico
from modelos.avaliacao import Avaliacao
from modelos.controle_cancelamento import ControleCancelamento
from modelos.suporte import Suporte

from bancos_dados import *

from datetime import date

# =========================
# SISTEMA EVE - SAFETY FIRST (INTERATIVO)
# =========================

def limpar_tela():
    """Limpa a tela do console"""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_menu_principal():
    """Exibe o menu principal"""
    print("\n" + "="*50)
    print("  🚕 EVE - SAFETY FIRST 🚕")
    print("="*50)
    print("\n1. Cadastrar Passageiro")
    print("2. Cadastrar Motorista")
    print("3. Login")
    print("4. Sair")
    print("\n" + "="*50)

def exibir_menu_passageiro(usuario):
    """Exibe o menu do passageiro autenticado"""
    print(f"\n{'='*50}")
    print(f"  👤 PASSAGEIRO: {usuario.nome_completo}")
    print(f"{'='*50}")
    print("\n1. 🚕 Solicitar Corrida")
    print("2. 📋 Ver Histórico")
    print("3. 💬 Enviar Mensagem de Suporte")
    print("4. 🚪 Logout")
    print("\n" + "="*50)

def exibir_menu_motorista(usuario):
    """Exibe o menu do motorista autenticado"""
    print(f"\n{'='*50}")
    print(f"  🚗 MOTORISTA: {usuario.nome_completo}")
    print(f"{'='*50}")
    print("\n1. 👁️  Ver Perfil e Veículo")
    print("2. 📋 Ver Histórico de Corridas")
    print("3. ⏹️  Gerenciar Cancelamentos")
    print("4. ⭐ Ver Avaliações Recebidas")
    print("5. 💬 Enviar Mensagem de Suporte")
    print("6. 🚪 Logout")
    print("\n" + "="*50)

def exibir_menu_veiculo():
    """Exibe menu de seleção de veículos usando Factory"""
    print("\n" + "="*50)
    print("  Escolha o tipo de veículo:")
    print("="*50)
    print("\n1. 🏍️  Moto      (R$1.00 por km)")
    print("2. 🚗 Carro     (R$2.00 por km)")
    print("3. 👑 VIP       (R$4.00 por km)")
    print("\n" + "="*50)

def exibir_menu_pagamento():
    """Exibe menu de seleção de pagamento usando Factory"""
    print("\n" + "="*50)
    print("  Escolha a forma de pagamento:")
    print("="*50)
    print("\n1. 💳 PIX       (Aprovado instantaneamente)")
    print("2. 💰 Cartão    (Aprovado instantaneamente)")
    print("3. 💵 Dinheiro  (Na entrega)")
    print("\n" + "="*50)

def cadastrar_passageiro():
    """Cadastra um novo passageiro"""
    limpar_tela()
    print("\n" + "="*50)
    print("  CADASTRO DE PASSAGEIRO")
    print("="*50)
    
    nome = input("\nNome completo: ")
    cpf = input("CPF (11 dígitos): ")
    email = input("Email: ")
    senha = input("Senha: ")
    telefone = input("Telefone: ")
    
    try:
        passageiro = Passageiro(nome, cpf, email, senha, telefone)
        passageiro.cadastrar()
        salvar_usuarios(passageiro)
        print("\n✅ Passageiro cadastrado com sucesso!")
        input("\nPressione Enter para continuar...")
        return passageiro
    except Exception as e:
        print(f"\n❌ Erro ao cadastrar: {e}")
        input("\nPressione Enter para continuar...")
        return None

def cadastrar_motorista():
    """Cadastra um novo motorista"""
    limpar_tela()
    print("\n" + "="*50)
    print("  CADASTRO DE MOTORISTA")
    print("="*50)
    
    nome = input("\nNome completo: ")
    cpf = input("CPF (11 dígitos): ")
    email = input("Email: ")
    senha = input("Senha: ")
    telefone = input("Telefone: ")
    cnh = input("CNH (11 dígitos): ")
    placa = input("Placa do veículo: ")
    modelo = input("Modelo do veículo: ")
    
    try:
        motorista = Motorista(nome, cpf, email, senha, telefone, cnh, placa, modelo)
        motorista.cadastrar()
        
        if motorista.validar_documentos():
            motorista.confirmar_conta()
            print("\n✅ Motorista cadastrado e verificado com sucesso!")
        else:
            print("\n⚠️  Motorista cadastrado, mas não passou na verificação.")
        
        salvar_usuarios(motorista)
        input("\nPressione Enter para continuar...")
        return motorista
    except Exception as e:
        print(f"\n❌ Erro ao cadastrar: {e}")
        input("\nPressione Enter para continuar...")
        return None

def fazer_login():
    """Realiza login do usuário"""
    limpar_tela()
    print("\n" + "="*50)
    print("  LOGIN")
    print("="*50)
    
    email = input("\nEmail: ")
    senha = input("Senha: ")
    
    # Tenta fazer login como passageiro
    usuarios = listar_usuarios()
    for usuario_dict in usuarios:
        if usuario_dict.get('email') == email and usuario_dict.get('senha') == senha:
            tipo = usuario_dict.get('tipo_usuario')
            
            if tipo == 'passageiro':
                usuario = Passageiro(
                    usuario_dict['nome'], usuario_dict['cpf'],
                    usuario_dict['email'], usuario_dict['senha'],
                    usuario_dict['telefone']
                )
            else:
                usuario = Motorista(
                    usuario_dict['nome'], usuario_dict['cpf'],
                    usuario_dict['email'], usuario_dict['senha'],
                    usuario_dict['telefone'], usuario_dict['cnh'],
                    usuario_dict['placa'], usuario_dict['modelo']
                )
            
            login = Login(usuario)
            if login.autenticar(email, senha):
                print(f"\n✅ Login realizado com sucesso!")
                input("\nPressione Enter para continuar...")
                return usuario
    
    print("\n❌ Email ou senha incorretos!")
    input("\nPressione Enter para continuar...")
    return None

def solicitar_corrida(passageiro):
    """Solicita uma corrida com uso do Factory Method"""
    limpar_tela()
    print("\n" + "="*50)
    print("  SOLICITAR CORRIDA")
    print("="*50)
    
    origem = input("\nOnde você está? ")
    destino = input("Para onde deseja ir? ")
    
    corrida = Corrida(passageiro, origem, destino)
    
    # Menu de Veículos com Factory
    exibir_menu_veiculo()
    opcao_veiculo = input("Opção: ").strip()
    
    tipos = {'1': 'moto', '2': 'carro', '3': 'vip'}
    tipo_escolhido = tipos.get(opcao_veiculo, 'carro')
    
    try:
        veiculo = VeiculoFactory.criar(tipo_escolhido)
        corrida.escolher_veiculo(veiculo)
        corrida.calcular_preco()
        corrida.confirmar()
        
        print(f"\n✅ Corrida confirmada!")
        print(f"   Veículo: {veiculo.tipo}")
        print(f"   Preço: R${corrida.valor:.2f}")
        
        # Menu de Pagamento com Factory
        exibir_menu_pagamento()
        opcao_pagamento = input("Opção: ").strip()
        
        formas = {'1': 'pix', '2': 'cartao', '3': 'dinheiro'}
        forma_escolhida = formas.get(opcao_pagamento, 'pix')
        
        pagamento = PagamentoFactory.criar(forma_escolhida, corrida.valor)
        pagamento.processar_pagamento()
        pagamento.mostrar_status()
        
        # Salvar dados
        salvar_corridas(corrida)
        salvar_pagamentos(pagamento)
        
        # Adicionar ao histórico
        historico = Historico(passageiro)
        historico.adicionar(corrida)
        
        print("\n✅ Corrida finalizada com sucesso!")
        input("\nPressione Enter para continuar...")
        
    except ValueError as e:
        print(f"\n❌ Erro: {e}")
        input("\nPressione Enter para continuar...")

def ver_historico(usuario):
    """Exibe o histórico de corridas"""
    limpar_tela()
    print("\n" + "="*50)
    print("  HISTÓRICO DE CORRIDAS")
    print("="*50)
    
    historico = Historico(usuario)
    historico.visualizar()
    
    input("\nPressione Enter para continuar...")

def enviar_suporte(usuario):
    """Envia mensagem de suporte"""
    limpar_tela()
    print("\n" + "="*50)
    print("  SUPORTE AO CLIENTE")
    print("="*50)
    
    mensagem = input("\nDescreva seu problema ou dúvida: ")
    
    suporte = Suporte(usuario)
    suporte.enviar(mensagem)
    suporte.historico()
    
    salvar_mensagens(usuario, mensagem)
    
    print("\n✅ Mensagem enviada com sucesso!")
    input("\nPressione Enter para continuar...")

