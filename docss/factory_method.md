# Factory Method - Padrão Criacional

## O que é Factory Method?

Factory Method é um **padrão de design criacional** que define uma interface para criar objetos, permitindo que a criação seja centralizada em uma classe especial chamada "fábrica". Em vez de instanciar objetos diretamente com `novo_objeto = Classe()`, usamos `novo_objeto = Factory.criar("tipo")`.

## Arquitetura - Diagrama do Padrão

```
┌─────────────────────────────────────────────────────────────────┐
│                     🚗 SISTEMA DE VEÍCULOS                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────────────────┐                                  │
│  │ <<abstract>>             │                                  │
│  │ Veiculo                  │                                  │
│  │ ──────────────────────── │                                  │
│  │ calcular_tarifa()        │                                  │
│  └──────────────────────────┘                                  │
│         ▲         ▲         ▲                                  │
│         │         │         │                                  │
│    ┌────┴─┐  ┌────┴─┐  ┌───┴──┐                              │
│    │ Moto │  │Carro │  │ VIP  │                              │
│    │ x1.0 │  │ x2.0 │  │ x4.0 │                              │
│    └──────┘  └──────┘  └──────┘                              │
│                                                                │
│  ┌────────────────────────────────────────────────────────┐   │
│  │ 🏭 VeiculoFactory                                      │   │
│  │ ──────────────────────────────────────────────────────  │   │
│  │ @staticmethod                                          │   │
│  │ criar(tipo: str) -> Veiculo                            │   │
│  │   if tipo == "moto": return Moto()                     │   │
│  │   elif tipo == "carro": return Carro()                 │   │
│  │   elif tipo == "vip": return VeiculoVIP()              │   │
│  │   else: raise ValueError(...)                          │   │
│  └────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                   💳 SISTEMA DE PAGAMENTOS                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────────────────┐                                  │
│  │ <<abstract>>             │                                  │
│  │ Pagamento                │                                  │
│  │ ──────────────────────── │                                  │
│  │ processar_pagamento()    │                                  │
│  └──────────────────────────┘                                  │
│         ▲         ▲         ▲                                  │
│         │         │         │                                  │
│  ┌──────┴──┐ ┌────┴────┐ ┌──┴───────┐                         │
│  │   PIX   │ │ Cartão  │ │ Dinheiro │                         │
│  │aprovado │ │aprovado │ │  entrega │                         │
│  └─────────┘ └─────────┘ └──────────┘                         │
│                                                                │
│  ┌────────────────────────────────────────────────────────┐   │
│  │ 🏭 PagamentoFactory                                    │   │
│  │ ──────────────────────────────────────────────────────  │   │
│  │ @staticmethod                                          │   │
│  │ criar(tipo: str, valor: float) -> Pagamento            │   │
│  │   if tipo == "pix": return PagamentoPix(valor)          │   │
│  │   elif tipo == "cartao": return PagamentoCartao(valor)   │   │
│  │   elif tipo == "dinheiro": return PagamentoDinheiro(...) │   │
│  │   else: raise ValueError(...)                          │   │
│  └────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│            📋 main.py (Código Cliente)                   │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  veiculo = VeiculoFactory.criar("carro")                 │
│  pagamento = PagamentoFactory.criar("pix", 100)          │
│                                                          │
│  ✨ Sem conhecer as classes concretas!                   │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

## 🔄 O que foi Mudado

### ANTES (Acoplamento Direto)

```python
# main.py - ANTES
from modelos.veiculo import Carro, Moto, VeiculoVIP
from modelos.pagamento import PagamentoPix, PagamentoCartao, PagamentoDinheiro

# Instanciação direta
veiculo = Carro()
pagamento = PagamentoPix(corrida.valor)

# Lógica condicional espalhada
veiculos = [
    Moto(),
    Carro(),
    VeiculoVIP()
]

pagamentos = [
    PagamentoPix(50),
    PagamentoCartao(100),
    PagamentoDinheiro(30)
]
```

**Problemas:**
- ❌ Código cliente acoplado às classes concretas
- ❌ Múltiplos imports de classes específicas
- ❌ Difícil adicionar novos tipos
- ❌ Lógica de criação espalhada

### DEPOIS (Factory Method)

```python
# main.py - DEPOIS
from modelos.veiculo import VeiculoFactory
from modelos.pagamento import PagamentoFactory

# Criação centralizada
veiculo = VeiculoFactory.criar("carro")
pagamento = PagamentoFactory.criar("pix", corrida.valor)

# Simples e consistente
veiculos = [
    VeiculoFactory.criar("moto"),
    VeiculoFactory.criar("carro"),
    VeiculoFactory.criar("vip")
]

pagamentos = [
    PagamentoFactory.criar("pix", 50),
    PagamentoFactory.criar("cartao", 100),
    PagamentoFactory.criar("dinheiro", 30)
]
```

**Vantagens:**
- ✅ Código desacoplado - só importa as factories
- ✅ Criação centralizada em um único lugar
- ✅ Fácil manutenção e escalabilidade
- ✅ Tratamento de erros centralizado
- ✅ Código mais legível e intuitivo

## 📝 Implementação nas Factories

### VeiculoFactory (`modelos/veiculo.py`)

```python
class VeiculoFactory:
    """Factory Method para criar instâncias de Veículos."""
    
    @staticmethod
    def criar(tipo_veiculo: str) -> Veiculo:
        tipo_veiculo = tipo_veiculo.lower().strip()
        
        if tipo_veiculo == "moto":
            return Moto()
        elif tipo_veiculo == "carro":
            return Carro()
        elif tipo_veiculo == "vip":
            return VeiculoVIP()
        else:
            raise ValueError(
                f"Tipo de veículo '{tipo_veiculo}' não reconhecido. "
                f"Use 'moto', 'carro' ou 'vip'."
            )
