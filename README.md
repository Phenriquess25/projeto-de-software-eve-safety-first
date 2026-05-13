# Eve - Safety First 

Sistema de transporte com foco em segurança e controle de cancelamentos pelo motorista.

## Descrição
Este projeto é uma simulação de plataforma de transporte desenvolvida para demonstrar práticas avançadas de **Programação Orientada a Objetos (POO)** e organização modular em Python.

## Autor

Senan Isäc Armel DJENONLO

## Estrutura do Projeto (Refatorada)

O código foi organizado seguindo padrões de modularidade para facilitar a manutenção:

```text
.
├── modelos/              # Pacote com as regras de negócio
│   ├── usuario.py        # Herança: Usuario, Passageiro e Motorista
│   ├── veiculo.py        # Polimorfismo: Diferentes tarifas (Moto, Carro, VIP)
│   ├── corrida.py        # Gestão de trajetos e distâncias
│   ├── pagamento.py      # Polimorfismo: Pix, Cartão e Dinheiro
│   └── ...               # Suporte, Avaliação e Histórico
├── main.py               # Script principal com testes de integração
└── .gitignore            # Limpeza de arquivos temporários (__pycache__)
```

## Funcionalidades principais

- Cadastro de usuários (passageiro e motorista)
- Login com validação
- Solicitação de corridas
- Escolha de tipo de veículo
- Cálculo de preço automático
- Sistema de pagamento (PIX, cartão, dinheiro)
- Histórico de corridas
- Avaliação de motoristas
- Controle de cancelamentos
- Suporte ao cliente

## Conceitos de POO utilizados

- Herança
- Polimorfismo
- Encapsulamento
- Classes abstratas

## 🏭 Factory Method - Padrão Criacional (IMPLEMENTADO)

O padrão criacional **Factory Method** foi aplicado nos módulos `modelos/veiculo.py` e `modelos/pagamento.py`. 

**Mudanças Principais:**
- ✅ `VeiculoFactory` centraliza a criação de veículos (Moto, Carro, VIP)
- ✅ `PagamentoFactory` centraliza a criação de pagamentos (PIX, Cartão, Dinheiro)
- ✅ `main.py` refatorado para usar as factories em vez de instanciações diretas
- ✅ Código desacoplado e mais fácil de estender

**Exemplo de uso:**
```python
veiculo = VeiculoFactory.criar("carro")
pagamento = PagamentoFactory.criar("pix", 100)
```

📖 **Documentação completa:** [Factory Method Pattern](docss/factory_method.md)

## 📚 Documentação

- [Herança](docss/heranca.md)
- [Polimorfismo](docss/polimorfismo.md)
- [Funcionalidades](docss/documentacao_funcionalidades.md)
- [Factory Method (Padrão Criacional)](docss/factory_method.md)

## 🧪 Como Testar

### Teste Interativo (Modo Completo)

Para usar o sistema de forma interativa com menus:

```bash
python main.py
```

**Funcionalidades testadas:**
- ✅ Cadastro de Passageiro
- ✅ Cadastro de Motorista
- ✅ Login de Usuário
- ✅ Solicitação de Corrida (com Factory Method)
- ✅ Escolha de Veículo (Moto, Carro, VIP - via VeiculoFactory)
- ✅ Escolha de Pagamento (PIX, Cartão, Dinheiro - via PagamentoFactory)
- ✅ Histórico de Corridas
- ✅ Envio de Mensagens de Suporte
- ✅ Logout

### Teste Automatizado Completo

Para testar todos os caminhos de forma automatizada:

```bash
python teste_completo.py
```

**Testes executados:**
- ✅ Cadastro e Operações do Passageiro
- ✅ Solicitação de Corrida com Factory Method
- ✅ Histórico e Suporte
- ✅ Polimorfismo com múltiplos Pagamentos
- ✅ Polimorfismo com múltiplos Veículos
- ✅ Cadastro e Operações do Motorista
- ✅ Tratamento de Erros do Factory Method
- ✅ Persistência de Dados

### Teste do Factory Method

Para demonstrar o padrão criacional em ação:

```bash
python teste_factory.py
```

**O que é testado:**
- ✅ Criação de Veículos com VeiculoFactory
- ✅ Criação de Pagamentos com PagamentoFactory
- ✅ Tratamento de Erros
- ✅ Polimorfismo em Ação
