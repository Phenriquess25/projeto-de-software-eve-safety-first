````md
# Eve - Safety First 

Sistema de transporte com foco em segurança e controle de cancelamentos pelo motorista.

## Descrição
Este projeto é uma simulação de plataforma de transporte desenvolvida para demonstrar práticas avançadas de **Programação Orientada a Objetos (POO)** e organização modular em Python.

## Autor

Pedro Henrique Santos da Silva

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
````

## Funcionalidades principais

* Cadastro de usuários (passageiro e motorista)
* Login com validação
* Solicitação de corridas
* Escolha de tipo de veículo
* Cálculo de preço automático
* Sistema de pagamento (PIX, cartão, dinheiro)
* Histórico de corridas
* Avaliação de motoristas
* Controle de cancelamentos
* Suporte ao cliente

## Conceitos de POO utilizados

* Herança
* Polimorfismo
* Encapsulamento
* Classes abstratas

---

# Padrões de Projeto Utilizados

Além dos conceitos de Programação Orientada a Objetos, o projeto também aplica padrões de projeto para melhorar a organização, reutilização e manutenção do código.

---

## 🏭 Factory Method - Padrão Criacional

O padrão criacional Factory Method foi aplicado nos módulos `modelos/veiculo.py` e `modelos/pagamento.py`.

### Mudanças principais

* `VeiculoFactory` centraliza a criação de veículos
* `PagamentoFactory` centraliza a criação de pagamentos
* `main.py` refatorado para usar as factories
* Código desacoplado e mais fácil de expandir

### Exemplo de uso

```python
veiculo = VeiculoFactory.criar("carro")
pagamento = PagamentoFactory.criar("pix", 100)
```

### Vantagens do Factory Method

* reduz acoplamento
* evita múltiplos `if/elif`
* facilita manutenção
* permite adicionar novos tipos facilmente
* melhora organização do código

---

## 🎨 Decorator - Padrão Estrutural

O padrão estrutural Decorator foi utilizado para adicionar funcionalidades extras às corridas dinamicamente, sem modificar diretamente a classe principal.

### Exemplos de funcionalidades

* corrida VIP
* prioridade de atendimento
* taxa extra
* seguro adicional

### Exemplo conceitual

```python
class Corrida:
    def valor(self):
        return 20


class CorridaVIPDecorator:
    def __init__(self, corrida):
        self.corrida = corrida

    def valor(self):
        return self.corrida.valor() + 15
```

### Vantagens do Decorator

* adiciona funcionalidades sem alterar classes existentes
* reduz duplicação de código
* aumenta flexibilidade do sistema
* facilita manutenção
* melhora reutilização
* permite expansão futura com menor impacto

---

## 🔄 Mediator - Padrão Comportamental

O padrão comportamental Mediator foi utilizado para centralizar a comunicação entre os componentes do sistema.

### Componentes envolvidos

* passageiro
* motorista
* corrida
* pagamento
* suporte

### Exemplo conceitual

```python
class CentralCorridas:

    def solicitar_corrida(self, passageiro):
        print("Buscando motorista disponível")

    def finalizar_corrida(self):
        print("Corrida finalizada")
```

### Vantagens do Mediator

* reduz o acoplamento entre classes
* centraliza regras de comunicação
* melhora organização do sistema
* facilita manutenção
* simplifica futuras expansões
* evita dependências diretas excessivas

---

## 📚 Documentação

* [Herança](docss/heranca.md)
* [Polimorfismo](docss/polimorfismo.md)
* [Funcionalidades](docss/documentacao_funcionalidades.md)
* [Factory Method](docss/factory_method.md)

---

## 🧪 Como Testar

### Teste Interativo (Modo Completo)

Para usar o sistema de forma interativa com menus:

```bash
python main.py
```

### Funcionalidades testadas

* Cadastro de Passageiro
* Cadastro de Motorista
* Login de Usuário
* Solicitação de Corrida
* Escolha de Veículo
* Escolha de Pagamento
* Histórico de Corridas
* Envio de Mensagens de Suporte
* Logout

---

## Teste Automatizado Completo

Para testar todos os caminhos automaticamente:

```bash
python teste_completo.py
```

### Testes executados

* Cadastro e Operações do Passageiro
* Solicitação de Corrida
* Histórico e Suporte
* Polimorfismo com múltiplos Pagamentos
* Polimorfismo com múltiplos Veículos
* Cadastro e Operações do Motorista
* Tratamento de Erros
* Persistência de Dados

---

## Teste do Factory Method

Para demonstrar o padrão criacional em funcionamento:

```bash
python teste_factory.py
```

### O que é testado

* Criação de Veículos com VeiculoFactory
* Criação de Pagamentos com PagamentoFactory
* Tratamento de Erros
* Polimorfismo em ação

```
```
