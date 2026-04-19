
# Eve - Safety First 

Sistema de transporte com foco em segurança e controle de cancelamentos pelo motorista.

##  Descrição
Este projeto é uma simulação de plataforma de transporte desenvolvida para demonstrar práticas avançadas de **Programação Orientada a Objetos (POO)** e organização modular em Python.

## Autor

Senan Isäc Armel DJENONLO

##  Estrutura do Projeto (Refatorada)
O código foi organizado seguindo padrões de modularidade para facilitar a manutenção:

.
├── modelos/              # Pacote com as regras de negócio
│   ├── usuario.py        # Herança: Usuario, Passageiro e Motorista
│   ├── veiculo.py        # Polimorfismo: Diferentes tarifas (Moto, Carro, VIP)
│   ├── corrida.py        # Gestão de trajetos e distâncias
│   ├── pagamento.py      # Polimorfismo: Pix, Cartão e Dinheiro
│   └── ...               # Suporte, Avaliação e Histórico
├── main.py               # Script principal com testes de integração
└── .gitignore            # Limpeza de arquivos temporários (__pycache__)

##  Funcionalidades
    **Cadastro & Login:** Sistema com validação real de **CPF** e **CNH**.
    **Gestão de Corridas:** Escolha de veículos com cálculo automático de tarifas.
     **Segurança & Controle:** Sistema de cancelamento com limites diários e motivos obrigatórios.
    **Experiência Completa:** Histórico de viagens, avaliações de motoristas e suporte ao cliente.
    **Rastreamento:** Simulação de localização do motorista em tempo real.

## Como Testar
Certifique-se de ter o Python instalado e execute:
```bash
python main.py
 