```

### PagamentoFactory (`modelos/pagamento.py`)

```python
class PagamentoFactory:
    """Factory Method para criar instâncias de Pagamentos."""
    
    @staticmethod
    def criar(tipo_pagamento: str, valor: float) -> Pagamento:
        tipo_pagamento = tipo_pagamento.lower().strip()
        
        if tipo_pagamento == "pix":
            return PagamentoPix(valor)
        elif tipo_pagamento == "cartao":
            return PagamentoCartao(valor)
        elif tipo_pagamento == "dinheiro":
            return PagamentoDinheiro(valor)
        else:
            raise ValueError(
                f"Tipo de pagamento '{tipo_pagamento}' não reconhecido. "
                f"Use 'pix', 'cartao' ou 'dinheiro'."
            )
```

## 💎 Benefícios Obtidos

| Benefício | Descrição |
|-----------|-----------|
| **Desacoplamento** | Código cliente não depende de classes concretas |
| **Centralização** | Toda lógica de criação em um único lugar |
| **Escalabilidade** | Adicionar novo tipo é trivial (~3 linhas) |
| **Manutenção** | Mudanças só afetam a factory, não o resto do código |
| **Validação** | Erros tratados centralizadamente |
| **Legibilidade** | `criar("tipo")` é mais claro e expressivo |

## 🚀 Como Estender (Exemplo)

### Adicionar novo veículo (Bicicleta)

```python
# 1. Adicionar a classe
class Bicicleta(Veiculo):
    def __init__(self):
        super().__init__("Bicicleta")
    
    def calcular_tarifa(self, distancia):
        return distancia * 0.5  # R$0.50 por km

# 2. Adicionar à factory (apenas 2 linhas!)
elif tipo_veiculo == "bicicleta":
    return Bicicleta()

# 3. Usar em qualquer lugar
bicicleta = VeiculoFactory.criar("bicicleta")

# ✨ Nenhuma outra mudança necessária!
```

### Adicionar novo tipo de pagamento (ex: Crédito)

```python
# 1. Adicionar a classe
class PagamentoCredito(Pagamento):
    def __init__(self, valor):
        super().__init__(valor)
    
    def processar_pagamento(self):
        self.status = "pendente de confirmação"
        print(f"Pagamento de R${self.valor} via crédito pendente")

# 2. Adicionar à factory
elif tipo_pagamento == "credito":
    return PagamentoCredito(valor)

# 3. Usar em qualquer lugar
credito = PagamentoFactory.criar("credito", 100)
```

## 📁 Arquivos Modificados

| Arquivo | Mudança | Detalhes |
|---------|---------|----------|
| `modelos/veiculo.py` | Adicionada `VeiculoFactory` | Classe com método estático `criar()` |
| `modelos/pagamento.py` | Adicionada `PagamentoFactory` | Classe com método estático `criar()` |
| `main.py` | Refatoradas 4 instanciações | Uso direto das factories em vez de classes concretas |
| `teste_factory.py` | Script de demonstração | Exemplos de uso e tratamento de erros |

## ✅ Teste de Validação

Para testar o padrão em ação:

```bash
python teste_factory.py
```

Esse script demonstra:
- ✅ Criação de veículos com factory
- ✅ Criação de pagamentos com factory
- ✅ Tratamento de erros
- ✅ Polimorfismo em ação

## Exemplos de Uso em main.py

```python
# 5. CORRIDA - Usando VeiculoFactory
veiculo = VeiculoFactory.criar("carro")
motorista.cadastrar_veiculo(veiculo)

# 6. PAGAMENTO - Usando PagamentoFactory
pagamento = PagamentoFactory.criar("pix", corrida.valor)
pagamento.processar_pagamento()

# 11. POLIMORFISMO PAGAMENTO - Criando múltiplos tipos
pagamentos = [
    PagamentoFactory.criar("pix", 50),
    PagamentoFactory.criar("cartao", 100),
    PagamentoFactory.criar("dinheiro", 30)
]

# 12. POLIMORFISMO VEÍCULO - Criando múltiplos tipos
veiculos = [
    VeiculoFactory.criar("moto"),
    VeiculoFactory.criar("carro"),
    VeiculoFactory.criar("vip")
]

for v in veiculos:
    corrida.escolher_veiculo(v)
    corrida.calcular_preco()
```

## Conclusão

O Factory Method torna o código mais flexível, reutilizável e fácil de manter. É especialmente útil quando:
- Há múltiplas classes concretas que implementam uma interface comum
- A escolha de qual classe instanciar depende de parâmetros de tempo de execução
- Espera-se adicionar novos tipos no futuro

A persistência de dados em `bancos_dados/` continua funcionando normalmente, pois os dados armazenam o tipo do objeto utilizado no sistema.
