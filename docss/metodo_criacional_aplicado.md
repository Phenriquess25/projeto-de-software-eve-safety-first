# Factory Method aplicado no projeto

## O que foi aplicado

O projeto usa o padrão criacional Factory Method para centralizar a criação de objetos em vez de instanciar as classes concretas diretamente no fluxo principal.

Neste sistema, o padrão foi aplicado em dois pontos:

- `VeiculoFactory` em [modelos/veiculo.py](../modelos/veiculo.py)
- `PagamentoFactory` em [modelos/pagamento.py](../modelos/pagamento.py)

## Como ele está sendo aplicado

### 1. Criação de veículos

A fábrica `VeiculoFactory` recebe uma string com o tipo do veículo e devolve a classe correta:

```python
veiculo = VeiculoFactory.criar("carro")
```

Tipos aceitos:

- `moto` -> cria `Moto`
- `carro` -> cria `Carro`
- `vip` -> cria `VeiculoVIP`

### 2. Criação de pagamentos

A fábrica `PagamentoFactory` recebe o tipo de pagamento e o valor da corrida:

```python
pagamento = PagamentoFactory.criar("pix", 100)
```

Tipos aceitos:

- `pix` -> cria `PagamentoPix`
- `cartao` -> cria `PagamentoCartao`
- `dinheiro` -> cria `PagamentoDinheiro`

## Onde ele está sendo usado

### No arquivo [main.py](../main.py)

O `main.py` é o principal consumidor das factories. Ele usa esse padrão em:

- `solicitar_corrida()`
  - escolhe o veículo com `VeiculoFactory.criar(...)`
  - escolhe o pagamento com `PagamentoFactory.criar(...)`
- testes de polimorfismo dentro do fluxo de corrida
- menu do motorista, quando exibe as corridas disponíveis e calcula valores conforme o tipo de veículo

### No arquivo [teste_factory.py](../teste_factory.py)

Esse arquivo mostra o padrão funcionando de forma isolada, validando:

- criação de veículos
- criação de pagamentos
- tratamento de erros quando o tipo passado é inválido

### No arquivo [teste_completo.py](../teste_completo.py)

Esse script usa as factories para simular o sistema completo:

- cria corridas com veículo escolhido dinamicamente
- processa pagamentos por tipo
- salva tudo no banco JSON

## Por que isso foi usado

O Factory Method foi escolhido para evitar `if/elif` espalhado pelo sistema e para deixar a criação dos objetos mais organizada.

Com isso, o código ficou:

- mais fácil de manter
- mais fácil de expandir
- menos acoplado às classes concretas
- mais legível no fluxo principal

## Exemplo prático no projeto

### Antes

```python
from modelos.veiculo import Carro
veiculo = Carro()
```

### Depois

```python
from modelos.veiculo import VeiculoFactory
veiculo = VeiculoFactory.criar("carro")
```

## Resumo

No projeto, o Factory Method está sendo aplicado para criar:

- veículos
- pagamentos

E ele aparece principalmente em:

- [modelos/veiculo.py](../modelos/veiculo.py)
- [modelos/pagamento.py](../modelos/pagamento.py)
- [main.py](../main.py)
- [teste_factory.py](../teste_factory.py)
- [teste_completo.py](../teste_completo.py)

Esse padrão ajuda o sistema a ficar mais organizado e pronto para crescer sem bagunçar o código principal.
