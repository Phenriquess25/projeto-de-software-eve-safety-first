# Herança — Eve: Safety First

**Aluno:** Senan Isac Armel DJENONLO  
**Projeto:** Baseado no Uber  

---

## O que é Herança?

A herança permite que uma classe filha **reaproveite** automaticamente os atributos e métodos de uma classe mãe, sem precisar reescrevê-los. A classe filha pode também adicionar novos comportamentos ou modificar os existentes. Em Python, a herança é declarada passando a classe mãe entre parênteses: `class Filha(Mae)`.

---

## Onde foi usada no projeto

A herança foi aplicada em **3 hierarquias** no código.

---

## 1. `Usuario` → `Passageiro` e `Motorista`

### Onde no código

```python
class Passageiro(Usuario):
    def __init__(self, nome_completo, cpf, email, senha, telefone):
        super().__init__(nome_completo, cpf, email, senha, telefone, "passageiro")
        self.historico = []

class Motorista(Usuario):
    def __init__(self, nome_completo, cpf, email, senha, telefone, cnh, placa, modelo_veiculo):
        super().__init__(nome_completo, cpf, email, senha, telefone, "motorista")
        self.cnh = cnh
        self.placa = placa
        self.modelo_veiculo = modelo_veiculo
        self.veiculo = None
        self.cancelamentos = 0
```

### Por que foi usada

No sistema Eve, tanto o passageiro quanto o motorista são usuários. Os dois têm nome, CPF, e-mail, senha, telefone e precisam de cadastro e login. Sem herança, esses atributos e métodos teriam que ser escritos duas vezes — o que geraria duplicação de código e dificultaria a manutenção.

Com a herança, a classe `Usuario` centraliza tudo que é comum. `Passageiro` e `Motorista` herdam essa base via `super().__init__()` e acrescentam apenas o que é específico a cada um.

### O que é herdado automaticamente

| Atributos herdados                                              | Métodos herdados                   |
|-----------------------------------------------------------------|------------------------------------|
| `id_usuario`, `nome_completo`, `cpf`, `email`, `senha`, `telefone`, `status_conta` | `cadastrar()`, `confirmar_conta()`, `validar_documentos()` |

### O que cada subclasse adiciona

| Classe       | Atributos extras                                             | Métodos extras        |
|--------------|--------------------------------------------------------------|-----------------------|
| `Passageiro` | `historico`                                                  | `solicitar_corrida()` |
| `Motorista`  | `cnh`, `placa`, `modelo_veiculo`, `veiculo`, `cancelamentos` | `cadastrar_veiculo()` |

### Diagrama

```
Usuario
├── id_usuario
├── nome_completo
├── cpf, email, senha, telefone
├── cadastrar()
├── confirmar_conta()
└── validar_documentos()
        │
        ├── Passageiro
        │     └── + historico
        │     └── + solicitar_corrida()
        │
        └── Motorista
              └── + cnh, placa, modelo_veiculo
              └── + cadastrar_veiculo()
```

---

## 2. `Veiculo` → `Moto`, `Carro`, `VeiculoVIP`

### Onde no código

```python
class Veiculo(ABC):
    def __init__(self, tipo):
        self.tipo = tipo

class Moto(Veiculo):
    def __init__(self):
        super().__init__("Moto")

class Carro(Veiculo):
    def __init__(self):
        super().__init__("Carro")

class VeiculoVIP(Veiculo):
    def __init__(self):
        super().__init__("VIP")
```

### Por que foi usada

Os três tipos de veículo compartilham a mesma estrutura base — todos têm um atributo `tipo`. Em vez de criar três classes independentes repetindo essa estrutura, `Veiculo` define a base comum. Cada subclasse herda o atributo `tipo` via `super().__init__()` e só precisa passar seu próprio nome.

Além disso, `Veiculo` é uma **classe abstrata** (`ABC`), o que garante que nenhum objeto `Veiculo` genérico possa ser criado diretamente — apenas os tipos concretos (`Moto`, `Carro`, `VeiculoVIP`).

### O que é herdado automaticamente

| Atributo herdado | Descrição                        |
|------------------|----------------------------------|
| `tipo`           | Nome do tipo de veículo (`str`)  |

### Diagrama

```
Veiculo (ABC)
└── tipo
└── calcular_tarifa() ← @abstractmethod
        │
        ├── Moto         → tipo = "Moto"
        ├── Carro        → tipo = "Carro"
        └── VeiculoVIP   → tipo = "VIP"
```

---

## 3. `Pagamento` → `PagamentoPix`, `PagamentoCartao`, `PagamentoDinheiro`

### Onde no código

```python
class Pagamento(ABC):
    def __init__(self, valor):
        self.valor = valor
        self.status = "pendente"

    def mostrar_status(self):
        print(f"Status do pagamento: {self.status}")

class PagamentoPix(Pagamento):
    def __init__(self, valor):
        super().__init__(valor)

class PagamentoCartao(Pagamento):
    def __init__(self, valor):
        super().__init__(valor)

class PagamentoDinheiro(Pagamento):
    def __init__(self, valor):
        super().__init__(valor)
```

### Por que foi usada

Os três métodos de pagamento compartilham os mesmos atributos base: `valor` e `status`. A classe `Pagamento` também centraliza o método `mostrar_status()`, que funciona de forma idêntica para os três — não há motivo para reescrevê-lo em cada subclasse.

Com a herança, cada subclasse herda essa base via `super().__init__(valor)` e só precisa implementar sua própria lógica de processamento.

### O que é herdado automaticamente

| Atributos herdados    | Métodos herdados    |
|-----------------------|---------------------|
| `valor`, `status`     | `mostrar_status()`  |

### Diagrama

```
Pagamento (ABC)
├── valor
├── status = "pendente"
├── mostrar_status()
└── processar_pagamento() ← @abstractmethod
        │
        ├── PagamentoPix      → status = "aprovado"
        ├── PagamentoCartao   → status = "aprovado"
        └── PagamentoDinheiro → status = "pago na entrega"
```

---

## Resumo Geral

| Classe mãe  | Subclasses                                                  | O que é compartilhado via herança               |
|-------------|-------------------------------------------------------------|-------------------------------------------------|
| `Usuario`   | `Passageiro`, `Motorista`                                   | Atributos de identidade + `cadastrar()`, `confirmar_conta()` |
| `Veiculo`   | `Moto`, `Carro`, `VeiculoVIP`                               | Atributo `tipo`                                 |
| `Pagamento` | `PagamentoPix`, `PagamentoCartao`, `PagamentoDinheiro`      | Atributos `valor`, `status` + `mostrar_status()` |

---

*Aluno: Senan Isac Armel DJENONLO — Eve: Safety First*
