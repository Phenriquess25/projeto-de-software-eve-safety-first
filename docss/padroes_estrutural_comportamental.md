# Padrões Estrutural e Comportamental — Eve: Safety First

## 📚 Índice

1. [Padrão Estrutural - Decorator](#padrão-estrutural---decorator)
2. [Padrão Comportamental - Mediator](#padrão-comportamental---mediator)
3. [Combinação dos Padrões](#combinação-dos-padrões)
4. [Como Executar](#como-executar)

---

## 🎨 Padrão Estrutural - Decorator

### O que é Decorator?

O **Decorator** é um padrão estrutural que permite adicionar comportamentos a objetos dinamicamente, sem modificar suas classes. É ideal para adicionar funcionalidades de forma flexível e reutilizável.

### Problema que resolve

```
ANTES (sem Decorator):
- Classe Corrida com 10 subclasses (CorridaVIP, CorridaComSeguro, CorridaComPrioridade, etc.)
- Explosão de combinações (CorridaVIPComSeguro, CorridaVIPComPrioridade, etc.)
- Dificuldade em manutenção
- Violação do princípio Single Responsibility
```

### Solução com Decorator

```
DEPOIS:
- Classe Corrida base simples
- Decoradores independentes que envolvem a corrida
- Combinações dinâmicas sem limitar subclasses
- Fácil de manutenção e expansão
```

### Implementação no Eve Safety First

#### 1. Interface de Corrida Decorada

```python
class CorridaDecorada(ABC):
    @abstractmethod
    def calcular_valor(self) -> float:
        pass
    
    @abstractmethod
    def obter_descricao(self) -> str:
        pass
```

#### 2. Componente Concreto (Corrida Simples)

```python
class CorridaSimples(CorridaDecorada):
    def __init__(self, valor_base: float):
        self.valor_base = valor_base
    
    def calcular_valor(self) -> float:
        return self.valor_base
```

#### 3. Decoradores

```python
# Decorator Base
class DecoradorCorrida(CorridaDecorada):
    def __init__(self, corrida: CorridaDecorada):
        self.corrida = corrida

# Decoradores Específicos
class CorridaVIP(DecoradorCorrida):
    def calcular_valor(self) -> float:
        return self.corrida.calcular_valor() + 50.0

class PrioridadeAtendimento(DecoradorCorrida):
    def calcular_valor(self) -> float:
        return self.corrida.calcular_valor() + 15.0

class SeguroAdicional(DecoradorCorrida):
    def calcular_valor(self) -> float:
        return self.corrida.calcular_valor() + 20.0

class Promocao(DecoradorCorrida):
    def calcular_valor(self) -> float:
        valor = self.corrida.calcular_valor()
        return valor - (valor * 0.15)  # 15% OFF
```

### Exemplos de Uso

#### 1. Corrida Simples
```python
corrida = CorridaSimples(50.0)
# Resultado: R$50.00
```

#### 2. Corrida com VIP
```python
corrida = CorridaVIP(CorridaSimples(50.0))
# Resultado: R$100.00 (50 + 50 VIP)
```

#### 3. Corrida Premium (VIP + Seguro + Prioridade)
```python
corrida = SeguroAdicional(
    PrioridadeAtendimento(
        CorridaVIP(CorridaSimples(50.0))
    )
)
# Resultado: R$135.00 (50 + 50 VIP + 15 Prioridade + 20 Seguro)
```

#### 4. Usando Construtor Fluente
```python
corrida = (ConstrutorCorrida(50.0)
    .adicionar_vip()
    .adicionar_prioridade()
    .adicionar_seguro()
    .aplicar_promocao(0.10))

print(corrida.obter_descricao())
print(f"Total: R${corrida.obter_valor_final():.2f}")
```

### Diagrama - Padrão Decorator

```
┌──────────────────────────────┐
│  <<interface>>               │
│  CorridaDecorada             │
│  ─────────────────────────── │
│  + calcular_valor()          │
│  + obter_descricao()         │
└──────────────────────────────┘
         ▲         ▲
         │         │
    ┌────┴─────┐   │
    │           │   │
    │           │   ├─ CorridaVIP
    │           │   ├─ PrioridadeAtendimento
    │           │   ├─ SeguroAdicional
    │           │   ├─ TaxaExtra
    │           │   ├─ Promocao
    │           │   └─ DecoradorCorrida (base)
    │           │
    │       ┌───┴──────────────┐
    │       │                  │
    │    Composição         Herança
    │       │
┌───┴──────┐
│ Corrida  │
│  Simples │
└──────────┘
```

### Vantagens do Decorator

| Vantagem | Descrição |
|----------|-----------|
| **Flexibilidade** | Adiciona comportamentos dinamicamente |
| **Sem Explosão de Classes** | Evita múltiplas subclasses |
| **Single Responsibility** | Cada decorator tem uma responsabilidade |
| **Composição** | Combina comportamentos conforme necessário |
| **Fácil Manutenção** | Adicionar novo decorator é trivial |
| **Open/Closed Principle** | Aberto para extensão, fechado para modificação |

### Casos de Uso

- ✅ Adicionar funcionalidades opcionais a objetos
- ✅ Combinar comportamentos de forma flexível
- ✅ Evitar hierarquias profundas de classes
- ✅ Adicionar taxas/cobranças extras dinamicamente

---

## 🔄 Padrão Comportamental - Mediator

### O que é Mediator?

O **Mediator** é um padrão comportamental que define um objeto centralizado que encapsula como um conjunto de objetos interagem. Em vez de os objetos se comunicarem diretamente, eles se comunicam através do mediador.

### Problema que resolve

```
ANTES (sem Mediator):
- Passageiro comunica com Motorista
- Motorista comunica com Corrida
- Corrida comunica com Pagamento
- Pagamento comunica com Suporte
- Múltiplas dependências cruzadas (Spaghetti Code)
- Difícil de testar e manutenção complexa
```

### Solução com Mediator

```
DEPOIS:
- Central de Corridas (Mediator) centraliza comunicação
- Todos comunicam com a Central
- Reduz acoplamento
- Fácil de testar
- Simples de manutenção
```

### Implementação no Eve Safety First

#### 1. Central de Corridas (Mediator)

```python
class CentralCorridas:
    def __init__(self):
        self.passageiros = []
        self.motoristas = []
        self.corridas_ativas = []
        self.observadores = []
    
    # Gerenciamento centralizado
    def solicitar_corrida(self, passageiro, origem, destino):
        # Busca motorista
        # Cria corrida
        # Notifica observadores
        pass
    
    def processar_pagamento(self, id_corrida, pagamento):
        # Processa pagamento
        # Atualiza histórico
        pass
```

#### 2. Componentes (Passageiro, Motorista, etc.)

```python
# Antes (acoplamento direto):
passageiro.solicitar_corrida(motorista)
motorista.aceitar_corrida(corrida)
corrida.pagar(pagamento)

# Depois (com mediator):
central.solicitar_corrida(passageiro, origem, destino)
central.processar_pagamento(id_corrida, pagamento)
```

#### 3. Observer Pattern (Integrado)

```python
class ObservadorEventos:
    def notificar(self, evento, dados):
        print(f"Evento: {evento} - Dados: {dados}")

# Registrar observador
observador = ObservadorEventos()
central.registrar_observador(observador)

# Central notifica automaticamente
central.solicitar_corrida(passageiro, origem, destino)  # ← Notifica observador
```

### Exemplos de Uso

#### 1. Registrar Usuários
```python
central = CentralCorridas()

# Registrar passageiro
central.registrar_passageiro(passageiro)

# Registrar motorista
central.registrar_motorista(motorista)
```

#### 2. Solicitar Corrida
```python
# Passageiro solicita
corrida_info = central.solicitar_corrida(
    passageiro,
    origem="Aeroporto",
    destino="Centro"
)

# Central:
# - Busca motorista disponível
# - Cria corrida
# - Notifica observadores
# - Retorna informações
```

#### 3. Processar Pagamento
```python
pagamento = PagamentoPix(valor=75.50)
central.processar_pagamento(id_corrida, pagamento)

# Central:
# - Processa pagamento
# - Atualiza corrida
# - Notifica observadores
# - Libera motorista
```

#### 4. Enviar Suporte
```python
central.enviar_mensagem_suporte(
    usuario,
    "Problema na corrida"
)

# Central:
# - Registra mensagem
# - Notifica observadores
# - Permite resposta posterior
```

### Diagrama - Padrão Mediator

```
┌─────────────────────────────────────────────────────┐
│         🏢 CENTRAL DE CORRIDAS (Mediator)           │
├─────────────────────────────────────────────────────┤
│                                                     │
│  ✓ solicitar_corrida()                              │
│  ✓ finalizar_corrida()                              │
│  ✓ processar_pagamento()                            │
│  ✓ enviar_mensagem_suporte()                        │
│  ✓ registrar_observador()                           │
│  ✓ obter_estatisticas()                             │
│                                                     │
└──────────┬──────────────────────┬──────────────────┘
           │                      │
    ┌──────┴─────┐        ┌───────┴──────┐
    │             │        │               │
    │             │        │               │
┌───▼────┐ ┌─────▼──┐ ┌───▼────┐ ┌──────▼──┐
│Passageiro│ │Motorista│ │Corrida │ │Pagamento│
└────┬────┘ └────┬───┘ └────┬───┘ └────┬────┘
     │           │          │          │
     │           │          │          │
     └───────────┼──────────┼──────────┘
                 │          │
           Comunicação através
              do Mediator
```

### Sequência de Eventos

```
1. Passageiro solicita corrida
   └─> Central busca motorista disponível
       └─> Central cria corrida
           └─> Central notifica observadores
               └─> Observador recebe evento

2. Motorista aceita
   └─> Central atualiza status
       └─> Central notifica observadores

3. Corrida finaliza
   └─> Central libera motorista
       └─> Central atualiza histórico
           └─> Central notifica observadores

4. Processamento de pagamento
   └─> Central registra pagamento
       └─> Central notifica observadores
```

### Eventos do Sistema

| Evento | Dados | Descrição |
|--------|-------|-----------|
| `passageiro_registrado` | nome, timestamp | Novo passageiro registrado |
| `motorista_registrado` | nome, veículo, timestamp | Novo motorista registrado |
| `corrida_aceita` | passageiro, motorista, origem, destino | Corrida iniciada |
| `corrida_finalizada` | passageiro, motorista, valor | Corrida concluída |
| `preco_atualizado` | id_corrida, valor | Preço atualizado |
| `pagamento_processado` | tipo, status, valor | Pagamento realizado |
| `mensagem_suporte_recebida` | usuário, mensagem | Suporte recebido |
| `suporte_respondido` | usuário, resposta | Resposta de suporte |

### Vantagens do Mediator

| Vantagem | Descrição |
|----------|-----------|
| **Reduz Acoplamento** | Objetos não precisam se conhecer diretamente |
| **Centralização** | Lógica de comunicação em um único lugar |
| **Facilita Testes** | Cada componente pode ser testado isoladamente |
| **Manutenção** | Mudanças em um lugar, afetam todo sistema |
| **Escalabilidade** | Fácil adicionar novos componentes |
| **Reutilização** | Componentes podem ser reutilizados em outros contextos |

### Métodos Principais da Central

```python
# Gerenciamento de Usuários
central.registrar_passageiro(passageiro)
central.registrar_motorista(motorista)

# Gerenciamento de Corridas
central.solicitar_corrida(passageiro, origem, destino)
central.atualizar_preco_corrida(id_corrida, valor)
central.finalizar_corrida(id_corrida)
central.cancelar_corrida(id_corrida, motivo)

# Gerenciamento de Pagamentos
central.processar_pagamento(id_corrida, pagamento)

# Gerenciamento de Suporte
central.enviar_mensagem_suporte(usuario, mensagem)
central.responder_suporte(id_mensagem, resposta)

# Observer Pattern
central.registrar_observador(observador)
central.remover_observador(observador)

# Consultas
central.obter_corrida_ativa(id_corrida)
central.obter_corridas_passageiro(passageiro)
central.obter_motoristas_disponiveis()
central.obter_estatisticas()
```

---

## 🔗 Combinação dos Padrões

### Scenario Real

```python
# 1. Criar corrida com decoradores
corrida_premium = (ConstrutorCorrida(100.0)
    .adicionar_vip()
    .adicionar_seguro()
    .aplicar_promocao(0.10))

valor_final = corrida_premium.obter_valor_final()  # R$148.50

# 2. Registrar na central (mediator)
central.atualizar_preco_corrida(id_corrida, valor_final)

# 3. Processamento automático
central.processar_pagamento(id_corrida, pagamento)

# 4. Observadores notificados
# └─> Monitor recebe evento: "pagamento_processado"
```

### Benefícios da Combinação

| Combinação | Benefício |
|-----------|-----------|
| **Decorator** | Flexibilidade em cálculo de tarifas |
| **Mediator** | Centralização de comunicação |
| **Decorator + Mediator** | Sistema robusto, escalável e fácil de manutenção |

---

## 📁 Arquivos Criados

| Arquivo | Descrição |
|---------|-----------|
| `modelos/decorador_corrida.py` | Implementação do padrão Decorator |
| `modelos/mediador_corridas.py` | Implementação do padrão Mediator |
| `teste_padroes_estrutural_comportamental.py` | Script de demonstração e testes |

---

## 🧪 Como Executar

### Teste Interativo Completo

```bash
python teste_padroes_estrutural_comportamental.py
```

### Teste Individual - Decorator

```python
from modelos.decorador_corrida import ConstrutorCorrida

# Criar corrida premium
corrida = (ConstrutorCorrida(50.0)
    .adicionar_vip()
    .adicionar_seguro()
    .aplicar_promocao(0.15))

print(corrida.obter_descricao())
print(f"Total: R${corrida.obter_valor_final():.2f}")
```

### Teste Individual - Mediator

```python
from modelos.mediador_corridas import CentralCorridas, ObservadorEventos
from modelos.usuario import Passageiro, Motorista

# Criar central
central = CentralCorridas()

# Criar observador
monitor = ObservadorEventos()
central.registrar_observador(monitor)

# Registrar usuários
central.registrar_passageiro(passageiro)
central.registrar_motorista(motorista)

# Solicitar corrida
central.solicitar_corrida(passageiro, "A", "B")

# Exibir estatísticas
stats = central.obter_estatisticas()
print(stats)
```

---

## 📚 Resumo

### Decorator (Estrutural)
- ✅ Adiciona comportamentos dinamicamente
- ✅ Compõe funcionalidades
- ✅ Evita explosão de subclasses
- ✅ Ideal para taxas/cobranças opcionais

### Mediator (Comportamental)
- ✅ Centraliza comunicação
- ✅ Reduz acoplamento
- ✅ Facilita testes
- ✅ Melhora escalabilidade

### Combinação
- ✅ Cálculo de tarifas flexível (Decorator)
- ✅ Comunicação centralizada (Mediator)
- ✅ Sistema robusto e mantível

---

*Padrões Estrutural e Comportamental — Eve: Safety First*
