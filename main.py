# -*- coding: utf-8 -*-
import sys
import os

# Configurar encoding para UTF-8 no Windows
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

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
    print("2. 🚕 Pegar Corrida")
    print("3. 📋 Ver Histórico de Corridas")
    print("4. ⏹️  Gerenciar Cancelamentos")
    print("5. ⭐ Ver Avaliações Recebidas")
    print("6. 💬 Enviar Mensagem de Suporte")
    print("7. 🚪 Logout")
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
        
        if salvar_usuarios(passageiro):
            print("\n✅ Passageiro cadastrado com sucesso!")
            input("\nPressione Enter para continuar...")
            return passageiro
        else:
            print("\n❌ Erro ao cadastrar passageiro!")
            input("\nPressione Enter para continuar...")
            return None
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

    # Menu para escolher tipo de veículo
    print("\n" + "="*50)
    print("  Qual tipo de veículo você possui?")
    print("="*50)
    print("\n1. 🏍️  Moto")
    print("2. 🚗 Carro")
    print("3. 👑 VIP")
    print("\n" + "="*50)
    
    opcao_veiculo = input("Escolha (1/2/3): ").strip()
    tipos_veiculo = {'1': 'Moto', '2': 'Carro', '3': 'VIP'}
    tipo_veiculo = tipos_veiculo.get(opcao_veiculo, 'Carro')
    modelo_especifico = input("Modelo específico (ex: Honda PCX, Toyota Corolla): ")
    placa = input("Placa do veículo: ")
    modelo = f"{tipo_veiculo} - {modelo_especifico}"
    
    try:
        motorista = Motorista(nome, cpf, email, senha, telefone, cnh, placa, modelo)
        motorista.cadastrar()
        
        if motorista.validar_documentos():
            motorista.confirmar_conta()
        
        if salvar_usuarios(motorista):
            print("\n✅ Motorista cadastrado com sucesso!")
            input("\nPressione Enter para continuar...")
            return motorista
        else:
            print("\n❌ Erro ao cadastrar motorista!")
            input("\nPressione Enter para continuar...")
            return None
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
    
    try:
        # Tenta fazer login
        usuarios = listar_usuarios()
        for usuario_dict in usuarios:
            # Validação de campos
            if usuario_dict.get('email') != email or usuario_dict.get('senha') != senha:
                continue
            
            # Garante que tem os campos necessários
            if 'nome_completo' not in usuario_dict:
                print("\n❌ Erro: Usuário com dados incompletos no banco!")
                input("\nPressione Enter para continuar...")
                return None
            
            tipo = usuario_dict.get('tipo_usuario', 'passageiro')
            
            try:
                if tipo == 'passageiro':
                    usuario = Passageiro(
                        usuario_dict['nome_completo'], usuario_dict['cpf'],
                        usuario_dict['email'], usuario_dict['senha'],
                        usuario_dict['telefone']
                    )
                else:  # motorista
                    usuario = Motorista(
                        usuario_dict['nome_completo'], usuario_dict['cpf'],
                        usuario_dict['email'], usuario_dict['senha'],
                        usuario_dict['telefone'], usuario_dict.get('cnh', ''),
                        usuario_dict.get('placa', ''), usuario_dict.get('modelo_veiculo', '')
                    )
                
                print(f"\n✅ Login realizado com sucesso!")
                input("\nPressione Enter para continuar...")
                return usuario
            except Exception as e:
                print(f"\n❌ Erro ao processar dados do usuário: {e}")
                input("\nPressione Enter para continuar...")
                return None
        
        print("\n❌ Email ou senha incorretos!")
        input("\nPressione Enter para continuar...")
        return None
        
    except Exception as e:
        print(f"\n❌ Erro ao fazer login: {e}")
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

def obter_tipo_veiculo_motorista(motorista):
    """Extrai o tipo do veículo a partir do cadastro do motorista."""
    modelo = getattr(motorista, 'modelo_veiculo', '')
    modelo_upper = modelo.upper()

    if 'MOTO' in modelo_upper:
        return 'Moto'
    if 'VIP' in modelo_upper:
        return 'VIP'
    return 'Carro'

