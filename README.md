
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


##  Funcionalidades principais

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

##  Conceitos de POO utilizados

- Herança
- Polimorfismo
- Encapsulamento
- Classes abstratas


## Aplicação de Factory Method

O padrão criacional Factory Method pode ser aplicado nos módulos `modelos/veiculo.py` e `modelos/pagamento.py`, pois o sistema possui múltiplas classes concretas que representam variações do mesmo comportamento.

No módulo de veículos, existem diferentes tipos como `Moto`, `Carro` e `VeiculoVIP`, cada um implementando sua própria lógica de tarifa. Já no módulo de pagamentos, classes como `PagamentoPix`, `PagamentoCartao` e `PagamentoDinheiro` representam diferentes formas de processamento de pagamento.

Atualmente, a escolha dessas classes é realizada diretamente no `main.py` através de condicionais e instanciações explícitas. Com o Factory Method, essa criação poderia ser centralizada em uma classe fábrica, reduzindo acoplamento e melhorando a organização do sistema.

Exemplo conceitual:

```python
veiculo = VeiculoFactory.criar("carro")
pagamento = PagamentoFactory.criar("pix", valor)

## 📚 Documentação

- [Herança](docss/heranca.md)
- [Polimorfismo](docss/polimorfismo.md)
- [Funcionalidades](docss/documentacao_funcionalidades.md)


## Como Testar
Certifique-se de ter o Python instalado e execute:
```bash
python main.py
 
