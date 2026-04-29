# Documentação das Funcionalidades — Eve: Safety First

**Aluno:** Senan Isac Armel DJENONLO  
**Projeto:** Baseado no Uber  
**Sistema:** Eve - Safety First (segurança em primeiro lugar)

---

## Sumário

1. [Cadastro de Usuário](#1-cadastro-de-usuário)
2. [Login no Sistema](#2-login-no-sistema)
3. [Solicitar Corrida](#3-solicitar-corrida)
4. [Rastreamento](#4-rastreamento)
5. [Escolher Tipo de Veículo](#5-escolher-tipo-de-veículo)
6. [Pagamento](#6-pagamento)
7. [Histórico de Corridas](#7-histórico-de-corridas)
8. [Avaliação](#8-avaliação)
9. [Controle de Cancelamento](#9-controle-de-cancelamento)
10. [Suporte ao Cliente](#10-suporte-ao-cliente)

---

## 1. Cadastro de Usuário

**Classe:** `Usuario`, `Passageiro`, `Motorista`

**Objetivo:**  
Criar uma identidade digital para o usuário (passageiro ou motorista), garantindo a segurança e autenticidade dos dados antes do acesso ao sistema.

**Inputs:**

| Parâmetro        | Tipo   | Descrição                              |
|------------------|--------|----------------------------------------|
| `nome_completo`  | `str`  | Nome completo do usuário               |
| `cpf`            | `str`  | CPF do usuário (11 dígitos)            |
| `email`          | `str`  | Endereço de e-mail válido              |
| `senha`          | `str`  | Senha de acesso à conta                |
| `telefone`       | `str`  | Número de telefone do usuário          |
| `cnh` *(motorista)* | `str` | Carteira Nacional de Habilitação (11 dígitos) |
| `placa` *(motorista)* | `str` | Placa do veículo do motorista     |
| `modelo_veiculo` *(motorista)* | `str` | Modelo do veículo         |

**Outputs:**

| Resultado              | Tipo   | Descrição                                      |
|------------------------|--------|------------------------------------------------|
| Objeto `Passageiro` ou `Motorista` | objeto | Instância criada com ID único gerado automaticamente |
| Mensagem de confirmação | `str` | Ex: `"Passageiro João criado com ID: ..."` |
| `True` / `False`       | `bool` | Resultado da validação dos documentos          |

**Fluxo:**
1. O usuário preenche os dados do formulário
2. O sistema chama `validar_documentos()` para verificar CPF, e-mail e CNH (motorista)
3. Se válido, o objeto é criado com `cadastrar()`
4. A conta é ativada com `confirmar_conta()`

**Validações aplicadas:**
- CPF: algoritmo de verificação dos dois dígitos verificadores
- E-mail: formato válido via expressão regular
- CNH *(motorista)*: algoritmo de verificação dos dois dígitos verificadores

---

## 2. Login no Sistema

**Classe:** `Login`

**Objetivo:**  
Autenticar o usuário no sistema, verificando suas credenciais e o status de ativação da conta.

**Inputs:**

| Parâmetro | Tipo  | Descrição                    |
|-----------|-------|------------------------------|
| `email`   | `str` | E-mail cadastrado do usuário |
| `senha`   | `str` | Senha cadastrada do usuário  |

**Outputs:**

| Resultado             | Tipo   | Descrição                                         |
|-----------------------|--------|---------------------------------------------------|
| `True`                | `bool` | Login realizado com sucesso                       |
| `False`               | `bool` | Falha na autenticação (dados incorretos ou conta não confirmada) |
| Mensagem de status    | `str`  | Ex: `"Login realizado com sucesso!"` ou `"Dados incorretos"` |

**Fluxo:**
1. O usuário informa e-mail e senha
2. O sistema compara com os dados armazenados no objeto `Usuario`
3. Verifica se `status_conta` está ativo (`True`)
4. Retorna resultado da autenticação

**Regras:**
- A conta deve estar confirmada (`status_conta = True`) para o login ser aceito
- E-mail e senha devem corresponder exatamente aos dados cadastrados

---

## 3. Solicitar Corrida

**Classe:** `Corrida`

**Objetivo:**  
Permitir que o passageiro solicite uma corrida informando origem e destino, calcule a distância e confirme o pedido.

**Inputs:**

| Parâmetro    | Tipo         | Descrição                              |
|--------------|--------------|----------------------------------------|
| `passageiro` | `Passageiro` | Objeto do passageiro que solicita      |
| `origem`     | `str`        | Local de partida da corrida            |
| `destino`    | `str`        | Local de chegada da corrida            |
| `veiculo`    | `Veiculo`    | Tipo de veículo escolhido              |

**Outputs:**

| Resultado           | Tipo    | Descrição                                    |
|---------------------|---------|----------------------------------------------|
| `id_corrida`        | `str`   | Identificador único da corrida (UUID)        |
| `distancia`         | `float` | Distância calculada em km (1 a 50 km)        |
| `valor`             | `float` | Preço da corrida calculado pela tarifa do veículo |
| `status`            | `str`   | Estado da corrida: `"pendente"` → `"confirmada"` |
| Mensagem de status  | `str`   | Ex: `"Corrida confirmada"`                   |

**Fluxo:**
1. O passageiro informa origem e destino
2. O sistema calcula a distância com `calcular_distancia()`
3. O passageiro escolhe o tipo de veículo com `escolher_veiculo()`
4. O preço é calculado com `calcular_preco()`
5. A corrida é confirmada com `confirmar()`

---

## 4. Rastreamento

**Classe:** `Rastreamento`

**Objetivo:**  
Dar ao passageiro visibilidade em tempo real sobre a localização do motorista e o tempo estimado de chegada.

**Inputs:**

| Parâmetro  | Tipo      | Descrição                          |
|------------|-----------|------------------------------------|
| `corrida`  | `Corrida` | Objeto da corrida em andamento     |
| `local`    | `str`     | Localização atual do motorista     |

**Outputs:**

| Resultado               | Tipo  | Descrição                                  |
|-------------------------|-------|--------------------------------------------|
| Mensagem de localização | `str` | Ex: `"Motorista está em: Av. Paulista"`    |
| Tempo estimado          | `str` | Ex: `"Tempo estimado: 5 minutos"`          |

**Fluxo:**
1. O sistema recebe as coordenadas do motorista
2. `atualizar_localizacao()` exibe a posição atual
3. `calcular_tempo()` informa o tempo estimado de chegada

---

## 5. Escolher Tipo de Veículo

**Classe:** `Veiculo` *(classe abstrata)*, `Moto`, `Carro`, `VeiculoVIP`

**Objetivo:**  
Permitir que o passageiro escolha a categoria de veículo conforme sua necessidade financeira ou de espaço, aplicando a tarifa correspondente.

**Inputs:**

| Parâmetro   | Tipo    | Descrição                  |
|-------------|---------|----------------------------|
| `distancia` | `float` | Distância da corrida em km |

**Outputs:**

| Resultado | Tipo    | Descrição                                   |
|-----------|---------|---------------------------------------------|
| `valor`   | `float` | Tarifa calculada conforme o tipo de veículo |

**Tarifas por categoria:**

| Veículo      | Tarifa por km | Exemplo (10 km) |
|--------------|---------------|-----------------|
| `Moto`       | R$ 1,00/km    | R$ 10,00        |
| `Carro`      | R$ 2,00/km    | R$ 20,00        |
| `VeiculoVIP` | R$ 4,00/km    | R$ 40,00        |

---

## 6. Pagamento

**Classe:** `Pagamento` *(classe abstrata)*, `PagamentoPix`, `PagamentoCartao`, `PagamentoDinheiro`

**Objetivo:**  
Garantir que o motorista seja remunerado e que o passageiro possa pagar de forma prática com o método de sua escolha.

**Inputs:**

| Parâmetro | Tipo    | Descrição                      |
|-----------|---------|--------------------------------|
| `valor`   | `float` | Valor total da corrida a pagar |

**Outputs:**

| Resultado               | Tipo  | Descrição                                              |
|-------------------------|-------|--------------------------------------------------------|
| `status`                | `str` | Estado do pagamento: `"aprovado"` ou `"pago na entrega"` |
| Mensagem de confirmação | `str` | Ex: `"Pagamento de R$20.0 via PIX aprovado"`           |

**Comportamento por método:**

| Classe              | Método | Status resultante   |
|---------------------|--------|---------------------|
| `PagamentoPix`      | PIX    | `"aprovado"`        |
| `PagamentoCartao`   | Cartão | `"aprovado"`        |
| `PagamentoDinheiro` | Dinheiro | `"pago na entrega"` |

---

## 7. Histórico de Corridas

**Classe:** `Historico`

**Objetivo:**  
Permitir que o usuário consulte suas viagens anteriores com origem, destino e status de cada corrida.

**Inputs:**

| Parâmetro | Tipo      | Descrição                              |
|-----------|-----------|----------------------------------------|
| `usuario` | `Usuario` | Usuário dono do histórico              |
| `corrida` | `Corrida` | Corrida a ser adicionada ao histórico  |

**Outputs:**

| Resultado            | Tipo   | Descrição                                          |
|----------------------|--------|----------------------------------------------------|
| Lista de corridas    | `list` | Lista de objetos `Corrida` registrados             |
| Mensagem de exibição | `str`  | Ex: `"São Paulo -> Rio de Janeiro (confirmada)"`   |

**Fluxo:**
1. Após cada corrida concluída, `adicionar()` registra o objeto `Corrida`
2. O usuário pode chamar `visualizar()` para ver todas as corridas anteriores

---

## 8. Avaliação

**Classe:** `Avaliacao`

**Objetivo:**  
Permitir que o passageiro avalie sua experiência com o motorista após a corrida, contribuindo para a qualidade do serviço.

**Inputs:**

| Parâmetro    | Tipo        | Descrição                              |
|--------------|-------------|----------------------------------------|
| `usuario`    | `Passageiro` | Passageiro que realiza a avaliação    |
| `motorista`  | `Motorista`  | Motorista sendo avaliado              |
| `nota`       | `int`        | Nota de 1 a 5 estrelas                |
| `comentario` | `str`        | Comentário escrito sobre a experiência |

**Outputs:**

| Resultado             | Tipo  | Descrição                                                |
|-----------------------|-------|----------------------------------------------------------|
| Mensagem de avaliação | `str` | Ex: `"João avaliou Carlos — Nota: 5 - Ótimo motorista!"` |

**Fluxo:**
1. Após a conclusão da corrida, o passageiro cria um objeto `Avaliacao`
2. O método `avaliar()` registra e exibe a nota e o comentário

---

## 9. Controle de Cancelamento

**Classe:** `ControleCancelamento`

**Objetivo:**  
Evitar que motoristas aceitem e cancelem corridas com frequência, causando atrasos aos passageiros. O sistema impõe um limite diário de cancelamentos e exige um motivo válido.

**Inputs:**

| Parâmetro        | Tipo  | Descrição                                         |
|------------------|-------|---------------------------------------------------|
| `limite_por_dia` | `int` | Número máximo de cancelamentos permitidos por dia |
| `motivo`         | `str` | Motivo do cancelamento (deve ser um dos válidos)  |

**Motivos válidos:**
- `"Problema no carro"`
- `"Trânsito extremo"`
- `"Emergência"`

**Outputs:**

| Resultado                   | Tipo  | Descrição                                                       |
|-----------------------------|-------|-----------------------------------------------------------------|
| Confirmação de cancelamento | `str` | Ex: `"Corrida cancelada. Motivo: Emergência"`                   |
| Mensagem de erro            | `str` | Ex: `"Limite de cancelamentos atingido"` ou `"Motivo inválido"` |
| Reset automático            | —     | Contador zerado automaticamente a cada novo dia                 |

**Fluxo:**
1. O motorista solicita cancelamento informando um motivo
2. O sistema verifica se o motivo é válido
3. O sistema verifica se o limite diário não foi atingido
4. Se as condições forem satisfeitas, o cancelamento é registrado
5. O contador é resetado automaticamente no dia seguinte

**Regras:**
- Motivo é obrigatório — cancelamento sem motivo é recusado
- Motivo fora da lista de válidos é recusado
- Ao atingir o limite diário, nenhum cancelamento adicional é permitido

---

## 10. Suporte ao Cliente

**Classe:** `Suporte`

**Objetivo:**  
Ajudar o usuário em caso de problemas técnicos, perda de objetos ou reclamações, mantendo um histórico das mensagens enviadas.

**Inputs:**

| Parâmetro  | Tipo      | Descrição                               |
|------------|-----------|-----------------------------------------|
| `usuario`  | `Usuario` | Usuário que abre o atendimento          |
| `mensagem` | `str`     | Conteúdo da mensagem enviada ao suporte |

**Outputs:**

| Resultado              | Tipo   | Descrição                            |
|------------------------|--------|--------------------------------------|
| Confirmação de envio   | `str`  | `"Mensagem enviada ao suporte"`      |
| Histórico de mensagens | `list` | Lista de todas as mensagens enviadas |

**Fluxo:**
1. O usuário envia uma mensagem com `enviar()`
2. A mensagem é armazenada na lista `mensagens`
3. O usuário pode consultar todas as mensagens anteriores com `historico()`

---

*Aluno: Senan Isac Armel DJENONLO — Eve: Safety First*