def formatar_modelo_motorista(motorista):
    """Separa o tipo e o modelo específico cadastrados."""
    modelo = getattr(motorista, 'modelo_veiculo', '')
    if ' - ' in modelo:
        tipo, modelo_especifico = modelo.split(' - ', 1)
        return tipo, modelo_especifico
    return obter_tipo_veiculo_motorista(motorista), modelo

def gerar_corridas_disponiveis(tipo_veiculo):
    """Gera 3 corridas fictícias compatíveis com o tipo de veículo do motorista"""
    locais_origem = ["Centro", "Vila Industrial", "Bairro Leste", "Aeroporto", "Terminal Rodoviário", "Shopping Mall"]
    locais_destino = ["Residência", "Trabalho", "Hospital", "Hotel", "Restaurante", "Escola"]
    
    import random
    corridas = []
    
    for i in range(1, 4):
        origem = random.choice(locais_origem)
        destino = random.choice(locais_destino)
        distancia = round(random.uniform(3, 30), 2)
        
        # Preços base por tipo de veículo
        preco_moto = round(distancia * 1.50, 2)
        preco_carro = round(distancia * 2.50, 2)
        preco_vip = round(distancia * 4.00, 2)
        
        corridas.append({
            'id': i,
            'origem': origem,
            'destino': destino,
            'distancia': distancia,
            'tipo_veiculo': tipo_veiculo,
            'preco_moto': preco_moto,
            'preco_carro': preco_carro,
            'preco_vip': preco_vip
        })
    
    return corridas

def pegar_corrida(motorista):
    """Menu para motorista escolher e aceitar uma corrida"""
    limpar_tela()
    print("\n" + "="*50)
    print("  CORRIDAS DISPONÍVEIS")
    print("="*50)
    
    tipo_veiculo = obter_tipo_veiculo_motorista(motorista)
    corridas = gerar_corridas_disponiveis(tipo_veiculo)
    
    for corrida in corridas:
        print(f"\n🚕 CORRIDA #{corrida['id']}")
        print(f"   Tipo: {corrida['tipo_veiculo']}")
        print(f"   De: {corrida['origem']}")
        print(f"   Para: {corrida['destino']}")
        print(f"   Distância: {corrida['distancia']} km")
        
        # Mostrar preço conforme tipo de veículo
        if tipo_veiculo == "Moto":
            preco = corrida['preco_moto']
        elif tipo_veiculo == "VIP":
            preco = corrida['preco_vip']
        else:
            preco = corrida['preco_carro']
        
        print(f"   Preço: R$ {preco:.2f}")
        print("   " + "-"*45)
    
    print("\n" + "="*50)
    opcao = input("Escolha a corrida para aceitar (1/2/3) ou 0 para cancelar: ").strip()
    
    if opcao in ['1', '2', '3']:
        corrida_escolhida = corridas[int(opcao) - 1]
        
        if tipo_veiculo == "Moto":
            preco = corrida_escolhida['preco_moto']
        elif tipo_veiculo == "VIP":
            preco = corrida_escolhida['preco_vip']
        else:
            preco = corrida_escolhida['preco_carro']
        
        limpar_tela()
        print("\n" + "="*50)
        print("  ✅ CORRIDA ACEITA!")
        print("="*50)
        print(f"\n📍 Origem: {corrida_escolhida['origem']}")
        print(f"📍 Destino: {corrida_escolhida['destino']}")
        print(f"📏 Distância: {corrida_escolhida['distancia']} km")
        print(f"💰 Valor: R$ {preco:.2f}")
        print(f"🚗 Veículo: {tipo_veiculo}")
        print("\n" + "="*50)

        gerar_avaliacao_corrida(motorista, corrida_escolhida)
        input("Pressione Enter para continuar...")
    else:
        print("\n❌ Operação cancelada!")
        input("Pressione Enter para continuar...")

def gerar_avaliacao_corrida(motorista, corrida):
    """Gera automaticamente uma avaliação para a corrida aceita."""
    import random

    notas_possiveis = [4, 5]
    comentarios_possiveis = [
        "Viagem tranquila e motorista educado.",
        "Corrida rápida e segura.",
        "Motorista pontual e atencioso.",
        "Boa experiência, recomendo.",
        "Atendimento excelente durante a corrida."
    ]

    passageiro_fake = Passageiro("Sistema", "00000000000", "sistema@eve.com", "", "0000000000")
    nota = random.choice(notas_possiveis)
    comentario = random.choice(comentarios_possiveis)

    avaliacao = Avaliacao(passageiro_fake, motorista, nota, comentario)
    avaliacao.avaliar()

    if adicionar_avaliacao_motorista(motorista.cpf, {
        "nota": nota,
        "comentario": comentario,
        "origem": corrida["origem"],
        "destino": corrida["destino"],
        "distancia": corrida["distancia"]
    }):
        print(f"\n⭐ Avaliação registrada: {nota}/5")
        print(f"   Comentário: {comentario}")
    else:
        print("\n⚠️ Não foi possível salvar a avaliação no cadastro do motorista.")

