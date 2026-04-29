# Polimorfismo — Eve: Safety First

**Aluno:** Senan Isac Armel DJENONLO  
**Projeto:** Baseado no Uber  

---

## O que é Polimorfismo?

O polimorfismo permite chamar **o mesmo método** em objetos de tipos diferentes e obter **comportamentos diferentes** — sem que o código que faz a chamada precise saber qual tipo exato está sendo usado. Em Python, isso é implementado sobrescrevendo métodos nas subclasses.

---

## Onde foi usado no projeto

O polimorfismo foi aplicado em **3 lugares** no código.

---

## 1. `calcular_tarifa()` — em `Veiculo`

### Onde no código

```python
# Definição na classe abstrata — obriga todas as subclasses a implementar
class Veiculo(ABC):
    @abstractmethod
    def calcular_tarifa(self, distancia):
        pass

# Cada subclasse implementa com sua própria lógica
class Moto(Veiculo):
    def calcular_tarifa(self, distancia):
        return distancia * 1

class Carro(Veiculo):
    def calcular_tarifa(self, distancia):
        return distancia * 2

class VeiculoVIP(Veiculo):
    def calcular_tarifa(self, distancia):
        return distancia * 4
```

### Uso polimórfico real — em `Corrida.calcular_preco()`

```python
def calcular_preco(self):
    self.valor = self.veiculo.calcular_tarifa(self.distancia)
```

### Por que foi usado

Este é o uso mais natural do polimorfismo no projeto. Quando o passageiro confirma a corrida, o sistema chama `calcular_tarifa()` sem saber se o veículo é uma `Moto`, um `Carro` ou um `VeiculoVIP`. O Python resolve automaticamente qual implementação executar conforme o objeto real.

Isso torna o código extensível: se no futuro for adicionado um novo tipo de veículo (ex: `VeiculoEletrico`), basta criar a nova subclasse com sua própria tarifa — sem precisar modificar nada na classe `Corrida`.

### Por que `@abstractmethod` foi usado

O `@abstractmethod` garante que nenhuma subclasse de `Veiculo` possa ser instanciada sem implementar `calcular_tarifa()`. Se alguém criar um novo tipo de veículo e esquecer de definir a tarifa, o Python lança um erro imediatamente — o que evita bugs silenciosos no sistema.

### Resultado por tipo

| Veículo      | Chamada                        | Resultado (10 km) |
|--------------|--------------------------------|-------------------|
| `Moto`       | `moto.calcular_tarifa(10)`     | R$ 10,00          |
| `Carro`      | `carro.calcular_tarifa(10)`    | R$ 20,00          |
| `VeiculoVIP` | `vip.calcular_tarifa(10)`      | R$ 40,00          |

---

## 2. `validar_documentos()` — em `Usuario`

### Onde no código

```python
# Método base em Usuario — valida nome, CPF e e-mail
class Usuario:
    def validar_documentos(self):
        if not self.nome_completo:
            return False
        if not validar_cpf(self.cpf):
            return False
        if not validar_email(self.email):
            return False
        return True

# Passageiro sobrescreve e reutiliza a lógica base com super()
class Passageiro(Usuario):
    def validar_documentos(self):
        if not super().validar_documentos():
            return False
        print("Documentos do passageiro validados")
        return True

# Motorista sobrescreve, reutiliza a lógica base e adiciona validação da CNH
class Motorista(Usuario):
    def validar_documentos(self):
        if not super().validar_documentos():
            return False
        if not validar_cnh(self.cnh):
            print("CNH inválida")
            return False
        print("Documentos do motorista validados")
        return True
```

### Por que foi usado

Passageiro e motorista têm regras de validação diferentes. O passageiro precisa apenas de CPF e e-mail válidos. O motorista precisa de tudo isso **mais** a CNH. Com o polimorfismo, o sistema pode chamar `usuario.validar_documentos()` sem saber se o objeto é um passageiro ou motorista — cada um executa sua própria validação.

O uso de `super()` evita duplicação de código: a validação comum (CPF, e-mail) está escrita uma só vez em `Usuario` e é reaproveitada pelas duas subclasses.

### Comportamento por tipo

| Tipo         | Valida nome + CPF + e-mail | Valida CNH |
|--------------|:--------------------------:|:----------:|
| `Passageiro` | ✓                          | ✗          |
| `Motorista`  | ✓                          | ✓          |

---

## 3. `processar_pagamento()` — em `Pagamento`

### Onde no código

```python
# Definição na classe abstrata — obriga todas as subclasses a implementar
class Pagamento(ABC):
    @abstractmethod
    def processar_pagamento(self):
        pass

# Cada subclasse implementa de forma diferente
class PagamentoPix(Pagamento):
    def processar_pagamento(self):
        self.status = "aprovado"
        print(f"Pagamento de R${self.valor} via PIX aprovado")

class PagamentoCartao(Pagamento):
    def processar_pagamento(self):
        self.status = "aprovado"
        print(f"Pagamento de R${self.valor} com cartão aprovado")

class PagamentoDinheiro(Pagamento):
    def processar_pagamento(self):
        self.status = "pago na entrega"
        print(f"Pagamento de R${self.valor} será feito em dinheiro")
```

### Por que foi usado

Cada método de pagamento tem um comportamento diferente — PIX e cartão são aprovados imediatamente, dinheiro é pago na entrega. Com o polimorfismo, o sistema pode chamar `pagamento.processar_pagamento()` independentemente do método escolhido pelo passageiro.

Assim como nos veículos, adicionar um novo método de pagamento no futuro (ex: `PagamentoCripto`) não exige alterar nenhum outro código — basta criar a nova subclasse com sua própria lógica.

### Resultado por tipo

| Classe              | Chamada                       | Status resultante   |
|---------------------|-------------------------------|---------------------|
| `PagamentoPix`      | `pix.processar_pagamento()`   | `"aprovado"`        |
| `PagamentoCartao`   | `cartao.processar_pagamento()` | `"aprovado"`       |
| `PagamentoDinheiro` | `dinheiro.processar_pagamento()` | `"pago na entrega"` |

---

## Resumo

| Método sobrescrito      | Classe base  | Subclasses                                        | Usado diretamente em     |
|-------------------------|--------------|---------------------------------------------------|--------------------------|
| `calcular_tarifa()`     | `Veiculo`    | `Moto`, `Carro`, `VeiculoVIP`                     | `Corrida.calcular_preco()` |
| `validar_documentos()`  | `Usuario`    | `Passageiro`, `Motorista`                         | Cadastro de usuário      |
| `processar_pagamento()` | `Pagamento`  | `PagamentoPix`, `PagamentoCartao`, `PagamentoDinheiro` | Fluxo de pagamento  |

---

*Aluno: Senan Isac Armel DJENONLO — Eve: Safety First*