def mostrar_avaliacoes_motorista(motorista):
    """Mostra as avaliações salvas do motorista."""
    usuario = buscar_usuario_por_cpf(motorista.cpf)
    avaliacoes = []

    if usuario:
        avaliacoes = usuario.get("avaliacoes", [])

    print("\n⭐ Avaliações Recebidas")

    if not avaliacoes:
        print("   Nenhuma avaliação registrada ainda.")
        return

    media = usuario.get("media_avaliacoes", 0)
    total = usuario.get("total_avaliacoes", len(avaliacoes))

    print(f"   Média: {media}/5.0")
    print(f"   Total de avaliações: {total}")

    for indice, avaliacao in enumerate(avaliacoes[-5:], start=1):
        print(f"   {indice}. {avaliacao['nota']}/5 - {avaliacao['comentario']}")

def main():
    while True:
        exibir_menu_principal()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            # Cadastrar Passageiro
            cadastrar_passageiro()
            
        elif opcao == "2":
            # Cadastrar Motorista
            cadastrar_motorista()
            
        elif opcao == "3":
            # Login
            usuario = fazer_login()
            if usuario:
                # Detectar tipo de usuário
                tipo = 'passageiro' if isinstance(usuario, Passageiro) else 'motorista'
                nome = usuario.nome_completo

                while True:
                    if tipo == 'passageiro':
                        exibir_menu_passageiro(usuario)
                        menu_opc = input("Escolha uma opção: ").strip()
                        if menu_opc == "1":
                            solicitar_corrida(usuario)
                        elif menu_opc == "2":
                            ver_historico(usuario)
                        elif menu_opc == "3":
                            enviar_suporte(usuario)
                        elif menu_opc == "4":
                            print("\n🚪 Você foi desconectado!")
                            input("\nPressione Enter para continuar...")
                            break
                        else:
                            print("\n❌ Opção inválida!")
                            input("\nPressione Enter para continuar...")
                            
                    elif tipo == 'motorista':
                        exibir_menu_motorista(usuario)
                        menu_opc = input("Escolha uma opção: ").strip()
                        if menu_opc == "1":
                            print(f"\n👤 {usuario.nome_completo}")
                            print(f"   CNH: {usuario.cnh}")
                            print(f"   Placa: {usuario.placa}")
                            tipo_veiculo, modelo_especifico = formatar_modelo_motorista(usuario)
                            print(f"   Tipo do veículo: {tipo_veiculo}")
                            if modelo_especifico:
                                print(f"   Modelo: {modelo_especifico}")
                            input("\nPressione Enter para continuar...")
                        elif menu_opc == "2":
                            pegar_corrida(usuario)
                        elif menu_opc == "3":
                            ver_historico(usuario)
                        elif menu_opc == "4":
                            print("\n⏹️  Gerenciar Cancelamentos")
                            print("Nenhum cancelamento recente.")
                            input("\nPressione Enter para continuar...")
                        elif menu_opc == "5":
                            mostrar_avaliacoes_motorista(usuario)
                            input("\nPressione Enter para continuar...")
                        elif menu_opc == "6":
                            enviar_suporte(usuario)
                        elif menu_opc == "7":
                            print("\n🚪 Você foi desconectado!")
                            input("\nPressione Enter para continuar...")
                            break
                        else:
                            print("\n❌ Opção inválida!")
                            input("\nPressione Enter para continuar...")
            
        elif opcao == "4":
            limpar_tela()
            print("\n👋 Obrigado por usar o EVE - SAFETY FIRST!")
            print("Saindo...\n")
            break
        else:
            print("\n❌ Opção inválida!")
            input("\nPressione Enter para continuar...")


if __name__ == "__main__":
    main()
